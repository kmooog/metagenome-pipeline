#!/bin/sh
cd $WORKDIR
echo "python /work/G10800/kumay/metagenome-pipeline/script/metagenome-luigi.py $SAMPLE $WORKDIR" 
python /work/G10800/kumay/metagenome-pipeline/script/metagenome-luigi.py $SAMPLE $WORKDIR
