cwlVersion: v1.0
class: CommandLineTool
baseCommand: prinseq-lite.pl
inputs:
  input:
    type: File
    inputBinding:
      position: 1
      prefix: -fastq
  output:
    type: string
    inputBinding:
      position: 2
      prefix: -out_good
  lc_method:
    type: string
    inputBinding:
      position: 3
      prefix: -lc_method
      
  lc_threshold:
    type: string
    inputBinding:
      position: 4
      prefix: -lc_threshold
      
outputs:
  prinseq_out:
    type: File
    outputBinding:
      glob: prinseq_out.fastq


