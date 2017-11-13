import nltk
from nltk import tokenize
from nltk.corpus import reuters 
import time
import pysolr
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# nltk.download('reuters')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

solr = pysolr.Solr('http://localhost:8983/solr/nlp-core1', timeout=10)
solr.delete(q='*:*')


def getDocuments():
    documentIDs = reuters.fileids()
    train = list(filter(lambda doc: doc.startswith('train'), documentIDs))
    test= list(filter(lambda doc: doc.startswith('test'), documentIDs))

    print('# Documents :', len(documentIDs))

    return documentIDs, train, test


def getInput():
    # Getting the input search query
    input = 'suppliers were. production'
    input = tokenize.sent_tokenize(input.replace('\n', ''))
    print('Input sentence is: ', input)

    return input


def segmentation(documents, documentIDs):
    docList = []
    for i in range(len(documents)):
        sentence = tokenize.sent_tokenize(reuters.raw(documentIDs[i]).replace('\n', ''))
        for j in range(len(sentence)):
            id = str(documents[i]) + '-' + str(j)
            docList.append({'id': id, 'text': sentence[j]})

    return docList


def indexing(documents, documentIDs):
    docList = []
    for i in range(len(documents)):
        sentence = tokenize.sent_tokenize(reuters.raw(documentIDs[i]).replace('\n', ''))
        for j in range(len(sentence)):

            # tokenize the words from the string
            tokens = tokenization(sentence[j])

            # get POS tags for the tokens
            pos = posTagging(tokens)

            for k in range(len(tokens)):

                # Stem the tokens generated from tokenization
                stems = stemmer(tokens[k])

                # Lemmatize the tokens generated from tokenization
                lemmas = lemmatize(tokens[k])

                # get the Hypernyms of the tokens generated from tokenization
                hypernyms = getHypernym(tokens[k])

                # get the Hyponyms of the tokens generated from tokenization
                hyponyms = getHyponymn(tokens[k])

                # get the Meronyms of the tokens generated from tokenization
                meronyms = getMeronym(tokens[k])

                # get the Holonyms of the tokens generated from tokenization
                holonyms = getHolonyms(tokens[k])

        break

    # print(docList)


def tokenization(sentence):
    tokens = tokenize.word_tokenize(sentence)
    # print(tokens)

    return tokens


def stemmer(token):
    stemmer = PorterStemmer()
    stem = stemmer.stem(token)
    # print(token, stem)

    return stem


def lemmatize(token):
    lemmatizer = WordNetLemmatizer()
    lemma = lemmatizer.lemmatize(token)
    # print(token, lemma)

    return lemma


def posTagging(tokens):
    posTags = nltk.pos_tag(tokens)
    # print(posTags)

    return posTags


def getHypernym(token):
    hypernym = []
    synsets = wordnet.synsets(token)
    for synset in synsets:
        for h in synset.hypernyms():
            for l in h.lemmas():
                hypernym.append(l.name())
    # print(token, set(hypernym))

    return set(hypernym)


def getHyponymn(token):
    hyponym = []
    synsets = wordnet.synsets(token)
    for synset in synsets:
        for h in synset.hyponyms():
            for l in h.lemmas():
                hyponym.append(l.name())
    print(token, set(hyponym))

    return set(hyponym)


def getMeronym(token):
    meronym = []
    synsets = wordnet.synsets(token)
    for synset in synsets:
        for h in synset.part_meronyms():
            for l in h.lemmas():
                meronym.append(l.name())
    # print(token, set(meronym))

    return set(meronym)


def getHolonyms(token):
    holonym = []
    synsets = wordnet.synsets(token)
    for synset in synsets:
        for h in synset.member_holonyms():
            for l in h.lemmas():
                holonym.append(l.name())
    # print(token, set(holonym))

    return set(holonym)


def solrData(indexData):
    # Adding the data to solr
    solr.add(indexData)


def searching(input):
    results = []
    # Naive semantic searching
    for i in range(len(input)):
        testSentence = 'text: (' + input[i] + ')'
        results.append(solr.search(testSentence, sort='score desc'))

    for i in range(len(results)):
        # print("Saw {0} result(s).".format(len(results[i])), '\n')
        print('\n-----------------------------------------------------------------------------------------------\n')
        print('Input sentence', i + 1, ': ', input[i])
        for result in results[i]:
            print("The ID is '{0}'.".format(result['id']))
            print("The text is '{0}'.".format(result['text']))


if __name__ == '__main__':
    start_time = time.clock()
    documentIDs, train, test = getDocuments()
    # input = getInput()

    # Task 2 - Naive approach
    # indexData = segmentation(test, documentIDs)
    # solrData(indexData)
    # searching(input)

    # Task 3 - Deeper NLP Pipeline
    indexing(test, documentIDs)
    print('Total Time Taken: ', round((time.clock() - start_time) / 60, 2), ' minutes')