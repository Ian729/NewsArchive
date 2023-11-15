import feedparser
from wordcloud import WordCloud
# World News
ents = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/World.xml").entries
words = ""
for ent in ents:
    words += ent.get("content", [{}])[0].get('value', "")
wordcloud = WordCloud(width=800, height=400).generate(words)
wordcloud.to_file("image.png")

# US News
ents = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/US.xml").entries
words = ""
for ent in ents:
    words += ent.get("content", [{}])[0].get('value', "")
wordcloud = WordCloud(width=800, height=400).generate(words)
wordcloud.to_file("usnews.png")

# Asian News
ents = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml").entries
words = ""
for ent in ents:
    words += ent.get("content", [{}])[0].get('value', "")
wordcloud = WordCloud(width=800, height=400).generate(words)
wordcloud.to_file("asia.png")

print("Done!")