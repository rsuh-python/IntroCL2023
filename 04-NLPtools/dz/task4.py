from nltk.tag.stanford import StanfordNERTagger
jar = "stanford-ner-2015-04-20/stanford-ner-3.5.2.jar"
model = "stanford-ner-2015-04-20/classifiers/" 
st_4class = StanfordNERTagger(model + "english.conll.4class.distsim.crf.ser.gz", jar, encoding='utf8')  #используется 4 class model for recognizing locations, persons, organizations, and miscellaneous entities

with open('news.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    f.close()

for i in [st_4class.tag(text.split())]:
  for b in i:
    if b[1] != 'O':
        print(b)

