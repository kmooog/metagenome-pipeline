import luigi
import glob 
import subprocess
import os
import pathlib
from pathlib import Path

files = "*.gz"
file_list = glob.glob(files)
file_list = [a.replace(".fastq.gz","") for a in file_list]

file_list_merged = []

cwd = Path.cwd()

eggnog_mapper_path = "/work/G10800/kumay/eggnog-mapper/emapper.py"

for file_tmp in file_list:
    if file_tmp.find("_R1_") != -1:
        file_list_merged.append(file_tmp)

script_path = "/work/G10800/kumay/metagenome-pipeline/script/"

print("following files detected")
print(file_list)

class _1_TrimGalore(luigi.Task):
    task_namespace = 'metagenomes'

    def run(self):
        print("_1_TrimGalore: run")
        cmd = 'mkdir 01_TrimGalore && cd 01_TrimGalore && cp ../*.fastq.gz . && sh {0}run_TrimGalore.sh && cd ..'.format(script_path)
        os.system(cmd)
    def output(self):
        print("Task1: output")
        outputDict = {}
        print(file_list)
        for i, outFile in enumerate(file_list):
            print(outFile)
            count = 0
            if outFile.find("_R1_") != -1:
                count += 1
                outputDict["output" + str(2 * count - 1)] = luigi.LocalTarget('01_TrimGalore/' + outFile + "_val_1.fq.gz")
                outputDict["output" + str(2 * count)] = luigi.LocalTarget('01_TrimGalore/' + outFile.replace("_R1_","_R2_") + "_val_2.fq.gz")
        return outputDict

class _2_Flash(luigi.Task):
    task_namespace = 'metagenomes'

    def requires(self):
        print("_2_Flash: requires")
        return _1_TrimGalore()

    def run(self):
        print("_2_Flash: run")
        cmd = 'mkdir 02_Flash && cd 02_Flash && cp ../01_TrimGalore/*_val_*.fq.gz . && sh {0}run_FLASH.sh && cd ..'.format(script_path)
        os.system(cmd)
    def output(self):
        print("_2_Flash: output")
        outputDict = {}
        for i, outFile in enumerate(file_list_merged):
           outputDict["output" + str(i)] = luigi.LocalTarget('02_Flash/' + outFile + ".extendedFrags.fastq")
           print("_2_Flash output: " + '02_Flash/' + outFile + ".extendedFrags.fastq" )
        return outputDict

class _3_bowtie2(luigi.Task):
    task_namespace = 'metagenomes'

    def requires(self):
        print("_3_bowtie2: requires")
        return _2_Flash()

    def run(self):
        print("_3_bowtie2: run")
        cmd = 'mkdir 03_bowtie2 && cd 03_bowtie2 && cp ../02_Flash/*.extendedFrags.fastq . && sh {0}run_bowtie2.sh && cd ..'.format(script_path)
        os.system(cmd)
    def output(self):
        print("_3_bowtie2: output")
        outputDict = {}
        for i, outFile in enumerate(file_list_merged):
           outputDict["output" + str(i)] = luigi.LocalTarget('03_bowtie2/' + outFile + ".nophix.fastq")
        return outputDict

class _4_megahit(luigi.Task):
    task_namespace = 'metagenomes'

    def requires(self):
        print("_4_megahit: requires")
        return _3_bowtie2()

    def run(self):
        print("_4_megahit: run")
        cmd = 'mkdir 04_megahit && cd 04_megahit && cp ../03_bowtie2/*.nophix.fastq .'
        os.system(cmd)
        for input_file in (file_list_merged):
           current_path = cwd/'04_megahit'
           subprocess.Popen('echo ${FASTQ_FILE} > tmpout'.split(), stdout=subprocess.PIPE,cwd=current_path)
           subprocess.Popen('qsub -q l {0}run_megahit.sh -v FASTQ_FILE={1},MEGAHIT_DIR={2}'.format(script_path,input_file,os.getcwd()+"/04_megahit").split(),cwd=current_path)
    def output(self):
        print("_4_megahit: output")
        outputDict = {}
        for i, outFile in enumerate(file_list_merged):
           outputDict["output" + str(i)] = luigi.LocalTarget('04_megahit/' + outFile + ".nophixassembled/final.contigs.fa")
        return outputDict


class _5_Prodigal(luigi.Task):
    task_namespace = 'metagenomes'

    def requires(self):
        print("_5_Prodigal: requires")
        return _4_megahit()

    def run(self):
        print("_5_Prodigal: run")
        cmd = 'mkdir 05_Prodigal && cd 05_Prodigal sh {0}run_Prodigal.sh && cd ..'.format(script_path)
        os.system(cmd)
    def output(self):
        print("_5_Prodigal: output")
        outputDict = {}
        for i, outFile in enumerate(file_list_merged):
           outputDict["output" + str(i)] = luigi.LocalTarget('05_Prodigal/' + outFile + ".nophixassembled.faa")
           outputDict["output" + str(i)] = luigi.LocalTarget('05_Prodigal/' + outFile + ".nophixassembled.fna")
        return outputDict

class _6_eggnog_mapper(luigi.Task):
    task_namespace = 'metagenomes'
    # ここもshell scriptにしてqsubしたほうが良さそう
    def requires(self):
        print("_6_eggnog_mapper: requires")
        return _5_Prodigal()

    def run(self):
        print("_6_eggnog_mapper: run")
        p = pathlib.Path('06_eggnog-mapper')
        p.mkdir()
        workdir = cwd / '06_eggnog-mapper'
        for i, outFile in enumerate(file_list_merged):
           subprocess.Popen('qsub -q l {0}run_eggnog-mapper.sh -v EMAPPER_PATH={1},FNA_FILE={2},OUTPUT_FILE={3}'.format(script_path,eggnog_mapper_path,outFile + ".nophixassembled.fna", outFile + ".emapper"),cwd=workdir)
    def output(self):
        print("_6_eggnog_mapper: output")
        outputDict = {}
        for i, outFile in enumerate(file_list_merged):
           outputDict["output" + str(i)] = luigi.LocalTarget('06_eggnog-mapper/' + outFile + ".emapper")
        return outputDict





if __name__ == '__main__':
    luigi.run(['metagenomes._5_Prodigal', '--workers', '1', '--local-scheduler'])
