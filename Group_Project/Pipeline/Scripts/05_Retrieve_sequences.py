from Bio import SeqIO

### RETREIVEING SEQUENCES FUNCTION ###
def RETRIEVE_SEQ(Title):
    '''
RETRIEVE_SEQ function searches for sequences based on the ID inputted into the function. RETRIEVE_SEQUENCES then writes the ID and corresponding peptide sequence to a .fas file.
    Args:
        Title (string): A single or list of title(s)
        
        Returns:
            File called RETRIEVED_SEQUENCES.fas which contains all the sequences searched for
            Error message if the sequence is not found
            
        Examples:
        # Title accepted:
        >>> RETRIEVE_SEQ("title_that_exists")
        >>> with open("RETRIEVED_SEQUENCES.FAS") as f:
                lines = f.readlines()
            Found title_that_exists on line 1
            > title_name_found
            PEPTIDE SEQUENCE
        # Title not accepted:
        >>> RETRIEVE_SEQ("title_that_does_not_exist")
            X  Did not find title_that_does_not_exist
    '''
    LIST=[]
    TEMP = []

    # File where sequences will be stored - new sequences will be appended to this list everytime this script is run
    f = open("RETRIEVED_SEQS.fas", "a")

    # List of sequence IDs
    TITLE = []
    for record in SeqIO.parse("ALL_SEQS.txt", "fasta"):
        TITLE.append(record.id)
        
    # List of peptide sequences
    SEQUENCE = []
    for record in SeqIO.parse("ALL_SEQS.txt", "fasta"):
        SEQUENCE.append(record.seq)
    
    # Searching  for the sequence of interest
    if Title in TITLE:
        # Create the appropriate fasta format
        TEMP.append(">")
        TEMP.append(Title)
        TEMPJ=''.join(TEMP)
        POSITION = TITLE.index(Title)

        # State location of sequence in human-readable format
        print("/  Found", Title, "on line", POSITION+1)

        # Create lines to be written
        LIST.append(TEMPJ)
        SEQ_POS=SEQUENCE[POSITION]
        LIST.append(str(SEQ_POS))
        for item in LIST:
            f.writelines(item +'\n')
    else:
        # Sequence ID was not found in the file
        print(f"X  Did not find {Title}")
        
   
# Locate all the files which contain the renamed peptide sequences                
import os
ext = ('.pep.txt')
RENAMED_LIST=[]
for files in os.listdir():
    if files.endswith(ext):
        RENAMED_LIST.append(files)
        
        
# Create a .txt file that contains all the sequences and their unique names, only if it does not already exist 
CHECK_ALL_SEQS_EXISTS = []
for file in os.listdir():
    CHECK_ALL_SEQS_EXISTS.append(file)
    
# RETRIEVE_SEQS function will be able to select sequences from one location
if "ALL_SEQS.txt" not in CHECK_ALL_SEQS_EXISTS:
    print("Creating file of all peptides")
    with open ("ALL_SEQS.txt", "a") as outfile:
        for file_name in RENAMED_LIST:
            with open(file_name) as initial_file:
                for line in initial_file:
                    outfile.write(line)
                outfile.write("\n")
                

# Can input a list to retrieve multiple sequences at once, or copy and paste a list of sequences when required: TCep11a06_q1k_Gene_2377 TCep11d12_q1k_Gene_2425 TCep11e09_q1k_Gene_2435 NONAME_q1k_Gene_1234          
input_seq = list(map(str, input("Please input the name(s) of sequence(s), seperated by a space:").split()))

for name in input_seq:
    print(f"Searching for {name}")
    RETRIEVE_SEQ(f"{name}")