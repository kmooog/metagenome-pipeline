import sys

#eggnog_dict = {}
#seed_dict = {}
#COG_dict = {}
#for a in open("/lustre7/home/kumay/metagenome_data/clusterd_genes/eggnog-mapper/chunks/emapper_output.emapper.annotations"):
   #eggnog_dict[a.split("\t")[0]] = a.strip()
   #seed_dict[a.split("\t")[0]] = a.strip()
   #cog_dict[a.split("\t")[0]] = a.strip()

count_dict = {}

for i in range (723,956):
   count_dict = {}
   sum_count = 0
   with open(str(i)+"/normalized_count") as norm:
      tmpfile = open("mapping/tmp/normalized_by_sum_"+str(i), "w")
      for a in norm:
         tmpid, tmpcount = (a.split(",")[0],float(a.split(",")[1].strip()))
         sum_count += tmpcount
         count_dict[tmpid] = tmpcount
      for a in count_dict:
         tmpfile.write(a + "," + str(count_dict[a])+ "\n")
      tmpfile.close()
"""
out = open("mapping/mapped_profile","w")
out.write("sample")
for i in range (723,956):
   out.write(","+str(i))
out.write("\n")
for a in eggnog_dict:
   out.write(a)
   for i in range (723,956):
      if a in count_dict[i]:
         out.write(","+str(count_dict[i][a]))
      else:
         out.write(",0")
   out.write("\n")
out.close()
"""      
    





