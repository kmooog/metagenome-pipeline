#!/bin/sh
cd ${EMAPPER_DIR} 
python2 ${EMAPPER_PATH} -i ${FNA_FILE} --output ${OUTPUT_FILE} -m diamond --usemem --cpu 40


