#!/bin/bash
for file in `ls *extendedFrags.fastq`; do
     bowtie2 -x /root/metagenome-pipeline/util-data/phix ${file} --un ./${file/extendedFrags.fastq/nophix.fastq} -S ./${file/extendedFrags.fastq/log}
done



