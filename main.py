from Bio import SeqIO

# the following program will extract individual fasta sequences and display a couple of its attibutes

def main():
    try:
        # getting the file
        in_file = list(SeqIO.parse("files/var.fasta"), "fasta")

    except Exception as e:
        print("Something went wrong: ", e)

main()