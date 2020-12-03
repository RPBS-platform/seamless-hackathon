#/bin/bash
i=1
rm -f scrambled1.fasta
while read sequence
do
echo ">seq${i}" >> scrambled1.fasta
echo $sequence>> scrambled1.fasta
((i = i + 1 ))
done < scrambled1.txt
i=1
rm -f scrambled2.fasta
while read sequence
do
echo ">seq${i}" >> scrambled2.fasta
echo $sequence>> scrambled2.fasta
((i = i + 1 ))
done < scrambled2.txt

water -asequence scrambled1.fasta -bsequence scrambled2.fasta -gapopen 10 -gapextend 0.5 -outfile RESULT
