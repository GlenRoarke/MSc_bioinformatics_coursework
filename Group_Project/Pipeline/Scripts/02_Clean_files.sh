#!/bin/bash

# Remove dash characters '-' and replace with N for unspecified nucleotide
mkdir -p Archive/

for i in *.fas
do 
    # Find and replace '-' with 'N'
    sed '/^>/ s/-/_/g;/^>/! s/-/N/g' "$i" > "Final_$i"
    # Move raw, un-edited data into an Archive folder
    mv $i Archive/ 
done

exit 0 