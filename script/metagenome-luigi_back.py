import luigi
import glob 
import subprocess
import os
import pathlib
from pathlib import Path

files = "*.fq.gz"
file_list = glob.glob(files)
file_list = [a.replace(".fq.gz","") for a in file_list]

file_list_merged = []

cwd = Path.cwd()

eggnog_mapper_path = "/work/G10800/kumay/eggnog-mapper/emapper.py"

for file_tmp in file_list:
    if file_tmp.find("_1") != -1:
        file_list_merged.append(file_tmp)

script_path = "/work/G10800/kumay/metagenome-pipeline/script/"

print("following files detected")
print(file_list)

class _1_TrimGalore(luigi.Task):
    task_namespace = 'metagenomes'

    def run(self):
        print("_1_TrimGalore: run")
        cmd = 'mkdir 01_TrimGalore && cd 01_TrimGalore && cp ../*.fq.gz .'
        os.system(cmd)
        for input_file in (file_list_merged):
           current_path = cwd/'01_TrimGalore'
           path_for_check = current_path/(input_file + "_trimmed.fq.gz")
           if path_for_check.is_file():
              subprocess.Popen('qsub -q l {0}run_TrimGalore.sh -v FASTQ_FILE={1}.fq.gz,TRIMGALORE_DIR={2}'.format(script_path,input_file,os.getcwd()+"/01_TrimGalore").split(),cwd=current_path)
              print('qsub -q l {0}run_TrimGalore.sh -v FASTQ_FILE={1}.fq.gz,TRIMGALORE_DIR={2}'.format(script_path,input_file,os.getcwd()+"/01_TrimGalore"))
    def output(self):
        print("Task1: output")
        outputDict = {}
        print(file_list)
        for i, outFile in enumerate(file_list):
            print(outFile)
            count = 0
            if outFile.find("_1") != -1:
                count += 1
                outputDict["output" + str(2 * count - 1)] = luigi.LocalTarget('01_TrimGalore/' + outFile + "_val_1.fq.gz")
                outputDict["output" + str(2 * count)] = luigi.LocalTarget('01_TrimGalore/' + outFile.replace("_1","_2") + "_val_2.fq.gz")
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

class _35_prinseq(luigi.Task):
    task_namespace = 'metagenomes'

    def requires(self):
        print("_35_prinseq: requires")
        return _3_bowtie2()

    def run(self):
        print("_35_prinseq: run")
        cmd = 'mkdir 035_prinseq && cd 035_prinseq && cp ../03_bowtie2/*.nophix.fastq .'
        os.system(cmd)
        for input_file in (file_list_merged):
           current_path = cwd/'035_prinseq'
           subprocess.Popen('prinseq-lite.pl -fastq {0}.nophix.fastq -out_good {0} -lc_method dust -lc_threshold 7'.format(input_file).split(),cwd=current_path)
    def output(self):
        print("_35_prinseq: output")
        outputDict = {}
        for i, outFile in enumerate(file_list_merged):
           outputDict["output" + str(i)] = luigi.LocalTarget('035_prinseq/' + outFile + ".fastq")
        return outputDict


class _4_megahit(luigi.Task):
    task_namespace = 'metagenomes'

    def requires(self):
        print("_4_megahit: requires")
        return _35_prinseq()

    def run(self):
        print("_4_megahit: run")
        cmd = 'mkdir 04_megahit && cd 04_megahit '
        os.system(cmd)
        for input_file in (file_list_merged):
           current_path = cwd/'04_megahit'
           print(input_file)
           subprocess.Popen('echo \"035_prinseq/{0}.fastq_{0}.fastq\"'.format(input_file).split(), stdout=subprocess.PIPE,cwd=current_path)
           subprocess.Popen('cp ../035_prinseq/{0}.fastq {0}.fastq'.format(input_file).split(), stdout=subprocess.PIPE,cwd=current_path)
           subprocess.Popen('qsub -q l {0}run_megahit.sh -v FASTQ_FILE={1}.fastq,MEGAHIT_DIR={2}'.format(script_path,input_file,os.getcwd()+"/04_megahit").split(),cwd=current_path)
    def output(self):
        print("_4_megahit: output")
        outputDict = {}
        for i, outFile in enumerate(file_list_merged):
           outputDict["output" + str(i)] = luigi.LocalTarget('04_megahit/' + outFile + "assembled/final.contigs.fa")
        return outputDict


class _5_Prodigal(luigi.Task):
    task_namespace = 'metagenomes'

    def requires(self):
        print("_5_Prodigal: requires")
        return _4_megahit()

    def run(self):
        print("_5_Prodigal: run")
        current_path = cwd/'05_Prodigal'
        current_path.mkdir()
        for outFile in file_list_merged:
           print(outFile)
           print('cp ../04_megahit/{0}assembled/final.contigs.fa ./{0}'.format(outFile))
           print('prodigal -d {0}.fna -a {0}.faa -i {0} -p meta -o {0}.genes -q'.format(outFile))           
           popen = subprocess.Popen('cp ../04_megahit/{0}assembled/final.contigs.fa ./{0}'.format(outFile).split(),cwd=current_path)
           popen.wait()
           popen = subprocess.Popen('prodigal -d {0}.fna -a {0}.faa -i {0} -p meta -o {0}.genes -q'.format(outFile).split(),cwd=current_path)
           popen.wait()
    def output(self):
        print("_5_Prodigal: output")
        outputDict = {}
        for i, outFile in enumerate(file_list_merged):
           outputDict["output" + str(i)] = luigi.LocalTarget('05_Prodigal/' + outFile + ".faa")
           outputDict["output" + str(i)] = luigi.LocalTarget('05_Prodigal/' + outFile + ".fna")
        return outputDict

class _6_eggnog_mapper(luigi.Task):
    task_namespace = 'metagenomes'
    def requires(self):
        print("_6_eggnog_mapper: requires")
        return _5_Prodigal()

    def run(self):
        print("_6_eggnog_mapper: run")
        p = pathlib.Path('06_eggnog-mapper')
        p.mkdir()
        workdir = cwd / '06_eggnog-mapper'
        for i, outFile in enumerate(file_list_merged):
           subprocess.Popen('cp ../05_Prodigal/{0}.fna {0}.fna'.format(outFile).split(),cwd=workdir)
           subprocess.Popen('qsub -q l {0}run_eggnog-mapper.sh -v EMAPPER_DIR={1},EMAPPER_PATH={2},FNA_FILE={3},OUTPUT_FILE={4} -l cpunum_job=30,elapstim_req=72:00:00,memsz_job=128gb'.format(script_path,str(workdir),eggnog_mapper_path,outFile + ".fna", outFile + ".emapper").split(),cwd=workdir)
    def output(self):
        print("_6_eggnog_mapper: output")
        outputDict = {}
        for i, outFile in enumerate(file_list_merged):
           outputDict["output" + str(i)] = luigi.LocalTarget('06_eggnog-mapper/' + outFile + ".emapper")
        return outputDict





if __name__ == '__main__':
    luigi.run(['metagenomes._6_eggnog_mapper', '--workers', '1', '--local-scheduler'])
