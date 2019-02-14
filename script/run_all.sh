#!/bin/sh

# our server only allow 80 qsub for one user

# 01_TrimGalore
mkdir 01_TrimGalore
cd 01_TrimGalore
cp ../*.fastq.gz .
sh run_TrimGalore.sh
cd ..

# 02_Flash

mkdir 02_Flash
cd 02_Flash
cp ../01_TrimGalore/*_val_*.fq.gz .
sh run_FLASH.sh
cd ..

# 03_bowtie2

mkdir 03_bowtie2
cd 03_bowtie2
cp ../02_Flash/*.extendedFrags.fastq .
sh run_bowtie2.sh
cd ..

# 04_megahit
mkdir 04_megahit
cd 04_megahit 
cp ../03_bowtie2/*.nophix.fastq .
for file in `ls *.nophix.fastq`; do
   export FASTQ_FILE=${file}
   qsub -q l /work/G10800/kumay/metagenome-pipeline/script/run_megahit.sh
   export FASTQ_FILE=""   
done
cd ..

# 05_Prodigal
cd 05_Prodigal
sh run_Prodigal.sh
cd ..

# 06_eggnog_mapper



