# Requirements Interaction Analyzer

## Require libraries
TextBlob

## Running the Program

### Arguments
python3 run.py [CSV Filename] <-f resource file | resource>

#### Example
python3 run.py inputFile.csv -f resourceFile.txt

python3 run.py inputFile.csv workgroup

## Input File Formats
### CSV File
The CSV file should be a pipe (|) delimited CSV file with the fields in this order:
Number|Title|As a|Want to|So that
### Resource File
Should have resources on a single line separated by commas

