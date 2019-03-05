import sys
args = sys.argv

orthodict = {}
ortho_list = []
for i in range(int(args[1]),int(args[2])+1):
   print(i)
   tmpdict_for_ortho = {}
   for a in open ("abundance_{0}.txt".format(i)):
      if a.find("meanDepth") == -1:
         listtmp = a.strip().split("\t")
         ko = listtmp[0]
         rpkm = listtmp[3]
         tmpdict_for_ortho[ko] = rpkm
         if ko not in ortho_list:
            ortho_list.append(ko)
   orthodict[i] = tmpdict_for_ortho

ortho_list.sort()

with open("abundance.tsv", "w") as f:
   first_row = "ko\t"
   for i in range(int(args[1]),int(args[2])+1):
      first_row += str(i) + "\t"
   f.write(first_row.strip() + "\n")
   for a in ortho_list:
      row = a + "\t"
      for i in range(int(args[1]),int(args[2])+1):
         if a in orthodict[i]: 
            row += orthodict[i][a] + "\t"
         else:
            row += "0.0\t"
      f.write(row.strip() + "\n")


          
   
      







