#!/bin/sh
#$ -cwd
#$ -N meta_p
module load singularity
singularity exec /home/kumay/test_container/metagenome-pipeline-latest.img cwltool /root/metagenome-pipeline/script/cwl/preprocessing_single.cwl --file1 ../${1}.fq.gz --phix /root/metagenome-pipeline/util-data/phix
