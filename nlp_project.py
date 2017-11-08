import nltk
from nltk import tokenize
from nltk.corpus import reuters 
import time
import pysolr

# nltk.download('reuters')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

start_time = time.clock()

solr = pysolr.Solr('http://localhost:8983/solr/nlp-core1', timeout=10)
solr.delete(q='*:*')

documentIDs = reuters.fileids()

train_docs = list(filter(lambda doc: doc.startswith("train"),documentIDs))
test_docs = list(filter(lambda doc: doc.startswith("test"),documentIDs))

print("# Documents :", len(documentIDs))

docList = []
results = []

for i in range(len(test_docs)):
    sentence = tokenize.sent_tokenize(reuters.raw(documentIDs[i]).replace("\n",""))
    for j in range(len(sentence)):
        id = str(test_docs[i]) + '-' + str(j)
        docList.append({"id": id,"text": sentence[j]})

solr.add(docList)
input = 'suppliers were. production'
input = tokenize.sent_tokenize(input.replace("\n",""))
print('Input sentence is: ', input, '\n')
for i in range(len(input)):
    testSentence = 'text: (' + input[i] + ')'
    results.append(solr.search(testSentence, sort='score desc'))

for i in range(len(results)):
    # print("Saw {0} result(s).".format(len(results[i])), '\n')
    print('Input sentence', i+1, ': ', input[i])
    for result in results[i]:
        print("The ID is '{0}'.".format(result['id']))
        print("The text is '{0}'.".format(result['text']))
        print('\n')

print("Total Time Taken: " , round((time.clock() - start_time)/60,2), " minutes \n")
