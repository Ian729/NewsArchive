import feedparser
from wordcloud import WordCloud
# Global News
ents = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/World.xml").entries
global_news = ""
for ent in ents[:10]:
    global_news += "* "
    global_news += ent.get("summary","")
    global_news += "\n"
wordcloud = WordCloud(width=800, height=400).generate(global_news)
wordcloud.to_file("global.png")

# US News
ents = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/US.xml").entries
us_news = ""
for ent in ents[:10]:
    us_news += "* "
    us_news += ent.get("summary","")
    us_news += "\n"
wordcloud = WordCloud(width=800, height=400).generate(us_news)
wordcloud.to_file("usnews.png")

# Asian News
ents = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml").entries
asian_news = ""
for ent in ents[:10]:
    asian_news += "* "
    asian_news += ent.get("summary","")
    asian_news += "\n"
wordcloud = WordCloud(width=800, height=400).generate(asian_news)
wordcloud.to_file("asian.png")
print("update markdown file")

md = open("./README.md", 'w')
md.write("# NewsArchive\n")
md.write("Auto RSS New York Times and Generate Word Cloud\n")
md.write("\n")
md.write("## New York Times Global News\n")
md.write(global_news)
md.write("\n")
md.write("![Global](./global.png)")
md.write("\n")
md.write("## New York Times United States News\n")
md.write(us_news)
md.write("\n")
md.write("![US](./usnews.png)")
md.write("\n")
md.write("## New York Times Asia News\n")
md.write(asian_news)
md.write("\n")
md.write("![Asian](./asian.png)")
md.write("\n")

print("Done!")