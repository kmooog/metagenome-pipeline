class: Workflow
cwlVersion: v1.0
id: preprocessing
label: PreProcessing
$namespaces:
  sbg: 'https://www.sevenbridges.com/'
inputs:
  - id: file1
    type: File
    'sbg:x': -565
    'sbg:y': 191.14759826660156
  - id: file2
    type: File
    'sbg:x': -576
    'sbg:y': -39
  - id: phix
    type: string
    'sbg:x': -186
    'sbg:y': -99
outputs:
  - id: prinseq_out
    outputSource:
      - prinseq/prinseq_out
    type: File
    'sbg:x': 368
    'sbg:y': -5
steps:
  - id: trimgalore
    in:
      - id: file1
        source: file1
      - id: file2
        source: file2
    out:
      - id: tg_out1
      - id: tg_out2
    run: ./trimgalore.cwl
    'sbg:x': -334.3984375
    'sbg:y': 112
  - id: flash
    in:
      - id: file1
        source: trimgalore/tg_out1
      - id: file2
        source: trimgalore/tg_out2
    out:
      - id: flash_out
    run: ./flash.cwl
    'sbg:x': -119
    'sbg:y': 113
  - id: bowtie2
    in:
      - id: bowtie_log
        default: bowtie_log
      - id: filename
        source: flash/flash_out
      - id: phix
        source: phix
      - id: unmapped
        default: unmapped.fq
    out:
      - id: flash_out
    run: ./bowtie2.cwl
    'sbg:x': 44
    'sbg:y': -1
  - id: prinseq
    in:
      - id: input
        source: bowtie2/flash_out
      - id: lc_method
        default: dust
      - id: lc_threshold
        default: '7'
      - id: output
        default: prinseq_out
    out:
      - id: prinseq_out
    run: ./prinseq.cwl
    'sbg:x': 202
    'sbg:y': -1
requirements: []
