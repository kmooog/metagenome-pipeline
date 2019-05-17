cwlVersion: v1.0
class: CommandLineTool
baseCommand: bowtie2
inputs:
  phix:
    type: string
    inputBinding:
      position: 1
      prefix: -x
  filename:
    type: File
    inputBinding:
      position: 2
      prefix: -q
  unmapped:
    type: string
    inputBinding:
      position: 3
      prefix: --un
      
  bowtie_log:
    type: string
    inputBinding:
      position: 4
      prefix: -S
      
outputs:
  flash_out:
    type: File
    outputBinding:
      glob: unmapped.fq
      
      

