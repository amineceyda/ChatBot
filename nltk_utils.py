# Chatbot için Snowball Stemmer'ı ve tokenizasyon kullanarak Türkçe kelime işleme
import nltk
#nltk.download('punkt') #NLTK'nin dil verilerini indir 
from snowballstemmer import stemmer
import numpy as np


turkish_stemmer = stemmer("turkish")

#Cümlenin kelimelere ayrılmasını sağlar.
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

#Verilen kelimenin kökünü bulur ve küçük harflere döker.
def stem(word):
    return turkish_stemmer.stemWord(word.lower()) 

#Temsili kelime torbası oluşturur.
def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]

    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w, in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0

    return bag




"""
#tokenization test
a = "Kredi kartı taksit oranları"
print(a)
a = tokenize(a)
print(a)
"""

"""
words = ["krediler", "kredi", "taksitler", "oranlar", "ürünler"]
stemmed_words = [turkish_stemmer.stemWord(word) for word in words]
print(stemmed_words)
"""