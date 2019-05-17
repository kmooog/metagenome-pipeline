# submit job
import subprocess
import os
import pathlib
import sys
import glob
args = sys.argv
cwd = pathlib.Path.cwd()
script_path = "/root/metagenome-pipeline/script/"
for i in range(int(args[1]),int(args[2])+1):
   print(i)
   i = str(i).zfill(3)
   workdir = cwd/str(i)
   workdir.mkdir()
   workdir = str(workdir)
   cmd = "cp ../{0}_1.fq.gz .".format(str(i))
   popen = subprocess.Popen(cmd.split(),cwd=workdir)
   cmd = "cp ../{0}_2.fq.gz .".format(str(i))
   popen = subprocess.Popen(cmd.split(),cwd=workdir)
   popen.wait()
   cmd = "python3 {0}metagenome-luigi.py {1} {2}".format(script_path,i,str(workdir))
   #cmd = "qsub /work/G10800/kumay/metagenome-pipeline/script/qsub_luigi.sh -q l -l cpunum_job=30,elapstim_req=72:00:00,memsz_job=128gb -v SAMPLE={0},WORKDIR={1}".format(i,str(workdir))
   popen = subprocess.Popen(cmd.split(),cwd=workdir)
   popen.wait()






