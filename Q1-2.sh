#!/bin/bash

export PATH=$PATH:/home/exouser/tools/bwa-mem2-2.0pre2_x64-linux
export PATH=$PATH:/home/exouser/tools/clustalw-2.1-linux-x86_64-libcppstatic/
export PATH=$PATH:/home/exouser/tools/samtools-1.16.1
export PATH=$PATH:/home/exouser/tools/bcftools-1.16

accession=("ERR10009307" "ERR10009351" "ERR10009332" "ERR10009372" "ERR10033521")

for id in "${accession[@]}"
do
	prefetch "$id"
	fastq-dump -I --split-files "$id"

done

bwa-mem2.sse41 index mpoxreference.fasta

fastq_files=("ERR10009307_1.fastq" "ERR10009351_1.fastq" "ERR10009332_1.fastq" "ERR10009372_1.fastq" "ERR10033521_1.fastq")

for file in "${fastq_files[@]}"
do 
	bwa-mem2.sse41 mem mpoxreference.fasta "$file" > "$file".sam
	samtools view -S -b "$file".sam > "$file".bam
	samtools view "$file".bam|head
	samtools sort "$file".bam -o "$file".sorted.bam
	samtools index "$file".sorted.bam
done

for i in {1..$n}
do
	echo "* * * * 1" >> samples.ploidy
done

bcftools mpileup -f mpoxreference.fasta *.sorted.bam | bcftools call -mv -Ov --ploidy-file samples.ploidy -o spain1.bcf

bcftools view spain1.bcf > Shah_hmpox.vcf

