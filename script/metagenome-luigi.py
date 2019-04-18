import luigi
import glob 
import subprocess
import os
import pathlib
from pathlib import Path
import sys
args = sys.argv

if len(args) != 3:
   print(args)
   print("usage: python metagenome-luigi.py FILE_NAME WORKING_DIR")
   print("please specify only one file name and working dir. if you have test_1.fq.gz and test_2.fq.gz, please give \"test\" as an argument.")
   sys.exit()
filename = args[1]

cwd = str(Path.cwd())
workind_dir = args[2]

script_path = "/root/metagenome-pipeline/script/"
eggnog_mapper_path = ""

class _1_TrimGalore(luigi.Task):
    task_namespace = 'metagenomes'

    def run(self):
        print("_1_TrimGalore: run")
        print('bash {0}run_TrimGalore.sh {1} {2}'.format(script_path,os.getcwd(),filename))
        popen = subprocess.Popen('sh {0}run_TrimGalore.sh {1} {2}'.format(script_path,workind_dir,filename).split(),cwd=cwd)
        popen.wait() 
    
    def output(self):
        print("Task1: output")
        outputDict = {}
        print("require: " + filename + "_1_val_1.fq")
        outputDict["output1"] = luigi.LocalTarget(filename + "_1_val_1.fq")
        outputDict["output2"] = luigi.LocalTarget(filename + "_2_val_2.fq")
        return outputDict

class _2_Flash(luigi.Task):
    task_namespace = 'metagenomes'
    def requires(self):
        print("_2_Flash: requires")
        return _1_TrimGalore()
    def run(self):
        print("_2_Flash: run")
        cmd = 'bash {0}run_FLASH.sh'.format(script_path)
        os.system(cmd)
    def output(self):
        print("_2_Flash: output")
        return luigi.LocalTarget(filename + ".extendedFrags.fastq")

class _3_bowtie2(luigi.Task):
    task_namespace = 'metagenomes'

    def requires(self):
        print("_3_bowtie2: requires")
        return _2_Flash()

    def run(self):
        print("_3_bowtie2: run")
        cmd = 'bash {0}run_bowtie2.sh'.format(script_path)
        os.system(cmd)
    def output(self):
        print("_3_bowtie2: output")
        return luigi.LocalTarget(filename + ".nophix.fastq") 

class _4_prinseq(luigi.Task):
    task_namespace = 'metagenomes'

    def requires(self):
        print("_4_prinseq: requires")
        return _3_bowtie2()

    def run(self):
        print("_4_prinseq: run")
        popen = subprocess.Popen('prinseq-lite.pl -fastq {0}.nophix.fastq -out_good {0}_prinseq -lc_method dust -lc_threshold 7'.format(filename).split(),cwd=cwd)
        popen.wait()
    def output(self):
        print("_4_prinseq: output")
        return luigi.LocalTarget(filename + "_prinseq.fastq") 

class _5_megahit(luigi.Task):
    task_namespace = 'metagenomes'

    def requires(self):
        print("_5_megahit: requires")
        return _4_prinseq()

    def run(self):
        print("_5_megahit: run")
        popen = subprocess.Popen('bash {0}run_megahit.sh {1} {2}'.format(script_path,filename + "_prinseq.fastq",workind_dir).split(),cwd=cwd)
        popen.wait()

    def output(self):
        print("_5_megahit: output")
        outputDict = {}
        return luigi.LocalTarget(filename + "_prinseq_assembled/final.contigs.fa")

class _6_Prodigal(luigi.Task):
    task_namespace = 'metagenomes'

    def requires(self):
        print("_6_Prodigal: requires")
        return _5_megahit()

    def run(self):
        print("_6_Prodigal: run")
        popen = subprocess.Popen('prodigal -d {0}_prodigal.fna -a {0}_prodigal.faa -i {0}_prinseq_assembled/final.contigs.fa -p meta -o {0}.genes -q'.format(filename).split(),cwd=cwd)
        popen.wait()
    def output(self):
        print("_6_Prodigal: output")
        return luigi.LocalTarget(filename + "_prodigal.faa") 

class _7_eggnog_mapper(luigi.Task):
    task_namespace = 'metagenomes'
    def requires(self):
        print("_7_eggnog_mapper: requires")
        return _6_Prodigal()

    def run(self):
        print("_7_eggnog_mapper: run")
        print('bash {0}run_eggnog-mapper.sh {1} {2} {3} {4}'.format(script_path,workind_dir,eggnog_mapper_path,filename + "_prodigal.faa", filename + ".emapper"))
        popen = subprocess.Popen('bash {0}run_eggnog-mapper.sh {1} {2} {3} {4}'.format(script_path,workind_dir,eggnog_mapper_path,filename + "_prodigal.faa", filename + ".emapper").split(),cwd=cwd)
        popen.wait()
    def output(self):
        print("_7_eggnog_mapper: output")
        return luigi.LocalTarget(filename + ".emapper") 

class _8_bwa(luigi.Task):
    task_namespace = 'metagenomes'
    
    def requires(self):
        print("_8_bwa: requires")
        return _7_eggnog_mapper()

    def run(self):
        print("_8_bwa: run")
    
    def output(self):
        print("_8_bwa: output")
        return luigi.LocalTarget(filename+"_bwa")

if __name__ == '__main__':
    luigi.run(['metagenomes._6_Prodigal', '--workers', '1', '--local-scheduler'])
