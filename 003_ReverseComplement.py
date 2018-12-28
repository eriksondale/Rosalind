def revComp(Seq):
    Seq = Seq.lower()
    Seq = Seq[::-1]
    Seq = Seq.replace("a","T")
    Seq = Seq.replace("t","A")
    Seq = Seq.replace("c","G")
    Seq = Seq.replace("g","C")
    return Seq

tempSeq = input("Please enter a nucleotide sequence: ")
print(revComp(tempSeq))
