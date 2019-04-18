#!/bin/bash
cd $1 
trim_galore --paired  ${2}_1.fq.gz ${2}_2.fq.gz --dont_gzip



