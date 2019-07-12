#!/bin/sh
#$ -cwd
#$ -N mapping
module load singularity 
singularity exec /usr/local/biotools/b/bowtie2:2.3.3.1--py36pl5.22.0_0 bowtie2 -x /home/kumay/metagenome_data/mapping/DOMdb -U prinseq_out.fastq -S mapped.sam

