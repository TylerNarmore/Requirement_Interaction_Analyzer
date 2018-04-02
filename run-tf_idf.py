from extractCSV import *
from textblob import TextBlob as tb
from tfidf_Calculation import *
from copy import deepcopy
import sys


def main():
    for arg in range(len(sys.argv)):
        # input output file flags
        if sys.argv[arg] == '-i':
            requirements_file = sys.argv[arg + 1]
        elif '-i' not in sys.argv:
            raise ValueError("Missing input file argument")

        if sys.argv[arg] == '-o':
            output_file_name = sys.argv[arg + 1]
        elif '-o' not in sys.argv:
            output_file_name = "output.txt"

        # resource flags
        if sys.argv[arg] == '-f':
            resource_file_name = sys.argv[arg + 1]
            resource_file = open(resource_file_name, 'r')
            resources = resource_file.readline().rstrip('\n').split(',')
            resource_file.close()
        if sys.argv[arg] == '-r':
            resources = [sys.argv[arg + 1]]
        if '-f' not in sys.argv and '-r' not in sys.argv:
            raise ValueError("No resource input")

        if sys.argv[arg] == '-t':
            threshold = float(sys.argv[arg + 1])
        elif '-t' not in sys.argv:
            threshold = 0.25

    requirements_dictionary = extractFromCSV(requirements_file)

    bloblist = []

    for requirement_number in range(len(requirements_dictionary)):
        requirement_description = requirements_dictionary[requirement_number + 1].get_full_description()

        bloblist.append(tb(requirement_description))

    req_words_dict = {}
    for requirement in requirements_dictionary:
        req_words_dict[requirement] = {"words":{}}

    for i, blob in enumerate(bloblist):
        scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
        req_words_dict[i+1]["words"]= deepcopy(scores)

    # Calculate requirements relationships
    relationship_scores = {}
    for req_a in req_words_dict:
        for req_b in req_words_dict:
            if req_a == req_b:
                pass
            else:
                relation = sim(req_words_dict[req_a], req_words_dict[req_b])
                relationship_scores[(req_a, req_b)] = relation

    # Get relationships over set threshold
    relationships = []
    for pair in relationship_scores:
        if relationship_scores[pair] > threshold:
            relationships.append(pair)

    # Gathering list of items not related to resource
    to_be_deleted = []
    for item in relationships:
        valid = False
        for term in resources:
            if term not in requirements_dictionary[item[0]].get_full_description()\
                    and term not in requirements_dictionary[item[1]].get_full_description():
                pass
            else:
                valid = True
                break
        if not valid:
            to_be_deleted.append(item)
    # Removing items not related to resource
    for pair in to_be_deleted:
        relationships.remove(pair)

    output_file = open(output_file_name, 'w')
    output_file.write("Resource:" + ", ".join(resources) + '\n')
    for pair in relationships:
        string = str(pair[0]) + "," + str(pair[1]) + '\n'
        output_file.write(string)


if __name__ == '__main__':
    main()
