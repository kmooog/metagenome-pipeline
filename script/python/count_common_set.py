import sys 

blast_result = open(sys.argv[1])
centroids = open(sys.argv[2])
tara = open("/home/kumay/tara_data/OM-RGC.fa")
tara_count = tara.read().count(">")
centroids_count = centroids.read().count(">")
common_set = 0
common_genes = []
for a in blast_result:
   if a.split(0) not in common_genes:
      common_genes.append(a.split(0))
      common_set += 1
output = open("common_set_counts", "w")
output.write("tara_count: "+ tara_count + "\n")
output.write("centroids_count: "+ centroids_count + "\n")
output.write("common_set_counts: "+ common_set + "\n")


