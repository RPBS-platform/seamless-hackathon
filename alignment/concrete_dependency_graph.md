Protein sequence 1 & 2:
    Type: data (web user inputs)
    Name: seq1, seq2
    Format: raw text

Sequence alignment:
    Type: computation
    Inputs: seq1, seq2
    Format: command line tool
    Implementation: EMBOSS "water" command
    Output: alignment+score

Alignment+score:
    Type: data (web result)
    Name: alignment
    Format: text, EMBOSS "water" report

Generate scrambled sequences:
    Type: tool
    Name: scramble
    Format: Python
    Input: sequence
        Name: seq
        Format: raw text
    Output: 50 scrambled sequences
        Name: scrambled
        Format: raw text (one sequence per line)

Generate scrambled sequences 1:
    Type: computation
    Tool: scramble
    Input: seq1 => seq
    Output: scrambled1 <= scrambled

Generate scrambled sequences 2:
    Type: computation
    Tool: scramble
    Input: seq2 => seq
    Output: scrambled2 <= scrambled

scrambled1, scrambled2:
    Type: data
    Format: raw text (one sequence per line)

Align scrambled sequences:
    Type: computation
    Name: align_scrambled
    Inputs: scrambled1, scrambled2
    Description:
        Aligns every sequence N in scrambled1
         against every sequence M in scrambled2
         and calculates the alignment score
    Format: command line tool
    Implementation: EMBOSS "water" command
    Output: Scrambled alignment scores

Scrambled alignment scores:
    Type: data
    Name: scrambled_scores
    Format: text, MxN lines, 1 score per line

Analyze alignment scores:
    Type: computation
    Name: analyze_alignment_scores
    Format: Python
    Inputs:
        - Alignment+score
            Name: alignment
        - Scrambled alignment scores
            Name: scrambled_scores
    Description:
        Extract the score from the alignment
        and calculate its Z-score against the scrambled alignment scores.
        Finally, calculate the p-value of the alignment
    Output:
        Z-score and p-value

Z-score and p-value:
    Type: data (web result)
    Format: JSON
        Fields:
            - z (number)
            - p (number)