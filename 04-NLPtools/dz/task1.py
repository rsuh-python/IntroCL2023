
#это можно было сделать гораздо красивее, но времени нет(

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('punkt')

lemmatizer = WordNetLemmatizer()

sample = input("Название файла (с расширением): ")

with open(sample, 'r', encoding='utf-8') as f:
    text0 = f.read()
    f.close()
with open('1.txt', 'r', encoding='utf-8') as f:
    text1 = f.read()
    f.close()
with open('2.txt', 'r', encoding='utf-8') as f:
    text2 = f.read()
    f.close()
with open('3.txt', 'r', encoding='utf-8') as f:
    text3 = f.read()
    f.close()
with open('4.txt', 'r', encoding='utf-8') as f:
    text4 = f.read()
    f.close()
with open('5.txt', 'r', encoding='utf-8') as f:
    text5 = f.read()
    f.close()

tokens0 = word_tokenize(text0) #токенизация всего сразу
tokens1 = word_tokenize(text1)
tokens2 = word_tokenize(text2)
tokens3 = word_tokenize(text3)
tokens4 = word_tokenize(text4)
tokens5 = word_tokenize(text5)

#на этом этапе нужно выкинуть всю пунктуацию

lemma0 = lemmatizer.lemmatize(tokens0) #лемматизация всего сразу
lemma1 = lemmatizer.lemmatize(tokens1)
lemma2 = lemmatizer.lemmatize(tokens2)
lemma3 = lemmatizer.lemmatize(tokens3)
lemma4 = lemmatizer.lemmatize(tokens4)
lemma5 = lemmatizer.lemmatize(tokens5)

a = len(list(set(tokens0).intersection(set(tokens1)))) #рассматриваем размеры пересечений лемм
b = len(list(set(tokens0).intersection(set(tokens2))))
c = len(list(set(tokens0).intersection(set(tokens3))))
d = len(list(set(tokens0).intersection(set(tokens4))))
e = len(list(set(tokens0).intersection(set(tokens5))))

random_list = []
random_list.append (a,b,c,d,e)

closest = max (random_list) #мы записали все размеры пересечений по порядку в массив, и теперь выбираем максимальное пересечение

match closest:
  case random_list[0]: print ("Совпадает с текстом 1")
  case random_list[1]: print ("Совпадает с текстом 2")
  case random_list[2]: print ("Совпадает с текстом 3")
  case random_list[3]: print ("Совпадает с текстом 4")
  case random_list[4]: print ("Совпадает с текстом 5")  
