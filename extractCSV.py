from requirementDescription import RequirementDescription
# ExtractCSV.py

# Function: extractFromCSV
# Input:    CSV File name
# Returns:  ???
#
def extractFromCSV(csvFileName):

    csvFile = open(csvFileName, 'r')

    #Read line to remove headers
    csvFile.readline()

    requirementDictionary  = {}

    for line in csvFile:
        number, title, asA, wantTo, soThat  =  line.rstrip('\n').split('|')
        number = int(number)

        requirementDictionary[number] = RequirementDescription(number, title, asA, wantTo, soThat)

    return requirementDictionary



