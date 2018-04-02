# Requirements Interaction Analyzer

## Require libraries

TextBlob

## Running the Program

The program is to be ran using python3.

In order to run it using Jaccard-Indexing use run-jaccard.py

In order to run it using TF-IDF use run-tf_idf.py

### Arguments

-i [input file]

-o [output file] default = output.txt

-f [resource file]

-r [resource]

-t [threshold(float between 0 and 1)] default = 0.25

## Input File Formats

### CSV File
The CSV file should be a pipe (|) delimited CSV file with the fields in this order:

Number|Title|As a|Want to|So that

### Resource File

Should have resources on a single line separated by commas

