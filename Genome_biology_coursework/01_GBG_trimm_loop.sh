#!/bin/bash
#SBATCH --job-name=trimmomatic
#SBATCH --output=trimmomatic_out
#SBATCH --error=trimmomatic_error
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --mem=10G
#SBATCH --time=0-01:00:00
#SBATCH --account=bisc029026

#move into your current directory – this will be named in the $SLURM_SUBMIT_DIR environment variable
cd $SLURM_SUBMIT_DIR

# arg1: number of threads
# to run: 
# chmod +x trim.sh
# <path>/trim.sh <number of threads>
# Example: ./trim.sh 40

for f in *_R1.fastq # for each sample

do
    n=${f%%_R1.fastq} # strip part of file name
    java -jar /sw/apps/Trimmomatic-0.39/trimmomatic-0.39.jar PE -threads $1 ${n}_R1.fastq  ${n}_R2.fastq \
    ${n}_R1_trimmed.fastq.gz ${n}_R1_unpaired.fastq.gz ${n}_R2_trimmed.fastq.gz \
    ${n}_R2_unpaired.fastq.gz \
    LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15

done








 
