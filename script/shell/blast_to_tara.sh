#!/bin/sh
#$ -cwd
#$ -N blast_to_tara
for i in `seq 0 to 9`
do
  echo "start blast search to OM-RGC_${1}.fa"
  /home/kumay/software/ncbi-blast-2.9.0+/bin/blastn -query ${1} -db /home/kumay/tara_data/OM-RGC/OM-RGC_${i}.fa -outfmt 6 -max_target_seqs 1 -perc_identity 0.95 >> blast_to_tara.tsv        
done


 
