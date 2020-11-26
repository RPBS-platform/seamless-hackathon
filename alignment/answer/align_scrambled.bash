for seq1 in `cat scrambled1`; do
    for seq2 in `cat scrambled2`; do
        echo '>seq1' > seq1.fasta
        echo $seq1 >> seq1.fasta
        echo '>seq2' > seq2.fasta
        echo $seq2 >> seq2.fasta

        water seq1.fasta seq2.fasta -gapopen 10 -gapextend 0.5 -outfile temp.water
        score=`awk '$2 == "Score:"{print $3; exit}' temp.water`
        echo $score >> RESULT
    done
done
