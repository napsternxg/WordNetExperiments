# coding: utf-8

from nltk.corpus import wordnet as wn

all_synsets = set()
for word in wn.words():
    for synset in wn.synsets(word):
        all_synsets.add(synset)

with open("wordnet_synset_definition.txt", "wb+") as fp:
    for synset in all_synsets:
        print >> fp, "%s\t%s" % (
                synset.name(),
                synset.definition()
                )

