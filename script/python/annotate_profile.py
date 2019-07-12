import sys

eggnog_dict = {}
seed_dict = {}
COG_dict = {}
for a in open("/lustre7/home/kumay/metagenome_data/clusterd_genes/eggnog-mapper/chunks/emapper_output.emapper.annotations"):
   eggnog_dict[a.split("\t")[0]] = a.strip()
   seed_dict[a.split("\t")[20]] = 0
   cog_dict[a.split("\t")[21]] = 0

