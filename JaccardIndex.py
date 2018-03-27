from copy import deepcopy
import statistics

class Jaccard:
    def __init__(self, description_list):
        self.description_list = description_list

        self.description_word_list = []
        for description in self.description_list:
            for word in description.words:
                self.description_word_list.append(word)
        self.description_word_list = list(set(self.description_word_list))


    def calculate(self):

        # Create table to store words and appearnce of those words in a requirement
        jaccard_table = {}
        word_table = {}
        for word in self.description_word_list:
            word_table[word] = 0
        for number in range(len(self.description_list)):
            jaccard_table[number + 1] = {"words": deepcopy(word_table), "description": self.description_list[number].words}

        #Create table with word occurences
        for requirement in jaccard_table:
            for word in jaccard_table[requirement]["words"]:
                if word in jaccard_table[requirement]["description"]:
                    jaccard_table[requirement]["words"][word] = 1

        #Calculate and store Jaccard scores in a table
        jaccard_score_table = {}
        for item_a in jaccard_table:
            jaccard_score_table[item_a] = {}
            for item_b in jaccard_table:
                jaccard_score_table[item_a][item_b] = 0
                m11 = 0
                m01 = 0
                m10 = 0
                for word in self.description_word_list:
                    if jaccard_table[item_a]["words"][word] == 1 and jaccard_table[item_b]["words"][word] == 1:
                        m11 += 1
                    elif jaccard_table[item_a]["words"][word] == 0 and jaccard_table[item_b]["words"][word] == 1:
                        m01 += 1
                    elif jaccard_table[item_a]["words"][word] == 1 and jaccard_table[item_b]["words"][word] == 0:
                        m10 += 1

                score = (m11)/(m01+m10+m11)

                jaccard_score_table[item_a][item_b] = score

        # Return list of items that are above set threshold
        threshold = 0.25
        relationships_table = {}
        for item_a in jaccard_score_table:
            item_relationships = []
            for item_b in jaccard_score_table:
                if item_a != item_b:
                    if jaccard_score_table[item_a][item_b] >= threshold:
                        item_relationships.append(item_b)
#                    print(item_a, item_b, jaccard_score_table[item_a][item_b])
            relationships_table[item_a] = item_relationships

        return relationships_table
