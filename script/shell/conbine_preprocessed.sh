#!/bin/sh
#$ -cwd
#$ -N meta_p
for i in `seq -f %03g 723 955`
do
  cat ${i}/prinseq_out.fastq >> all.fq
done
