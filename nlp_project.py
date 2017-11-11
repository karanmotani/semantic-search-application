from nltk import tokenize
from nltk.corpus import reuters 
import time
import pysolr

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
    input = getInput()

    # Task 2 - Naive approach
    indexData = segmentation(test, documentIDs)
    solrData(indexData)
    searching(input)

    print('Total Time Taken: ', round((time.clock() - start_time) / 60, 2), ' minutes')