#!/bin/bash

### SUMMARY OF RAW DATA: number of sequences and number of sequences with invalid '-' characters ###

# Create file and add header for the number of sequences
touch Raw_data_summary.txt | echo "Number of sequences per file" > Raw_data_summary.txt

# Count the number of sequences in fas files
grep -c "^>" *.fas >> Raw_data_summary.txt
echo "" >> Raw_data_summary.txt

# Add header for number of sequences with invalid '-' characters
echo "Sequences containing '-'" >> Raw_data_summary.txt

# Count the number of invalid dash characters
for f in *.fas; do echo $f; grep -o "-" $f | wc -l; done >> Raw_data_summary.txt

# Rename analysis file with datetime to prevent overwriting
mv Raw_data_summary.txt Raw_data_summary$(date +%d-%m-%Y_%H%M%S).txt

exit 0
