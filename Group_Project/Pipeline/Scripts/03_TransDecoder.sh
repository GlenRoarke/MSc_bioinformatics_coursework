#!/bin/bash

### RUN TRANSDECODER ###
for i in *.fas
do 
    # Run TransDecoder on fasta files
    TransDecoder.LongOrfs -t $i

    # Predict likely coding regions
    TransDecoder.Predict -t $i
done

# Archive the cmds error output
for i in *.cmds; do mv $i Archive/ ;done

exit 0 