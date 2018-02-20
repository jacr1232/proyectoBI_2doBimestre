import io
import json
import string
min=3001
i=3001
max=3050
with io.open('test.csv','a') as file:
    with open('training.json', 'r') as f:
            tweets = json.load(f)
    for tweet in tweets['tweets']['tweet']:
            text=tweet['content']['__cdata']
            printable = set(string.printable)
            text=filter(lambda x: x in printable, text)
            text=text.replace(",",'')
            text=text.replace("\"",'')
            text=text.replace("\n",'')
            label=tweet['sentiments']['polarity'][0]['value']
            if(label=='NONE' or label=='NEU'):
                    label='neu'
            if(label=='N'):
                    label='neg'
            if(label=='P'):
                    label='pos'
            var= text+','+label+'\n'
            if(i>=3001 and i<max):
                file.write("%s"%var)
                i=i+1;
            else:
                break
