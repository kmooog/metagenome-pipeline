#!/bin/bash
for file in `ls *.fa`; do
    prodigal -d ${file/.fa/.fna} -a ${file/.fa/.faa} -i ${file} -p meta -o ${file/.fa//}.genes -q

done



