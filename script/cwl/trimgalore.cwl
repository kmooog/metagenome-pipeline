cwlVersion: v1.0
class: CommandLineTool
baseCommand: trim_galore
arguments: ["--dont_gzip"]
inputs:
  file1:
    type: File
    inputBinding:
      position: 1
      prefix: --paired
  file2:
    type: File
    inputBinding:
      position: 2
outputs:
  tg_out1:
    type: File
    outputBinding:
      glob: '*_1_val_1.fq'
  tg_out2:
    type: File
    outputBinding:
      glob: '*_2_val_2.fq'
 
