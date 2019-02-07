#!/bin/sh

for file in `ls *_R1_*.fastq.gz`; do
    trim_galore --paired  ${file} ${file/_R1_/_R2_}
done



