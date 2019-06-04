#!/bin/sh
#$ -cwd
#$ -N meta_assemble
module load singularity
singularity exec /usr/local/biotools/m/megahit\:1.1.2--py36_0 megahit -r all.fq -o all_assembled 

