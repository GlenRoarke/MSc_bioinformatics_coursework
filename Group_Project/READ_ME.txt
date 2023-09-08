#############################
## WELCOME TO THE PIPELINE ##
#############################

Here are all the files included in the Archive:
- Rmarkdown source file and html containing the manual and report
- A folder named Pipeline, containing all the data used, scripts run and outputs collected, for all 6 data sets (details below)

How to start:
1. Open the html which contains information on how to run the pipeline (you may need to run the Rmarkdown first)
2. Copy and paste the folder and its contents into Ubuntu - the data is already in the Data folder within Pipeline
3. Follow the instructions in the Rmarkdown manual to run each scripts

Scripts included in the folder Scripts within Pipeline:
- 00_Unzip_file (bash)
	# Unzips zipped files ready for downstream processing. 
	# Called by 01_Raw_data_summary and so does not need to be run manually
- 01_Raw_data_summary (bash)
	# Calculates some statistics based on the raw data inputted into the pipeline
- 02_Clean_files (bash)
	# Prepares the raw data for TransDecoder
	# Note that this loops through all data provided to the pipeline at once
- 03_TransDecoder (bash)
	# Runs TransDecoder (.Predict and .LongOrfs) on the cleaned files
	# Note that this loops through all data provided to the pipeline at once
- 04_Rename_sequences (python3)
	# Renames the sequences of the TransDecoder output files
	# Note that this loops through all data provided to the pipeline at once
- 05_Retrieve_sequences (python3)
	# Allows user input to retrieve sequences from any file that has been renamed based on unique ID

The final output of interest will be a file named RETRIEVED_SEQS.fas, which is in a usable fasta format
for further analysis (compatible with BLAST and other protein databases).