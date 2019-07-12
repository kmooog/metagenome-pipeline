import sys 
from Bio import SeqIO
sam = "mapped.sam"
fasta = "/home/kumay/metagenome_data/mapping/clusterd_over500_over100"

id_and_length = {}
outdict = {} 
with open(fasta, "r") as handle:
   for record in SeqIO.parse(handle, "fasta"):
      id_and_length[str(record.id)] = len(str(record.seq))

with open(sam) as sam_file:
   for a in sam_file:
      if a[0] != "@":
         tmplist = a.strip().split()
         if tmplist[2] != "*":
            if tmplist[2] not in outdict:
               outdict[tmplist[2]] = 1.0 / id_and_length[tmplist[2]] 
            else:
               outdict[tmplist[2]] += 1.0 / id_and_length[tmplist[2]]

out = open("normalized_count", "w")
for a in outdict:
   out.write(a + "," + str(outdict[a]) + "\n")
   


      
