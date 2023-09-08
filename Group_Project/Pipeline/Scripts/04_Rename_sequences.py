#!/usr/bin/env python3

### RENAMING SEQUENCES FUNCTION ###
def RENAME_SEQS(DATA_FILE):
    '''
RENAME_SEQS function takes a file, splices the original title and reconstructs a new and unique title for each sequence.
    Args:
        DATA_FILE (.pep): A file containing peptide sequences and the corresponding ID

        Returns:
        File called Renamed_DATA_FILE.pep.txt

        Examples:
        >>> RETRIEVE_SEQ("data_1.pep")
        >>> for files in os.listdir():
                if files.endswith(".pep.txt"):
                    print(files)
        Renamed_data_1.pep.txt
    '''
    with open(DATA_FILE) as SEQUENCE_DATA:
        BY_LINE = []
        # Create a file to write the renamed sequences to
        f = open(f'Renamed_{DATA_FILE}.txt', 'w')

        # Loop thorugh each line of the file and apply corrections
        for line in SEQUENCE_DATA:
            if line.startswith(">"):
                line_split=line.split(":")[2]

                # Create new title prefix from existing title information
                caps_data_set = (line_split.replace(line_split[1],line_split[1].upper())) # Get unique code
                line_removal_1=caps_data_set.replace(".", "_") # Remove special characters
                SEQ_NAME = line_removal_1.replace("-", "_")

                # Create Gene number suffix
                gene_info = line.split(":")[0] # Get Gene.n
                gene_removal_1 = gene_info.replace(".", "_") # Remove special characters
                GENE_NUMBER = gene_removal_1.replace(">","_")

                # Join Data information with Gene number sections to get the final title
                FINAL_TITLE = ">" + SEQ_NAME + GENE_NUMBER

                # Replace the line starting '>Gene.1...' with the new title
                TITLE_LINE=line.replace(line, FINAL_TITLE)
                BY_LINE.append(TITLE_LINE)
            else:
                PROTEIN = line.strip()
                BY_LINE.append(PROTEIN)

        f.write('\n'.join(BY_LINE))


### CODE TO RUN THE FUNCTION ###
import os
ext = ('.pep')
FILE_LIST=[] # A list containing all file names that will be analysed

# Loop through the directory containing the data, and append the file name to a list
for files in os.listdir():
    if files.endswith(ext):
        FILE_LIST.append(files)
    else:
        continue

# Loop thorugh the files and rename the sequences
if bool(FILE_LIST) == False:
    print("No files found for renaming.")
else:
    for files in FILE_LIST:
        RENAME_SEQS(files)
