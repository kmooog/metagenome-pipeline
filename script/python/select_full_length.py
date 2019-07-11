import sys 

fasta = sys.argv[1]
outfile = open("over_100.fa","w")
index = ""
seq = ""
for fasta_line in open (fasta):
   fasta_line = fasta_line.strip()
   if fasta_line[0] == ">" and index == "":
      index = fasta_line
   elif fasta_line[0] == ">":
      if len(seq) > 99:
         outfile.write(">" + index + "\n")
         outfile.write(seq + "\n")
         seq = ""
   else:
      seq = seq + fasta_line


      
