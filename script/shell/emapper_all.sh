for i in `seq 1 45`
do
  echo ${i} 
  qsub -l s_vmem=256G -l mem_req=256G -l medium /home/kumay/metagenome-pipeline/script/shell/emapper.sh clusterd_over500_over100_chunk_${i}.faa
done
