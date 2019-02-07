#!/bin/sh

for file in `ls *extendedFrags.fastq`; do
     ../../bowtie2-2.3.4.3-linux-x86_64/bowtie2 -x ../../util-data/phix ${file} --un ./${file/extendedFrags.fastq/nophix.fastq} -S ./${file/extendedFrags.fastq/log}
done



