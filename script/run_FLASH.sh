#!/bin/bash

for file in `ls *val_1.fq`; do
    flash --max-overlap 300 -o ${file/_1_val_1*/}  ${file} ${file/1_val_1/2_val_2} 2>&1 | tee ${file}_flash.log
done



