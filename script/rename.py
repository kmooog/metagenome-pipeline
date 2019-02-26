import glob
import os
import pathlib
files = glob.glob("./data/*")
print(files)
count=0
cwd = pathlib.Path.cwd()

os.system('mkdir renamed_data')
for a in files:

   # macrogen
   if a.find("_1.fastq.gz") != -1:
      count += 1
      countstr=str(count)
      print('cp {0} renamed_data/{1}'.format(a,countstr+".1.fq.gz"))
      os.system('cp {0} renamed_data/{1}'.format(a,countstr+".1.fq.gz"))
      os.system('cp {0} renamed_data/{1}'.format(a.replace("_1.fastq.gz","_2.fastq.gz")))
      os.system('echo {0},{1} >> RENAMELIST'.format(a.replace("_1.fastq.gz","").replace("./","")))

   if a.find("R1_001.fastq.gz") != -1:
      count += 1
      countstr=str(count)
      print('cp {0} renamed_data/{1}'.format(a,countstr+".1.fq.gz"))
      os.system('cp {0} renamed_data/{1}'.format(a,countstr+".1.fq.gz"))
      os.system('cp {0} renamed_data/{1}'.format(a.replace("R1_001.fastq.gz","R2_001.fastq.gz"),countstr+".2.fq.gz"))
      os.system('echo {0},{1} >> RENAMELIST'.format(a.replace("R1_001.fastq.gz","").replace("./",""),countstr+".1.fq.gz"))


