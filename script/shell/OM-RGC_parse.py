
o1 = open ("OM-RGC.fa","w")
o2 = open ("OM-RGC.tsv","w")

for a in open ("OM-RGC_seq.release.tsv"):
    tmplist = a.strip().split("\t")
    tsv_out = '\t'.join([str(i) for i in tmplist[:-1]]) + "\n"
    o2.write(tsv_out)
    if (tmplist[0] != "OM-RGC_ID"):
        o1.write(">" + tmplist[0] + "\n")
        o1.write(tmplist[-1] + "\n")
