import luigi
import time
import subprocess

class _1_TrimGalore(luigi.Task):
    task_namespace = 'metagenomes'

    def run(self):
        print("_1_TrimGalore: run")
        cmd = "mkdir 01_TrimGalore && cd 01_TrimGalore && cp ../*.fastq.gz . && sh run_TrimGalore.sh"
        subprocess.call(cmd.split())

    def output(self):
        print("Task1: output")
        cmd = "ls *_val_*"  
        fileList = subprocess.check_output(cmd.split()).split()
        outputDict = {}
        for i, outFile in enumerate(fileList):
            outputDict["output" + str(i)] = luigi.LocalTarget(outFile)
        return outputDict


class _2_Flash(luigi.Task):
    task_namespace = 'tasks'

    def requires(self):
        print("_2_Flash: requires")
        return _1_TrimGalore()

    def run(self):
        print("_2_Flash: run")
        cmd = "mkdir 02_Flash && cd 02_Flash && cp ../01_TrimGalore/*_val_*.fq.gz . && sh run_FLASH.sh"
        subprocess.call(cmd.split())
        
    def output(self):
        print("_2_Flash: output")
        cmd = "ls *extendedFrags.fastq"
        fileList = subprocess.check_output(cmd.split()).split()
        outputDict = {}
        for i, outFile in enumerate(fileList):
           outputDict["output" + str(i)] = luigi.LocalTarget(outFile)
        return outputDict


if __name__ == '__main__':
    luigi.run(['tasks._2_Flash', '--workers', '1', '--local-scheduler'])
