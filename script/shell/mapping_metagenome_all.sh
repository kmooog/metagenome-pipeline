for i in `seq -f %03g 723 955`
do
  cd ${i}
  qsub -l s_vmem=256G -l mem_req=256G -l medium /home/kumay/metagenome-pipeline/script/shell/mapping_metagenome.sh
  cd ..
done
