from Bio import SeqIO


# the following program will extract individual fasta sequences and display a couple of its attributes

def fasta70(seq):
    out_seq = ""
    try:
        for i in range(len(seq)):
            if i % 70 == 0 and i != 0:
                out_seq = out_seq + "\n"

            out_seq = out_seq + seq[i]

    except Exception as e:
        print("something went wrong", e)

    return out_seq


def is_dna(ea):
    for i in ea:
        if i not in ["A", "G", "T", "C"]:
            return False

    return True


def is_rna(ea):
    for i in ea:
        if i not in ["A", "G", "U", "C"]:
            return False

    return True


def is_protein(ea):
    for i in ea:
        if i not in ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y", "-"]:
            return False

    return True


def get_seq_type(ea):
    if is_dna(ea):
        return "DNA"
    elif is_rna(ea):
        return "RNA"
    elif is_protein(ea):
        return "protein"
    else:
        return "unidentified"


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
