import nltk
from nltk import tokenize
from operator import itemgetter
import math
import spacy
from newspaper import Article
from spacy.lang.en.stop_words import STOP_WORDS

url = "https://opensource.com/article/17/11/intro-tensorflow " #User Entered Article Here
Tech_url = "https://www.edureka.co/blog/top-10-trending-technologies/" #sample Article to Train Spacy Model

article = Article(url)
article.download()
article.parse()

article1 = Article(Tech_url)
article1.download()
article1.parse()


doc = article.text
checker_doc = article1.text

nlp = spacy.load('en_core_web_lg')

spacy_stopwords = nlp.Defaults.stop_words

my_doc = nlp(doc)
my_doc1 = nlp(checker_doc)

token_list = []
for token in my_doc:
    token_list.append(token.text)

fs =[]

for word in token_list:
    lexeme = nlp.vocab[word]
    if lexeme.is_stop == False:
        fs.append(word)

token_list1 = []
for token in my_doc1:
    token_list1.append(token.text)
 
fs1 =[]

for word in token_list1:
    lexeme = nlp.vocab[word]
    if lexeme.is_stop == False:
        fs1.append(word)

def listToString(s):

    str1 = ""

    for ele in s:
        str1 += ele
        str1 +=" "

    return str1

s = listToString(fs)
s1 = listToString(fs1)

c = nlp(s)
c1 = nlp(s1)

val=(c.similarity(c1))

if val>0.9:
    print("Its a Tech Related Article")
else:
    print("Its Not a Tech Related Article")

# THE END
