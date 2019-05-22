for i in `seq -f %03g 723 955`
do
  mkdir ${i} 
  cd ${i}
  qsub /home/kumay/metagenome-pipeline/script/shell/preprocessing_metagenome.sh ${i}
  cd ..
done
