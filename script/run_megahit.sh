#!/bin/sh
cd /work/G10800/kumay/01_make_analysis_workflow/04_megahit
megahit -r ${FASTQ_FILE} -o ${FASTQ_FILE/.fastq/assembled}



