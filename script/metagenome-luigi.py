import luigi
import glob 
import subprocess
import os

files = "*.gz"
file_list = glob.glob(files)
file_list = [a.replace(".fastq.gz","") for a in file_list]

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
        #subprocess.run(cmd.split())
        os.system(cmd)
    def output(self):
        print("_2_Flash: output")
        outputDict = {}
        for i, outFile in enumerate(file_list):
           outputDict["output" + str(i)] = luigi.LocalTarget('01_TrimGalore/' + outFile + ".extendedFrags.fastq")
        return outputDict


if __name__ == '__main__':
    luigi.run(['metagenomes._2_Flash', '--workers', '1', '--local-scheduler'])
