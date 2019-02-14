#!/bin/sh
cd ${MEGAHIT_DIR} 
megahit -r ${FASTQ_FILE}.nophix.fastq -o ${FASTQ_FILE/.fastq/assembled}
echo "MEGAHIT_DIR:$MEGAHIT_DIR"
echo "megahit -r ${FASTQ_FILE}.nophix.fastq -o ${FASTQ_FILE/.fastq/assembled}"


