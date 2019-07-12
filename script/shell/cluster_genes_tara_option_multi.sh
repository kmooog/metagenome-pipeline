#!/bin/sh  
#$ -cwd      
#$ -N cdhit   

/home/kumay/software/cd-hit-v4.8.1-2019-0228/cd-hit-est -i /home/kumay/metagenome_data/clusterd_genes/clusterd_over500_over100_with_TARA.fa -o /home/kumay/metagenome_data/clusterd_genes/tara_with_jam_clustered_together -c 0.95 -T 20 -M 256000 -G 0 -aS 0.9 -g 1 -r 1 -d 0 
