import wordcloud as wordcloud
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt, seaborn as sb

data = pd.read_csv("processed_lyrics.csv")


lyrics = " ".join(w for w in data["lyric"])

# arr = []
# for i in range(len(data)):
#     arr.extend([data.loc[i, "lyric"].split()])
#
# data["split_lyrics"] = arr

# Function to create a word cloud object from the corpus with the color map as passed
def generateWordCloud(corpus: str, cmap: str) -> wordcloud:
    """
    Return a Word Cloud object generated from the corpus and color map parameter.
    """
    wordcloud = WordCloud(background_color='black', width=800, height=400,
                          colormap=cmap, max_words=180, contour_width=3,
                          max_font_size=80, contour_color='steelblue',
                          random_state=0)

    wordcloud.generate(corpus)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.figure()

    return wordcloud


# Generate the Word Clouds for each of the Corpuses and save them as a PNG file
generateWordCloud(corpus=lyrics, cmap='viridis').to_file('wc_1.png')
