
# coding: utf-8

# In[1]:

from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

from gensim.parsing import STOPWORDS
from gensim.utils import tokenize

import re
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# In[4]:

def get_tagged_document(line,
                        include_parts=False,
                       stopwords=None):
    line = line.strip().split("\t")
    words = list((w for w in tokenize(line[1])
        if w
        ))
    if stopwords is not None:
        words = [w for w in words if w not in stopwords]
    tags = [line[0]]
    if include_parts:
        line = line[0].rsplit(".", 2)[:-1]
        tags.extend([line[0], "%s_POS" % line[1]])
    return TaggedDocument(words, tags)


# In[5]:


def save_doc_vecs(model, filename):
    with open(filename, "wb+") as fp:
        print >> fp, "%s %s" % model.docvecs.doctag_syn0.shape
        for k in model.docvecs.doctags:
            v = " ".join(map(str, model.docvecs[k]))
            print >> fp, "%s %s" % (k,v)

def load_stopwords(filename):
    with open(filename) as fp:
        stopwords = set(line.strip() for line in fp)
    return stopwords

def main(args):
    stopwords = None
    if args.stopwords == "default":
        stopwords = STOPWORDS
    elif args.stopwords is not None:
        stopwords = load_stopwords(args.stopwords)

    with open(args.input) as fp:
        data = []
        for line in fp:
            data.append(get_tagged_document(line,
                stopwords = stopwords,
                include_parts=args.include_parts))    
    # In[7]:
    model = Doc2Vec(documents=data, size=args.size, dm=0,
                    window=100, workers=20)
    save_doc_vecs(model, args.outfile)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Train wordnet synset embeddings based on definition.")
    parser.add_argument("--input", type=str, default="wordnet_synset_definition.txt",
            help="Word net synset definition file. Each line should be tab seperated synset and definition pair.")
    parser.add_argument("--outfile", type=str, default="synsets.100.dbow.txt",
            help="Word net synset embedding file in glove format.")
    parser.add_argument("--size", type=int, default=30,
            help="Embedding size.")
    parser.add_argument("--include-parts", default=False, action='store_true',
            help="If include parts is true, then the word becomes a sum of synset, word and its POS tag.")
    parser.add_argument("--stopwords", type=str, default=None,
            help="Stopwords to use. Specify a file or use keyword default to use GENSIM stopwords."
            )
    args = parser.parse_args()
    print(args)
    main(args)
