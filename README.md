# Wordnet embeddings

## Installation

* Install python 2.7 (suggested to use anaconda installation)
* Install gensim and nltk using `conda install gensim nltk`
* Download nltk wordnet corpora using `python -e "import nltk; nltk.download();"`, enter `d` and then `wordnet` and then `q`.


## Train embeddings of Wordnet synsets based on word definitions

Create wordnet synset definitions file using:
```
$ python extract_wn_synsets.py
```

Now train the embeddings for each synset.

```
$ python train_wordnet.py --help
Couldn't import dot_parser, loading of dot files will not be possible.
usage: train_wordnet.py [-h] [--input INPUT] [--outfile OUTFILE] [--size SIZE]
                        [--include-parts] [--stopwords STOPWORDS]

Train wordnet synset embeddings based on definition.

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT         Word net synset definition file. Each line should be
                        tab seperated synset and definition pair.
  --outfile OUTFILE     Word net synset embedding file in glove format.
  --size SIZE           Embedding size.
  --include-parts       If include parts is true, then the word becomes a sum
                        of synset, word and its POS tag.
  --stopwords STOPWORDS
                        Stopwords to use. Specify a file or use keyword
                        default to use GENSIM stopwords.

```


