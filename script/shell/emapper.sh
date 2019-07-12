#!/bin/sh
#$ -cwd
#$ -N emapper
/home/kumay/software/eggnog-mapper/emapper.py -m diamond --no_annot --no_file_comments --cpu 40 -i ${1} -o ${1}

