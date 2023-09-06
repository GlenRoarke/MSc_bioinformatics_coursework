   
srun --account=BISC029044 --partition=teach_cpu --nodes=1 --ntasks-per-node=16 --time=01:00:00 --pty bash -i

   
# load in fastqc
  module add apps/fastqc/0.11.9


#load fastqc
module add apps/fastqc/0.11.9

#MEGAHIT
module add lang/python/anaconda/3.8-2021-TW
/sw/lang/anaconda.3.8-2021-TW/bin/megahit -1 coursework2023_R1_trimmed.fastq -2 coursework2023_R2_trimmed.fastq -o assembly_all_contigs

#compute the basic assembly statistics
#quast 
module add lang/python/anaconda/3.8-2021-TW
quast.py assembly_all_contigs/final.contigs.fa

#### Quast with a reference #####

#download reference genome 
wget --timestamping https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/008/000/775/GCF_008000775.1_ASM800077v1/GCF_008000775.1_ASM800077v1_genomic.fna.gz -P cp_s_genome/

# quast without alignment
module add lang/python/anaconda/3.8-2021-TW
quast.py final.contigs.fa -r cp_s_genome/GCF_008000775.1_ASM800077v1_genomic.fna.gz

## BWA
module load apps/bwa/0.7.17

module load apps/samtools/1.9

# Index the assembly file
bwa index final.contigs.fa

# Map the reads to the assembly
bwa mem final.contigs.fa coursework2023_R1.fastq coursework2023_R2.fastq -o cp_s_align.sam

# Convert the SAM file to a BAM file
samtools view -S -b cp_s_align.sam > cps_align.bam

# Sort and index the BAM file
samtools sort cps_align.bam -o sort_cps_align.bam
samtools index sort_cps_align.bam

# run WITH alignment
quast.py final.contigs.fa -r cp_s_genome/GCF_008000775.1_ASM800077v1_genomic.fna.gz --bam sort_cps_align.bam
samtools depth sort_cps_align.bam | awk '{ sum += $3 } END { print sum / NR }' | awk '{ print $0 * 4427796 }'







### new version 

samtools depth sort_cps_align.bam | awk -v genome_size= 4427796 '{sum += $3} END {print sum/(genome_size)}'
samtools depth sort_cps_align.bam | awk -v genome_size=4427796 '{sum += $3} END {print sum/genome_size}'





# average coverage (for covered bases)
samtools depth  sort_cps_align.bam  |  awk '{sum+=$3} END { print "Average = ",sum/samtools view -H sort_cps_align.bam | grep -P '^@SQ' | cut -f 3 -d ':' | awk '{sum+=$1} END {print sum}'}'


samtools depth <sorted.bam> | awk -v genome_size=<genome_size> '{sum += $3} END {print sum/(genome_size)}'


samtools depth mapping.sorted.bam | awk '{sum+=$3} END {print sum/NR}'
samtools depth sort_cps_align.bam | awk '{sum+=$3} END {print sum/NR}'
samtools depth  sort_cps_align.bam  |  awk '{sum+=$3} END { print "Average = ",sum/NR}'


samtools depth  sort_cps_align.bam  |  awk '{sum+=$3} END { print "Average = ",sum/NR}'
samtools depth sort_cps_align.bam  |  awk '{sum+=$3; sumsq+=$3*$3} END { print "Average = ",sum/NR; print "Stdev = ",sqrt(sumsq/NR - (sum/NR)**2)}'





samtools depth sort_cps_align.bam |  awk '{sum+=$3} END { print "Average = ",sum/NR}'

quast.py final.contigs.fa -r cp_s_genome/GCF_008000775.1_ASM800tr7v1_genomic.fna.gz -t 15 -bam cor
ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/001/696/305/GCF_001696305.1_UCN72.1



#BUSCO for completeness 
module add lang/python/anaconda/3.8-2021-TW
module add lang/perl/5.30.0-bioperl-TW
module add apps/blast/2.2.31+
source activate busco-5.0.0

/sw/lang/anaconda.3.8-2021-TW/bin/megahit
busco --in final.contigs.fa --mode genome  --auto-lineage-prok --out busco_results

#Coverage calculation
megahit_toolkit contig2fasta -in <assembly_file> -out <output_file>
/sw/lang/anaconda.3.8-2021-TW/bin/megahit_toolkit contig2fastg -in final.contigs.fa -out megahit_assmbly.fa
/sw/lang/anaconda.3.8-2021-TW/bin/megahit_core contig2fasta -in final.contigs.fa -out megahit_assmbly.fa

seqtk fqchk <read_file> | awk '{s+=$2} END {print s}'

awk '{if (substr($1,1,1)==">") {if (seq!="") {print name "\t" length(seq)} name=$0;seq=""} else seq=seq $0} END {print name "\t" length(seq)}' <contigs_file> > <contigs_lengths_file>

#prokka
module add lang/python/anaconda/3.8-2021-TW
module add lang/perl/5.30.0-bioperl-TW
module add apps/blast/2.2.31+

#Bacteria
prokka --kingdom Bacteria 
prokka --outdir mydir --prefix mygenome contigs.fa
prokka --kingdom bacteria --outdir bact_prokka --prefix bact_ final.contigs.fa
prokka --kingdom Archaea --outdir archaea_prokka final.contigs.fa


