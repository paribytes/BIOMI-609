#!/bin/sh

export PATH=$PATH:/home/exouser/Documents/tools/velvet
export PATH=$PATH:/home/exouser/tools/SPAdes-3.15.5/spades.py
chmod +x /home/exouser/tools/SPAdes-3.15.5/spades.py

export PATH=$PATH:/home/exouser/tools/quast


time velveth run_27 27 -short -separate -fastq ERR10009332_1.fastq

time velvetg run_27

python3 /home/exouser/tools/SPAdes-3.15.5/spades.py -s ERR10009332_1.fastq -k 27 -o spades_out

python3 /home/exouser/tools/quast/quast.py run_27/contigs.fa spades_out/contigs.fasta unicycler_contigs.fasta -r mpoxreference.fasta











