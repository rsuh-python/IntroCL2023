import pyconll
import re
import pymorphy2

text = pyconll.load_from_file('GramEval2020-GSD-train.conllu')
splits = text.split ("\n\n") #распиливает строку на предложения, смотря по двойному отступу
print (len(splits)) #смотрим сколько элементов
i = 0

while i < (len(splits)): 
  if 'discourse' or 'dislocated' in splits[i]:
    current = parse (splits[i])
    current
  else:
    print ('Not found\n')

  i+=1
