#!/bin/sh
#$ -cwd
#$ -N emapper
/home/kumay/software/eggnog-mapper/emapper.py --annotate_hits_table input.emapper.seed_orthologs --no_file_comments -o output_file --cpu 20 

