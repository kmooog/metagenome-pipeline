import glob
import os
import pathlib
files = glob.glob("./*")
print(files)
count=0
cwd = pathlib.Path.cwd()


for a in files:

   # macrogen
   if a.find("_1.fastq.gz") != -1:
      count += 1
      countstr=str(count)
      os.system('echo {0} >> FILE'.format(countstr))
      os.system('mkdir {0} '.format(countstr))
      os.system('cp {0} ./{0}/{1}'.format(a,countstr+".1.fq.gz"))
      os.system('cp {0} ./{0}/{1}'.format(a.replace("_1.fastq.gz","_2.fastq.gz"),countstr+".2.fq.gz"))
      os.system('echo {0},{1} >> RENAMELIST'.format(a.replace("_1.fastq.gz","").replace("./",""),countstr+".1.fq.gz"))

   if a.find("R1_001.fastq.gz") != -1:
      count += 1
      countstr=str(count)
      os.system('echo {0} >> FILE'.format(countstr))
      os.system('mkdir {0} '.format(countstr))
      os.system('cp {0} ./{2}/{1}'.format(a,countstr+".1.fq.gz",countstr))
      os.system('cp {0} ./{2}/{1}'.format(a.replace("R1_001.fastq.gz","R2_001.fastq.gz"),countstr+".2.fq.gz",countstr))
      os.system('echo {0},{1} >> RENAMELIST'.format(a.replace("R1_001.fastq.gz","").replace("./",""),countstr+".1.fq.gz"))


