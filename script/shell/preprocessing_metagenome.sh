#!/bin/sh
#$ -cwd
#$ -N meta_p
module load singularity
singularity exec /home/kumay/test_container/metagenome-pipeline-latest.img cwltool /root/metagenome-pipeline/script/cwl/preprocessing.cwl --file1 ../${1}_1.fq.gz --file2 ../${1}_2.fq.gz --phix /root/metagenome-pipeline/util-data/phix
