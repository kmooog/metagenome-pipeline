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
outputs: []
