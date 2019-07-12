#!/bin/sh
#$ -cwd
#$ -N hit_with_len
module load singularity
singularity exec /usr/local/biotools/b/biopython\:1.70--np112py36_1 python3  ~/metagenome-pipeline/script/python/hit_seq_with_length.py
