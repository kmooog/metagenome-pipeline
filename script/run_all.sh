#!/bin/sh

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



