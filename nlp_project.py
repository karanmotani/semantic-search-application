import nltk
from nltk import tokenize
from nltk.corpus import reuters 
import time
import pysolr
from solrq import Q
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
    input = 'take care. How are you?'
    input = tokenize.sent_tokenize(input.replace('\n', ''))
    # print('Input sentence is: ', input)

    return input


def segmentation(documents, documentIDs):
    docList = []
    for i in range(len(documents)):
        sentence = tokenize.sent_tokenize(reuters.raw(documentIDs[i]).replace('\n', ''))
        for j in range(len(sentence)):
            id = str(documents[i]) + '-' + str(j)
            docList.append({'id': id, 'text': sentence[j]})

    return docList


def indexing(documents):
    docList = []

    for i in range(len(documents)):
        sentence = tokenize.sent_tokenize(reuters.raw(documents[i]).replace('\n', ''))
        for j in range(len(sentence)):

            tokens = ' '
            pos = ' '
            stems = []
            lemmas = []
            hypernyms = ' '
            hyponyms = ' '
            meronyms = ' '
            holonyms = ' '

            id = str(documents[i]) + '-' + str(j)

            # tokenize the words from the string
            listOfTokens = tokenization(sentence[j])
            tokens += ' '.join(str(x) for x in listOfTokens) + ' '

            # get POS tags for the tokens
            pos += ' '.join(str(y) for x, y in posTagging(listOfTokens)) + ' '

            for k in range(len(listOfTokens)):
                # Stem the tokens generated from tokenization
                stems.append(stemmer(listOfTokens[k]))
                # stems += stemmer(listOfTokens[k]) + ' '

                # Lemmatize the tokens generated from tokenization
                lemmas.append(lemmatize(listOfTokens[k]))
                # lemmas += lemmatize(listOfTokens[k]) + ' '

                # get the Hypernyms of the tokens generated from tokenization
                # hypernyms.append(getHypernym(listOfTokens[k]))
                hypernyms += ' '.join(str(x) for x in getHypernym(listOfTokens[k])) + ' '

                # get the Hyponyms of the tokens generated from tokenization
                # hyponyms.append(getHyponymn(listOfTokens[k]))
                hyponyms += ' '.join(str(x) for x in getHyponymn(listOfTokens[k])) + ' '

                # get the Meronyms of the tokens generated from tokenization
                # meronyms.append(getMeronym(listOfTokens[k]))
                meronyms += ' '.join(str(x) for x in getMeronym(listOfTokens[k])) + ' '

                # get the Holonyms of the tokens generated from tokenization
                # holonyms.append(getHolonyms(listOfTokens[k]))
                holonyms += ' '.join(str(x) for x in getHolonyms(listOfTokens[k])) + ' '

            stems = ' '.join(str(x) for x in stems)
            lemmas = ' '.join(str(x) for x in lemmas)

            docList.append({'id': id,
                            'text': sentence[j],
                            'tokens': tokens,
                            'posTag': pos,
                            'stem': stems,
                            'lemma': lemmas,
                            'hypernym': hypernyms,
                            'hyponym': hyponyms,
                            'meronym': meronyms,
                            'holonym': holonyms
                            },)
        break

    return docList


def queryIndexing(documents):
    docList = []

    for i in range(len(documents)):
        sentence = tokenize.sent_tokenize(documents[i].replace('\n', ''))
        for j in range(len(sentence)):

            tokens = ' '
            pos = ' '
            stems = []
            lemmas = []
            hypernyms = ' '
            hyponyms = ' '
            meronyms = ' '
            holonyms = ' '

            # id = str(documents[i]) + '-' + str(j)
            # print(id)

            # tokenize the words from the string
            listOfTokens = tokenization(sentence[j])
            tokens += ' '.join(str(x) for x in listOfTokens) + ' '
            # print(listOfTokens)

            # get POS tags for the tokens
            pos += ' '.join(str(y) for x, y in posTagging(listOfTokens)) + ' '

            for k in range(len(listOfTokens)):
                # Stem the tokens generated from tokenization
                stems.append(stemmer(listOfTokens[k]))
                # stems += stemmer(listOfTokens[k]) + ' '
                # print(stems)

                # Lemmatize the tokens generated from tokenization
                lemmas.append(lemmatize(listOfTokens[k]))
                # lemmas += lemmatize(listOfTokens[k]) + ' '
                # print(lemmas)

                # get the Hypernyms of the tokens generated from tokenization
                # hypernyms.append(getHypernym(listOfTokens[k]))
                hypernyms += ' '.join(str(x) for x in getHypernym(listOfTokens[k])) + ' '
                # print(hypernyms)

                # get the Hyponyms of the tokens generated from tokenization
                # hyponyms.append(getHyponymn(listOfTokens[k]))
                hyponyms += ' '.join(str(x) for x in getHyponymn(listOfTokens[k])) + ' '
                # print(hyponyms)

                # get the Meronyms of the tokens generated from tokenization
                # meronyms.append(getMeronym(listOfTokens[k]))
                meronyms += ' '.join(str(x) for x in getMeronym(listOfTokens[k])) + ' '
                # print(meronyms)

                # get the Holonyms of the tokens generated from tokenization
                # holonyms.append(getHolonyms(listOfTokens[k]))
                holonyms += ' '.join(str(x) for x in getHolonyms(listOfTokens[k])) + ' '
                # print(holonyms)

            stems = ' '.join(str(x) for x in stems)
            lemmas = ' '.join(str(x) for x in lemmas)

            # print(stems)
            # print(lemmas)
            # print(hypernyms)
            # print(hyponyms)
            # print(meronyms)
            # print(holonyms)

            docList.append({
                            # 'id': id,
                            'tokens': tokens,
                            'posTag': pos,
                            'stem': stems,
                            'lemma': lemmas,
                            'hypernym': hypernyms,
                            'hyponym': hyponyms,
                            'meronym': meronyms,
                            'holonym': holonyms
                            },)

    # for i in docList:
    #     print(i)

    return docList


