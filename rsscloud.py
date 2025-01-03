import feedparser
from translate import Translator

T = Translator(to_lang="zh")
# Global News
ents = feedparser.parse(
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
).entries
global_news = ""
for ent in ents[:10]:
    global_news += "* "
    current = ent.get("summary", "")
    global_news += current
    global_news += "\n"
    global_news += "* "
    trans = T.translate(current)
    global_news += trans
    global_news += "\n"


# US News
ents = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/US.xml").entries
us_news = ""
for ent in ents[:10]:
    us_news += "* "
    current = ent.get("summary", "")
    us_news += current
    us_news += "\n"
    us_news += "* "
    trans = T.translate(current)
    us_news += trans
    us_news += "\n"


# Asian News
ents = feedparser.parse(
    "https://rss.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml"
).entries
asian_news = ""
for ent in ents[:10]:
    asian_news += "* "
    current = ent.get("summary", "")
    asian_news += current
    asian_news += "\n"
    asian_news += "* "
    asian_news += T.translate(current)
    asian_news += "\n"

md = open("./README.md", "w")
md.write("# NewsArchive\n")
md.write("Auto RSS New York Times and Translate\n")
md.write("\n")
md.write("## New York Times Global News\n")
md.write(global_news)
md.write("\n")
md.write("## New York Times United States News\n")
md.write(us_news)
md.write("\n")
md.write("## New York Times Asia News\n")
md.write(asian_news)
md.write("\n")

print("Done!")
