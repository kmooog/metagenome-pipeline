for i in `seq -f %03g 723 833`
do
  mkdir ${i} 
  cd ${i}
  qsub -l s_vmem=256G -l mem_req=256G -l medium /home/kumay/metagenome-pipeline/script/shell/preprocessing_metagenome.sh ${i}
  cd ..
done
