#!/bin/sh

for file in `ls *extendedFrags.fastq`; do
     bowtie2 -x /work/G10800/kumay/metagenome-pipeline/util-data/phix ${file} --un ./${file/extendedFrags.fastq/nophix.fastq} -S ./${file/extendedFrags.fastq/log}
done



