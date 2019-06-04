import subprocess
import os
import pathlib
import sys
import glob

cwd = pathlib.Path.cwd()
scriptpath = "/home/kumay/metagenome-pipeline/script/shell" 

for i,a in enumerate(open("tara_data.txt")):
   id_list_file = open("id_num.txt","w")
   if (i > 0):
      num = str(i).zfill(3) # analysis ID
      workdir = cwd/num # working and output dir
      workdir.mkdir()
      tmplist = a.split("\t")
      sample_id = tmplist[2] # secondary_sample_accession
      id_list_file.write(num + "\t" + sample_id)
      print("start - " + num + " " + sample_id)
      single_or_pair = tmplist[8] # library_layout
      ftp = tmplist[9] # fastq_ftp 
      if (single_or_pair == "SINGLE"):
         cmd = "wget -P {0} -O {0}.fq.gz {1}".format(num,ftp)
         popen = subprocess.Popen(cmd.split(),cwd=workdir)
         popen.wait()
         cmd = "qsub {0}/preprocessing_metagenome_single.sh {1}".format(scriptpath,num)
         popen = subprocess.Popen(cmd.split(),cwd=workdir)
         popen.wait()
         # cmd = "rm {0}.fq.gz".format(num)
         # popen = subprocess.Popen(cmd.split(),cwd=workdir)
      elif (single_or_pair == "PAIRED"):
         cmd = "wget -P {0} -O {0}_1.fq.gz {1}".format(num,ftp.split(";")[0])                      
         popen = subprocess.Popen(cmd.split(),cwd=workdir)
         popen.wait()
         cmd = "wget -P {0} -O {0}_2.fq.gz {1}".format(num,ftp.split(";")[1])                     
         popen = subprocess.Popen(cmd.split(),cwd=workdir)
         popen.wait()
         cmd = "qsub {0}/preprocessing_metagenome.sh {1}".format(scriptpath,num)
         popen = subprocess.Popen(cmd.split(),cwd=workdir)
         popen.wait()
         # cmd = "rm {0}.fq.gz".format(num)
         # popen = subprocess.Popen(cmd.split(),cwd=workdir)
         






