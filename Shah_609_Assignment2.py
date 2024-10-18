from Bio import SeqIO

#write a code to take an input genome as a FASTA file
s = ''
for seq_record in SeqIO.parse("Assignment2_refgenome.fasta", "fasta"):#taking Assignment2_refgenome file as an input
    s= str(seq_record.seq)
    print(len(seq_record))#want to see the length of my sequence
    print(s)

#construct a suffix array tree from it

suffixes = [(s[i:], i) for i in range(len(s))]#constructing the suffix array library
suffixes.sort(key=lambda x: x[0])
suffix_array = sorted([s[1] for s in suffixes])
print(suffix_array)

#take a read as input from a FASTA file
list2 = []
for seq_record in SeqIO.parse("Assignment2_read.fasta", "fasta"):#taking Assignment2_read file as an input
    list2= str(seq_record.seq) #it is 5 bases long
    print(list2) #GTTCC

#print all the positions where that read occurs in the genome
# output: 781, 1082, 1260, 1760

# BISECTION APPROACH

from bisect import bisect_left

read = "GTTCC"
i = bisect_left(suffixes, (read,)) #reference hints
matches = []
while i < len(suffixes) and suffixes[i][0].startswith(read):
    matches.append(suffixes[i][1])
    i += 1

print(sorted(matches))

# NON-BISECTION APPROACH

read = "GTTCC"
matches = []
start = 0

while read in s:
    index = s.index(read)  # Finding the read's index in s
    matches.append(index + start)  # Storing the index in the list matches
    new = index + len(read)  # Getting the new index to look from after the read
    s = s[new:]  # Adjusting the string s (removing everything till the end of the read)
    start += new  # Adjusting the value of start with respect to the original string s

print("Output with non-bisection approach is",matches)


