import pysam
from pysam import VariantFile

#I am aware the question asked to use chr16.vcf.gz file, however when i tried to "gunzip" it, it gave an EOF error. So, I have used chr16_hwe.vcf instead. Hope that's okay.

#gunzip chr16_hwe.vcf.gz

#THE FOR LOOP BELOW WILL FEEL LIKE AN INFINITY LOOP BUT IS NOT 

Shah_vcf_file = pysam.VariantFile('chr16_hwe.vcf', 'r')

for rec in Shah_vcf_file:
        print(rec.chrom, rec.pos, rec.ref, rec.alts)
            
Shah_vcf_file.close()

#RAN BELOW CODES FIRST 

#vcftools --gzvcf chr16.vcf.gz --hardy
#vcftools --gzvcf chr16.vcf.gz --hwe 0.05 --min-alleles 2 --max-alleles 2 --recode --stdout | gzip -c > chr16_hwe.vcf.gz
#ESTIMATING HETEROZYGOSITY
#vcftools --gzvcf chr16_hwe.vcf.gz 
#ESTIMATING ALLELE FREQUENCIES 
#vcftools --gzvcf chr16_hwe.vcf.gz --freq2 

#ATTACHING THE OUTPUT OF ALL THESE AS SEPARATE FILES