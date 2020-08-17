#!/bin/sh
#$ -cwd
#$ -N correlation
module load singularity
singularity exec /home/kumay/test_container/scipy-notebook.img python ~/metagenome-pipeline/script/python/calculateCorrelation.py
