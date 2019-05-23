class: Workflow
cwlVersion: v1.0
id: preprocessing
label: PreProcessing
$namespaces:
  sbg: 'https://www.sevenbridges.com/'
inputs:
  - id: phix
    type: string
    'sbg:x': -186
    'sbg:y': -99
  - id: file1
    type: File
    'sbg:x': -339
    'sbg:y': 26
outputs:
  - id: prinseq_out
    outputSource:
      - prinseq/prinseq_out
    type: File
    label: prinseq_out
    'sbg:x': 365
    'sbg:y': -4
steps:
  - id: bowtie2
    in:
      - id: bowtie_log
        default: bowtie_log
      - id: filename
        source: trimgalore_single/tg_out1
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
  - id: trimgalore_single
    in:
      - id: file1
        source: file1
    out:
      - id: tg_out1
    run: ./trimgalore_single.cwl
    'sbg:x': -170
    'sbg:y': 21
requirements: []
