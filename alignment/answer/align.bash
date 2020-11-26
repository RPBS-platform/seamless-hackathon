
echo '>seq1' > seq1.fasta
cat seq1 >> seq1.fasta
echo '>seq2' > seq2.fasta
cat seq2 >> seq2.fasta

water seq1.fasta seq2.fasta -gapopen 10 -gapextend 0.5 -outfile RESULT
