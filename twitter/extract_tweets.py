import codecs
import html5lib

f = codecs.open("anna_kavan.html", "r", "utf-8")
html = f.read()

parser = html5lib.HTMLParser(tree=html5lib.treebuilders.getTreeBuilder("lxml"), namespaceHTMLElements=False)
tree = parser.parse(html, encoding=None, parseMeta=True, useChardet=True)

tweets = []

for elt in tree.xpath('//li[@data-item-type="tweet"]'):
    fullname = elt.xpath('.//strong[@class="fullname js-action-profile-name show-popup-with-id"]')[0].text
    username_elt = elt.xpath('.//span[@class="username js-action-profile-name"]')[0]
    username = [i for i in username_elt.itertext()][-1]
    tweet_elt = elt.xpath('.//p[@class="js-tweet-text tweet-text"]')[0]
    tweet = "".join([i for i in tweet_elt.itertext()])
    date_elt = elt.xpath('.//span[@data-time-ms]')[0]
    timestamp = int(date_elt.attrib['data-time-ms'])

    tweets.append({
        "fullname": fullname,
        "username": username,
        "timestamp": timestamp,
        "tweet": tweet
    })
    #print(fullname)
    #print(username)
    #print(timestamp)
    #print(tweet.encode('utf-8'))

print(tweets)


#nom
#id
#date
#texte
#image

