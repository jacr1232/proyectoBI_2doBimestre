import os
import pickle
import json
from textblob.classifiers import NaiveBayesClassifier

def guardar_clasificador(classifier):
    f = open('clasificador_de_sentimientos.pickle', 'wb')
    pickle.dump(classifier, f)
    f.close()

def cargar_clasificador():
    f = open('clasificador_de_sentimientos.pickle', 'rb')
    classifier = pickle.load(f)
    f.close()
    return classifier

if os.path.isfile('clasificador_de_sentimientos.pickle'):
    cl = cargar_clasificador()
else:
    with open('training.csv', 'r') as fp:
        cl = NaiveBayesClassifier(fp, format="csv")
        guardar_clasificador(cl)
'''
c = cl.classify("es fantastico ")
print format(c)
'''
positivos=0;
negativos=0;
neutros=0;
with open('consulta_cuenca.json', 'r') as f:
    tweets = json.load(f)
    for element in tweets['hits']['hits']:
        var= element['_source']['value']
        c=cl.classify("es fantastico ");
        if(format(c)=='pos'):
            positivos=positivos+1
        if(format(c)=='neg'):
            negativos=negativos+1
        if(format(c)=='neu'):
            neutros=neutros +1
    
# grafico
from pylab import *
figure(1, figsize=(8,8))
ax = axes([0, 0, 0.9, 0.9])
labels = 'por el si','por el no','neutros'
fracs = [positivos,negativos,neutros]
explode=(0.1, 0, 0)
pie(fracs, explode=explode,labels=labels, autopct='%10.0f%%', shadow=True)
legend()
title('Analisis consulta Cuenca', bbox={'facecolor':'0.8', 'pad':5})

savefig("pie_cuenca.png")
show()#mostrar grafico
