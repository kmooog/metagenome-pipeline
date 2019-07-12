#!/bin/sh
#$ -cwd
#$ -N merge
module load singularity
singularity exec  /usr/local/biotools/p/phylopandas:0.1.3--py36_0  python  ~/metagenome-pipeline/script/python/merge_profile.py
