import os

from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
langs = ['cplusplus', 'java', 'php al19']
def load_corpus():
    corpus = []
    for lang in langs:
        for filename in os.listdir('./resources/'+lang):
            with open(os.path.join('./resources/'+lang, filename), 'r') as f:
                corpus.append(f.read())
    return corpus


vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(load_corpus())
#feature_names = vectorizer.get_feature_names()
#print(feature_names)
#print('import' in feature_names)
Y = [0]*11462 +[1]*(21438-11462)+[2]*(22540-21438)
print(Y)
print(len(Y))
clsf =svm.SVC()
clsf.fit(X, Y)
with open('test.txt', 'r') as f:
    buff = f.read()
prepr = vectorizer.transform([buff])
print(clsf.predict(prepr))
