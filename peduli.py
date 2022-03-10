import re

import pandas as pd

from nltk import word_tokenize
from nltk import FreqDist
from nltk.corpus import stopwords
from string import punctuation
from time import sleep

# from nltk import download
# download('punkt')
# download('stopwords')

'''
\d  > [0-9]
\D  > [^0-9]
\s  > [ \t\n\r\f\v]
\S  > [^ \t\n\r\f\v]
\w  > [a-zA-Z0-9_]
\W  > [^a-zA-Z0-9_]
*   > {0,}
+   > {1,}
?   > {0,1}
'''
def cleaner(sentence):
    review = sentence.lower()
    
    # clear double letters
    review = re.compile(r"(.)\1{1,}").sub(r"\1", review )
    # clear @username
    review = re.sub('@[^\s]+', '', review )
    # clear #tag
    review = re.sub(r'#([^\s]+)', '', review )
    # clear non-ascii value
    review = re.sub(r'[^\x00-\x7f]', r'', review )
    review = re.sub(r'(\\u[0-9A-Fa-f]+)', r'', review )
    review = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", review )
    review = re.sub(r'\\u\w\w\w\w', '', review )
    # remove symbol, number, and strange char
    review = re.sub(r"[.,:;+!\-_<^/=?\"'\(\)\d\*]", " ", review )
    
    return review

tes = 'Me^ncoba menggunakan kalimat i234234ni 10237sebanyak (sepuluh) 10 kali agar mudah'
re.sub("[0-9()] *", "", tes)
re.sub(" +", " ", tes)
dir(re.ASCII)


df = pd.read_csv('d:/backup/hello/peduli5159.csv', usecols=['star', 'review'])

df.head(), df.shape

df.star = df.star.apply(lambda x: 1 if int(x[14]) > 3 else 0)

print('Positif', df[df.star == 1].shape)
print('Negatif', df[df.star == 0].shape)

print(stopwords.words('indonesian'))

sw_indo = stopwords.words('indonesian')

df.head(), df.shape
df.review = df.review.apply(lambda x: x.lower())
df.review = df.review.apply(lambda x: cleaner(x))
df.review = df.review.apply(lambda x: ' '.join(x.split()))
df.review = df.review.apply(lambda x: ' '.join([word for word in x.split() if word not in sw_indo]))
df.review

all_vocab = ''
all_vocab

for i in range(len(df)):
    all_vocab += df.review.loc[i]

print(FreqDist(all_vocab.split()))