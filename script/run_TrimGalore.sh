#!/bin/sh
cd ${TRIMGALORE_DIR}
trim_galore --paired  ${FASTQ_FILE} ${FASTQ_FILE/_1/_2}



