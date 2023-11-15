import feedparser
from wordcloud import WordCloud
ents = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/World.xml").entries
words = ""
for ent in ents:
    words += ent.get("content", [{}])[0].get('value', "")
# Construct the word cloud
wordcloud = WordCloud(width=800, height=400).generate(words)
wordcloud.to_file("image.png")
print("Done!")