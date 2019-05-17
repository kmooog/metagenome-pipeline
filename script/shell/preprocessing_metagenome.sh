#!/bin/sh
#$ -cwd
#$ -N meta_p
module load singularity
cd /home/kumay/metagenome_data 
mkdir ${1}
cd ${1}
singularity exec ../test_container/metagenome-pipeline-latest.img cwltool /root/metagenome-pipeline/script/cwl/preprocessing.cwl --file1 ../${1}_1.fq.gz --file2 ../${1}_2.fq.gz --phix /root/metagenome-pipeline/util-data/phix
