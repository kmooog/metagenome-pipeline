for i in `seq -f %03g 723 955`
do
  echo "${i}_1.fq.gz ${i}_2.fq.gz"
done
