#!/bin/bash

cd ${2} 
echo "output is ${1/.fastq/_assembled}"
megahit -r ${1} -o ${1/.fastq/_assembled}


