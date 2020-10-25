import pandas as pd
import numpy as np

data = pd.read_csv("processed_lyrics.csv")

arr = []
for i in range(len(data)):
    arr.extend([data.loc[i, "lyric"].split()])

data["split_lyrics"] = arr

arr1 = []
dict1 = {}

for i in range(len(arr)):
    arr1.extend(data.loc[i, "split_lyrics"])

for i in arr1:
    if i in dict1.keys():
        dict1[i] += 1
    else:
        dict1[i] = 1


print(data.loc[4,"mood"])

# creating the feature matrix
from sklearn.feature_extraction.text import CountVectorizer

matrix = CountVectorizer(max_features=1000)

X = matrix.fit_transform(data["lyric"])
Y = X.toarray()

Y_df = pd.DataFrame(Y, columns=matrix.get_feature_names())
Y_df["mood_label"] = data["mood"]

Y_df.to_csv(r'vectorized.csv')
# for i in X[1]:
#     if i > 0:
#         print("True")
#     else:
#         print("False")
