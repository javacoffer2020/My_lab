from re import template
import nltk
from nltk.corpus import brown


def clean_words(words):
    import re

    bts_copy = [(word, re.sub(r"-HL$|-NC$|-TL$", "", tag)) for word, tag in words]
    return bts_copy


def find_tag_words(words, targed_tag="", reverse=True):
    _words = []
    for word, tag in words:
        # if tag.startswith(targed_tag):
        if tag == targed_tag:
            _words.append(word.lower())
    _words = list(set(_words))
    finded_words = sorted(_words, reverse=reverse)
    return finded_words


def find_three_words(words, targed_tag="", reverse=True):
    jg = []
    for pair1, pair2, pair3 in nltk.trigrams(words):
        if "+".join([pair1[1], pair2[1], pair3[1]]) == targed_tag:
            jg.append(" ".join([pair1[0], pair2[0], pair3[0]]))
    _words = list(set(jg))
    finded_words = sorted(_words, reverse=reverse)
    return finded_words


def part_1(words):
    return find_tag_words(words, "MD")


def part_2(words):
    return find_tag_words(words, "NNS")


def part_3(words):
    words_cp = clean_words(words)
    return find_three_words(words_cp, "IN+AT+NN", reverse=False)


def sum_word(words, targets=[]):
    cfd = nltk.ConditionalFreqDist(words)
        PP_dict = nltk.defaultdict(int)
    total_PP = 0
    for word in word_list:
        temp_num = sum(i for _, i in cfd(word).items())
        PP_dict[word] = temp_num
        print("{}")
        total_PP += temp_num

    brown_tagged_words = brown.tagged_words()
    cfd = nltk.ConditionalFreqDist(brown_tagged_words)
    print(cfd['his'].items())
    print(sum(num for _, num in cfd['his'].items()))
    print(list(cfd['her']))
    print(list(cfd['hers']))
    print(list(cfd['himself']))
    print(list(cfd['herself']))
    # print(part_3(brown_tagged_words))
