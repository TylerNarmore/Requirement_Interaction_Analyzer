from extractCSV import *
from textblob import TextBlob as tb
from JaccardIndex import *
import sys


def main():
#    requirements_file = input("Enter name of csv file containing the requirement descriptions: ")
#    resource = input("Enter resource to be checked: ")

    requirements_file = sys.argv[1]
    resource = sys.argv[2]


    # Extracting requirements from CSV file
    requirements_dictionary = extractFromCSV(requirements_file)

    # Creating list of requirement descriptions
    description_list = []
    for requirement_number in range(len(requirements_dictionary)):
        requirement_description = requirements_dictionary[requirement_number + 1].get_full_description()

        description_list.append(tb(requirement_description))

    # Running Jaccard indexing to get relationships
    jaccard = Jaccard(description_list)
    relationships = jaccard.calculate()

    # Gathering list of items not related to resource
    to_be_deleted = []
    for item in relationships:
        if resource not in requirements_dictionary[item].get_full_description():
            to_be_deleted.append(item)

    # Removing items not related to resource
    for item in to_be_deleted:
        del relationships[item]
    for item in relationships:
        for item2 in to_be_deleted:
            if item2 in relationships[item]:
                relationships[item].remove(item2)


    #Output to file
    outputFile = open("output.txt", 'w')

    outputFile.write("Resource: ")
    outputFile.write(resource)
    outputFile.write("\n")

    for item in relationships:
        if len(relationships[item]) > 0:
            string = str(item) + ":\t"
            string += ",\t".join(list(map(lambda  x: str(x), relationships[item])))
            string += "\n"
            outputFile.write(string)

    outputFile.close()

if __name__ == '__main__':
    main()
