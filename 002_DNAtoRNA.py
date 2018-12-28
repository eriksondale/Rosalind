def DNAtoRNA(DNAseq):
    return DNAseq.replace("T","U")

tempSeq = input("Please enter a DNA sequnce: ")
print(DNAtoRNA(tempSeq))
