cwlVersion: v1.0
class: Workflow
inputs:
  target_file:
    type: File
outputs:
  preprocessed:
    type: File
    outputSource: preprocessed
steps:
  grep:
    run: grep.cwl
    in:
      pattern: grep_pattern
      file_to_search: target_file
    out: [results]
  wc:
    run: wc.cwl
    in:
      file: grep/results
    out: [counts]

