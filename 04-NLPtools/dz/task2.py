#этот код ещё ужаснее...
#слова, идущие после предлогов, записываются в отдельный массив для каждого предлога. потом для каждого в цикле идёт проверка на соответствие падежу, и таким образом обновляются счётчики.
#наверное, можно было бы обойтись одним массивом и сильно меньшим количеством строчек, но я пока это никак не оптимизировал и не делал отладку...

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pymorphy2
nltk.download('stopwords')
nltk.download('punkt')


lemmatizer = WordNetLemmatizer()
morph = pymorphy2.MorphAnalyzer()

with open('222.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    f.close()

tokens = word_tokenize(text)

prepositions = ['на', 'о', 'об', 'обо', 'в', 'во', 'за', 'под', 'подо', 'между', 'меж', 'по', 'с', 'со']

c = nltk.ConcordanceIndex(text.tokens, key = lambda s: s.lower())

i = 0

nominative = 0 #пока не знаю, включать ли loc2, acc2, gen2
genitive = 0
dative = 0
accusative = 0
ablative = 0
locative = 0



#-----------------------------------------------------------------------------



na = []
na = [text1.tokens[offset+1] for offset in c.offsets(prepositions[0])]
while i < len (na): #падежи винительный, предложный
  parse = morph.parse(na[i])
  t = parse[0].tag
  if t.case == 'acc':
    accusative+=1
  if t.case == 'loct':
    locative+=1 

  i+=1
print ('accusative:' accusative, ' ', 'locative:', locative, "\n")
i = 0
accusative = 0
locative = 0



o = []
o = [text1.tokens[offset+1] for offset in c.offsets(prepositions[1])]
while i < len (o): #падежи винительный, предложный
  parse = morph.parse(o[i])
  t = parse[0].tag
  if t.case == 'acc':
    accusative+=1
  if t.case == 'loct':
    locative+=1 

  i+=1
print ('accusative:' accusative, ' ', 'locative:', locative, "\n")
i = 0
accusative = 0
locative = 0



ob = []
ob = [text1.tokens[offset+1] for offset in c.offsets(prepositions[2])]
while i < len (ob): #падежи винительный, предложный
  parse = morph.parse(ob[i])
  t = parse[0].tag
  if t.case == 'acc':
    accusative+=1
  if t.case == 'loct':
    locative+=1 

  i+=1
print ('accusative:' accusative, ' ', 'locative:', locative, "\n")
i = 0
accusative = 0
locative = 0



obo = []
obo = [text1.tokens[offset+1] for offset in c.offsets(prepositions[3])]
while i < len (obo): #падежи винительный, предложный
  parse = morph.parse(obo[i])
  t = parse[0].tag
  if t.case == 'acc':
    accusative+=1
  if t.case == 'loct':
    locative+=1 

  i+=1
print ('accusative:' accusative, ' ', 'locative:', locative, "\n")
i = 0
accusative = 0
locative = 0



v = []
v = [text1.tokens[offset+1] for offset in c.offsets(prepositions[4])]
while i < len (v): #падежи винительный, предложный
  parse = morph.parse(v[i])
  t = parse[0].tag
  if t.case == 'acc':
    accusative+=1
  if t.case == 'loct':
    locative+=1 

  i+=1
print ('accusative:' accusative, ' ', 'locative:', locative, "\n")
i = 0
accusative = 0
locative = 0



vo = []
vo = [text1.tokens[offset+1] for offset in c.offsets(prepositions[5])]
while i < len (vo): #падежи винительный, предложный
  parse = morph.parse(vo[i])
  t = parse[0].tag
  if t.case == 'acc':
    accusative+=1
  if t.case == 'loct':
    locative+=1 

  i+=1
print ('accusative:' accusative, ' ', 'locative:', locative, "\n")
i = 0
accusative = 0
locative = 0



#-----------------------------------------------------------------------------



za = []
za = [text1.tokens[offset+1] for offset in c.offsets(prepositions[6])]
while i < len (za): #падежи винительный, творительный
  parse = morph.parse(za[i])
  t = parse[0].tag
  if t.case == 'acc':
    accusative+=1
  if t.case == 'ablt':
    ablative+=1 

  i+=1
print ('accusative:' accusative, ' ', 'ablative:', ablative, "\n")
i = 0
accusative = 0
ablative = 0



pod = []
pod = [text1.tokens[offset+1] for offset in c.offsets(prepositions[7])]
while i < len (pod): #падежи винительный, творительный
  parse = morph.parse(pod[i])
  t = parse[0].tag
  if t.case == 'acc':
    accusative+=1
  if t.case == 'ablt':
    ablative+=1 

  i+=1
print ('accusative:' accusative, ' ', 'ablative:', ablative, "\n")
i = 0
accusative = 0
ablative = 0



podo = []
podo = [text1.tokens[offset+1] for offset in c.offsets(prepositions[8])]
while i < len (podo): #падежи винительный, творительный
  parse = morph.parse(podo[i])
  t = parse[0].tag
  if t.case == 'acc':
    accusative+=1
  if t.case == 'ablt':
    ablative+=1 

  i+=1
print ('accusative:' accusative, ' ', 'ablative:', ablative, "\n")
i = 0
accusative = 0
ablative = 0



#-----------------------------------------------------------------------------



mezdu = []
mezdu = [text1.tokens[offset+1] for offset in c.offsets(prepositions[9])]
while i < len (mezdu): #падежи родительный, творительный
  parse = morph.parse(mezdu[i])
  t = parse[0].tag
  if t.case == 'gent':
    genitive+=1
  if t.case == 'ablt':
    ablative+=1 

  i+=1
print ('genitive:' genitive, ' ', 'ablative:', ablative, "\n")
i = 0
genitive = 0
ablative = 0



mez = []
mez = [text1.tokens[offset+1] for offset in c.offsets(prepositions[10])]
while i < len (mez): #падежи родительный, творительный
  parse = morph.parse(mez[i])
  t = parse[0].tag
  if t.case == 'gent':
    genitive+=1
  if t.case == 'ablt':
    ablative+=1 

  i+=1
print ('genitive:' genitive, ' ', 'ablative:', ablative, "\n")
i = 0
genitive = 0
ablative = 0



s = []
s = [text1.tokens[offset+1] for offset in c.offsets(prepositions[12])]
while i < len (s): #падежи родительный, творительный
  parse = morph.parse(s[i])
  t = parse[0].tag
  if t.case == 'gent':
    genitive+=1
  if t.case == 'ablt':
    ablative+=1 

  i+=1
print ('genitive:' genitive, ' ', 'ablative:', ablative, "\n")
i = 0
genitive = 0
ablative = 0



so = []
so = [text1.tokens[offset+1] for offset in c.offsets(prepositions[13])]
while i < len (so): #падежи родительный, творительный
  parse = morph.parse(so[i])
  t = parse[0].tag
  if t.case == 'gent':
    genitive+=1
  if t.case == 'ablt':
    ablative+=1 

  i+=1
print ('genitive:' genitive, ' ', 'ablative:', ablative, "\n")
i = 0
genitive = 0
ablative = 0



#-----------------------------------------------------------------------------



po = []
po = [text1.tokens[offset+1] for offset in c.offsets(prepositions[11])]
while i < len (po): #падежи винительный, предложный, дательный
  parse = morph.parse(po[i])
  t = parse[0].tag
  if t.case == 'acc':
    accusative+=1
  if t.case == 'loct':
    locative+=1 
  if t.case == 'datv':
    dative+=1     

  i+=1
print ('accusative:' accusative, ' ', 'locative:', locative, ' ', 'dative:', dative, "\n")
i = 0
accusative = 0
locative = 0
dative = 0

