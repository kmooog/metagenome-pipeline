#!/bin/sh
#$ -cwd
#$ -N meta_p
for i in `seq -f %03g 723 849`
do
  rm ${i}_1.fq.gz  ${i}_2.fq.gz 
done
