cwlVersion: v1.0
class: CommandLineTool
baseCommand: trim_galore
arguments: ["--dont_gzip"]
inputs:
  file1:
    type: File
    inputBinding:
      position: 1
outputs:
  tg_out1:
    type: File
    outputBinding:
      glob: '*.fq'
