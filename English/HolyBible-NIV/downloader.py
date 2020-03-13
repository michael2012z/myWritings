import urllib2

urlBase = 'http://www.tedmontgomery.com/bblovrvw/NIVBible/'

chapterList = [
    'Genesis', 
    'Exodus', 
    'Leviticus', 
    'Numbers', 
    'Deuteronomy', 
    'Joshua', 
    'Judges', 
    'Ruth', 
    '1 Samuel', 
    '2 Samuel', 
    '1 Kings', 
    '2 Kings', 
    '1 Chronicles', 
    '2 Chronicles', 
    'Ezra', 
    'Nehemiah', 
    'Esther', 
    'Job', 
    'Psalms', 
    'Proverbs', 
    'Ecclesiastes', 
    'Song of Songs', 
    'Isaiah', 
    'Jeremiah', 
    'Lamentations', 
    'Ezekiel', 
    'Daniel', 
    'Hosea', 
    'Joel', 
    'Amos', 
    'Obadiah', 
    'Jonah', 
    'Micah', 
    'Nahum', 
    'Habakkuk', 
    'Zephaniah', 
    'Haggai', 
    'Zechariah', 
    'Malachi', 
    'Matthew', 
    'Mark', 
    'Luke', 
    'John', 
    'Acts', 
    'Romans', 
    '1 Corinthians', 
    '2 Corinthians', 
    'Galatians', 
    'Ephesians', 
    'Philippians', 
    'Colossians', 
    '1 Thessalonians', 
    '2 Thessalonians', 
    '1 Timothy', 
    '2 Timothy', 
    'Titus', 
    'Philemon', 
    'Hebrews', 
    'James', 
    '1 Peter', 
    '2 Peter', 
    '1 John', 
    '2 John', 
    '3 John', 
    'Jude', 
    'Revelation',
]

htmlLinks = {
    'Genesis': 'Gen.html', 
    'Exodus': 'Exo.html', 
    'Leviticus': 'Lev.html', 
    'Numbers': 'Num.html', 
    'Deuteronomy': 'Deut.html', 
    'Joshua': 'Josh.html', 
    'Judges': 'Judg.html', 
    'Ruth': 'Ruth.html', 
    '1 Samuel': 'Sam_1.html', 
    '2 Samuel': 'Sam_2.html', 
    '1 Kings': 'Kng_1.html', 
    '2 Kings': 'Kng_2.html', 
    '1 Chronicles': 'Chr_1.html', 
    '2 Chronicles': 'Chr_2.html', 
    'Ezra': 'Ezra.html', 
    'Nehemiah': 'Neh.html', 
    'Esther': 'Esth.html', 
    'Job': 'Job.html', 
    'Psalms': 'Psalm.html', 
    'Proverbs': 'Prov.html', 
    'Ecclesiastes': 'Eccl.html', 
    'Song of Songs': 'Song.html', 
    'Isaiah': 'Isa.html', 
    'Jeremiah': 'Jer.html', 
    'Lamentations': 'Lam.html', 
    'Ezekiel': 'Ezek.html', 
    'Daniel': 'Dan.html', 
    'Hosea': 'Hosea.html', 
    'Joel': 'Joel.html', 
    'Amos': 'Amos.html', 
    'Obadiah': 'Obad.html', 
    'Jonah': 'Jonah.html', 
    'Micah': 'Micah.html', 
    'Nahum': 'Nahum.html', 
    'Habakkuk': 'Hab.html', 
    'Zephaniah': 'Zeph.html', 
    'Haggai': 'Hag.html', 
    'Zechariah': 'Zech.html', 
    'Malachi': 'Mal.html', 
    'Matthew': 'Matt.html', 
    'Mark': 'Mark.html', 
    'Luke': 'Luke.html', 
    'John': 'John.html', 
    'Acts': 'Acts.html', 
    'Romans': 'Rom.html', 
    '1 Corinthians': 'Cor_1.html', 
    '2 Corinthians': 'Cor_2.html', 
    'Galatians': 'Gal.html', 
    'Ephesians': 'Eph.html', 
    'Philippians': 'Phil.html', 
    'Colossians': 'Col.html', 
    '1 Thessalonians': 'Ths_1.html', 
    '2 Thessalonians': 'Ths_2.html', 
    '1 Timothy': 'Tim_1.html', 
    '2 Timothy': 'Tim_2.html', 
    'Titus': 'Titus.html', 
    'Philemon': 'Phmn.html', 
    'Hebrews': 'Heb.html', 
    'James': 'James.html', 
    '1 Peter': 'Pet_1.html', 
    '2 Peter': 'Pet_2.html', 
    '1 John': 'John_1.html', 
    '2 John': 'John_2.html', 
    '3 John': 'John_3.html', 
    'Jude': 'Jude.html', 
    'Revelation': 'Rev.html',
}

def downLoad(url):
    print "downloading file: " + url
    request = urllib2.Request(url)
    try:
        response = urllib2.urlopen(request)  
        downloaded = response.read()
    except Exception, e:
        print e
        downloaded = None
    return downloaded

for chapter in chapterList:
    fullUrl = urlBase + htmlLinks[chapter]
    t = downLoad(fullUrl)
    f = open('raw_pages/' + htmlLinks[chapter], 'w')
    f.write(t)
    f.close()
