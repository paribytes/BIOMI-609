import numpy as np
import matplotlib.pyplot as plt

#write a program that will take a FASTQ file as an input and print the distribution of quality scores across all reads.
from Bio import SeqIO

fastq_file = next(SeqIO.parse("assignment1.fastq", "fastq")) #taking assignment.fastq file as an input

textlength = len(fastq_file)

quality_scores = []#making my future self's life easier

for base in fastq_file:
    ascii = ord(base) #converting each base into its ascii code
    print(base, "\t", ascii)
    print(fastq_file.seq)#printing the sequences in the file
    quality_scores.append(fastq_file.letter_annotations["phred_quality"])#Q-score

#print(matplotlib.__version__) #just checking the version of my matplotlib
#Plotting the distribution of Q-scores
quality_scores = np.array(quality_scores)#need to learn more about numpy arrays

plt.boxplot(quality_scores)#generating the boxplot

plt.xlabel("Base position")#labeling my x-axis
plt.ylabel("Quality score")#labeling my y-axis
plt.title("Quality score distribution")
plt.show()#show me the plot

