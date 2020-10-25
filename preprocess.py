import re
import pandas as pd
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

data = pd.read_csv("lyrics.csv", names=['num', 'lyrics', 'mood'], dtype = 'object')

data = data[data['lyrics'].notna()]
data = data.reset_index(drop=True)



def text_preprocess(ds):
    for m in range(len(ds)):

        main_words = re.sub('[^A-Za-z ]', '', ds.loc[m, "lyrics"])
        main_words = (main_words.lower()).split()
        main_words = [w for w in main_words if not w in set(stopwords.words('english'))]

        lem = WordNetLemmatizer()
        main_words = [lem.lemmatize(w) for w in main_words if len(w) > 1]

        main_words = ' '.join(main_words)
        ds.loc[m, "lyrics"] = main_words
    return ds


data = text_preprocess(data)
data.to_csv(r'processed_lyrics.csv')
