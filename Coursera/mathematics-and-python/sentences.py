import numpy as np
from scipy import spatial
import re

with open("sentences.txt", 'r') as sentences_file:
    tokenized_sentences = [x.strip() for x in sentences_file.readlines()]
    tokenized_sentences = [list(filter(bool, re.split('[^a-z]', x.lower()))) for x in tokenized_sentences]

    word_list = []
    for sentence in tokenized_sentences:
        word_list += [word for word in sentence]

    word_list = set(word_list)
    word_list = {val : idx for idx, val in enumerate(word_list)}

    distances = []
    first_sentence = None

    for index, sentence in enumerate(tokenized_sentences):
        words = [sentence.count(word) for word in word_list]
        if index == 0:
            first_sentence = np.array(words)
        else:
            distances.append(spatial.distance.cosine(first_sentence, np.array(words)))

    result = [sentence for _,sentence in sorted(zip(distances, list(range(1, len(distances) + 1))))]

    res_file = open('result.txt', 'w')
    res_file.write(str(result[0]) + ' ' + str(result[1]))

    print ('')
