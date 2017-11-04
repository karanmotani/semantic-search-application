import nltk
from nltk import tokenize
from nltk.corpus import reuters 
import time
import pysolr

nltk.download('reuters')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

start_time = time.clock()

solr = pysolr.Solr('http://localhost:8983/solr/nlp-core1', timeout=10)
solr.delete(q='*:*')

documentIDs = reuters.fileids()

train_docs = list(filter(lambda doc: doc.startswith("train"),documentIDs))
test_docs = list(filter(lambda doc: doc.startswith("test"),documentIDs))

print("# Documents :", len(documentIDs))
print('\n')

docList = []

for i in range(len(test_docs)):
    sentence = tokenize.sent_tokenize(reuters.raw(documentIDs[i]).replace("\n",""))
    for j in range(len(sentence)):
        id = str(test_docs[i]) + '-' + str(j)
        docList.append({"id": id,"text": sentence[j]})

solr.add(docList)
results = solr.search('text: (suppliers were)', sort='score desc')

print(results, '\n')
print("Saw {0} result(s).".format(len(results)), '\n')

for result in results:
    print("The ID is '{0}'.".format(result['id']))
    print("The title is '{0}'.".format(result['text']))

print("\nTotal Time Taken: " , round((time.clock() - start_time)/60,2), " minutes \n")
