#!/bin/sh

for path in `find ../04_megahit/*nophixassembled -maxdepth 0 -type d`; do
    cp ${path}/final.contigs.fa ./${path/.*\//}.fa
    prodigal -d ${path/.*\//}.fna -a ${path/.*\//}.faa -i ${path/.*\//}.fa -p meta -o ${path/.*\//}.genes
done