def tokenization(sentence):
    tokens = tokenize.word_tokenize(sentence)
    # print(tokens)
    # print(type(tokens))

    return tokens


def stemmer(token):
    stemmer = PorterStemmer()
    stem = stemmer.stem(token)
    # print(token, stem)
    # print(type(stem))

    return stem


def lemmatize(token):
    lemmatizer = WordNetLemmatizer()
    lemma = lemmatizer.lemmatize(token)
    # print(token, lemma)
    # print(type(lemma))

    return lemma


def posTagging(tokens):
    posTags = nltk.pos_tag(tokens)
    # print(posTags)
    # print(type(posTags))

    return posTags


def getHypernym(token):
    hypernym = []
    synsets = wordnet.synsets(token)
    for synset in synsets:
        for h in synset.hypernyms():
            for l in h.lemmas():
                hypernym.append(l.name())
    # print(token, set(hypernym))

    return list(set(hypernym))


def getHyponymn(token):
    hyponym = []
    synsets = wordnet.synsets(token)
    for synset in synsets:
        for h in synset.hyponyms():
            for l in h.lemmas():
                hyponym.append(l.name())
    # print(token, set(hyponym))

    return list(set(hyponym))


def getMeronym(token):
    meronym = []
    synsets = wordnet.synsets(token)
    for synset in synsets:
        for h in synset.part_meronyms():
            for l in h.lemmas():
                meronym.append(l.name())
    # print(token, set(meronym))

    return list(set(meronym))


def getHolonyms(token):
    holonym = []
    synsets = wordnet.synsets(token)
    for synset in synsets:
        for h in synset.member_holonyms():
            for l in h.lemmas():
                holonym.append(l.name())
    # print(token, set(holonym))

    return list(set(holonym))


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


def deeperSearch(queryIndex):
    results = []

    # Deeper NLP Pipeline search
    for i in range(len(queryIndex)):
        tokens = queryIndex[i]['tokens']
        stems = queryIndex[i]['stem']
        lemmas = queryIndex[i]['lemma']
        posTags = queryIndex[i]['posTag']
        hypernyms = queryIndex[i]['hypernym']
        hyponyms = queryIndex[i]['hyponym']
        meronyms = queryIndex[i]['meronym']
        holonyms = queryIndex[i]['holonym']

        results.append(solr.search(Q(tokens=tokens) | Q(stem=stems), sort='score desc', score=True))

    for i in range(len(results)):
        print('\n-----------------------------------------------------------------------------------------------\n')
        print("Saw {0} result(s).".format(len(results[i])), '\n')
        print('Input sentence', i + 1, ': ', input[i])
        for result in results[i]:
            print("The ID is '{0}'.".format(result['id']))
            print("The ID is '{0}'.".format(result['text']))


if __name__ == '__main__':
    start_time = time.clock()
    documentIDs, train, test = getDocuments()
    input = getInput()

    # Task 2 - Naive approach
    # indexData = segmentation(test, documentIDs)
    # solrData(indexData)
    # searching(input)

    # Task 3 - Deeper NLP Pipeline
    index = indexing(train)
    solrData(index)
    queryIndex = queryIndexing(input)
    deeperSearch(queryIndex)

    print('Total Time Taken: ', round((time.clock() - start_time) / 60, 2), ' minutes')