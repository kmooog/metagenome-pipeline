import sys

eggnog_dict = {}

for a in open("/lustre7/home/kumay/metagenome_data/clusterd_genes/eggnog-mapper/chunks/emapper_output.emapper.annotations"):
   eggnog_dict[a.split("\t")[0]] = a.strip()

count_dict = {}

for i in range (723,956):
   count_dict[i] = {}
   sum_count = 0
   with open(str(i)+"/normalized_count") as norm:
      for a in norm:
         tmpid, tmpcount = (a.split(",")[0],double(a.split(",")[1].strip()))
         sum_count += tmpcount
         count_dict[i][tmpid] = tmpcount
      for a in count_dict[i]:
         count_dict[a] = count_dict[a]/sum_count
out = open("emapper_profile","w")
for a in eggnog_dict:
   out.write(a)
   for i in range (723,956):
      out.write(count_dict[a])
      
       



         
  

