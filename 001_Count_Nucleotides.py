def countNucs(DNAseq):
    return str(DNAseq.count('A'))+ " " + str(DNAseq.count('C')) \
     + " " + str(DNAseq.count('G')) + " " + str(DNAseq.count('T'))


tempSeq = input("Please enter DNA sequence: ")
print(countNucs(tempSeq))
