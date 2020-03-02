cwlVersion: v1.0
class: CommandLineTool
baseCommand: flash
arguments: ['-o', 'flash']
inputs:
  file1:
    type: File
    inputBinding:
      position: 5
  file2:
    type: File
    inputBinding:
      position: 6
outputs:
  flash_out:
    type: File
    outputBinding:
      glob: flash.extendedFrags.fastq
