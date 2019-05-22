#!/bin/sh
#$ -cwd
#$ -N meta_assemble
module load singularity
singularity exec /usr/local/biotools/m/megahit\:1.1.2--py36_0 megahit --mem-flag 0 --memory 0.5 -r all.fq -o all_assembled 

