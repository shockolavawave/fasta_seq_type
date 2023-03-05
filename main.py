from Bio import SeqIO


# the following program will extract individual fasta sequences and display a couple of its attributes
def print_seq(in_file):
    print("there are", len(in_file), "sequence(s) in the file\n\n")

    # primary loop for extracting all possible fasta sequences
    for ea in in_file:
        # following are operations made on each
        ea.seq = ea.seq.upper()  # setting the sequence to upper case

        print(ea.id, "          len:", len(ea), "       type:", get_seq_type(ea))
        print(fasta70(ea.seq), "\n\n")


def main():
    try:
        # getting the file
        in_file = list(SeqIO.parse("files/var.fasta", "fasta"))

        print_seq(in_file)

    except Exception as e:
        print("Something went wrong: ", e)


main()
