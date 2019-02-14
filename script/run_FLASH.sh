#!/bin/sh

for file in `ls *R1_001_val_1.fq.gz`; do
    flash --max-overlap 300 -o ${file/_val*/}  ${file} ${file/R1_001_val_1/R2_001_val_2} 2>&1 | tee ${file}_flash.log
done



