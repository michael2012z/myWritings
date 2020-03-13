from HTMLParser import HTMLParser

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

class BibleChapterParser(HTMLParser):
    STATUS_INVALID = -1
    STATUS_BOOK = 0
    STATUS_CHAPTER = 1
    STATUS_SUBJECT = 2
    STATUS_INDEX = 3
    STATUS_TEXT = 4
    STATUS_SUP = 5
    filteredText = ''
    status = -1
    savedStatus = -1
    bookText = ''
    chapterText = ''
    subjectText = ''
    indexText = ''
    textText = ''
    supText = ''
    stopFlag = False
    def __init__(self):
        HTMLParser.__init__(self)
        self.filteredText = ''
        self.status = self.STATUS_INVALID
        self.savedStatus = self.STATUS_INVALID

    def parse(self, html):
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if self.stopFlag == True:
            return
        if tag == "title":
            self.status = self.STATUS_BOOK
        elif tag == "h2":
            self.status = self.STATUS_CHAPTER
        elif tag == "i":
            self.status = self.STATUS_SUBJECT
        elif tag == "dt":
            self.status = self.STATUS_INDEX
        elif tag == "dd":
            self.status = self.STATUS_TEXT
        elif tag == "sup":
            self.savedStatus = self.status
            self.status = self.STATUS_SUP
        else:
            self.status = self.STATUS_INVALID

    def handle_data(self, data):
        if self.stopFlag == True:
            return
        data = data.strip()
        if self.status == self.STATUS_BOOK:
            self.bookText +=  data
        elif self.status == self.STATUS_CHAPTER:
            self.chapterText += data
        elif self.status == self.STATUS_SUBJECT:
            self.subjectText += data
        elif self.status == self.STATUS_INDEX:
            self.indexText += data
        elif self.status == self.STATUS_TEXT:
            self.textText += data
        elif self.status == self.STATUS_SUP:
            self.supText += data
        return

    def handle_endtag(self, tag):
        if self.stopFlag == True:
            return
        if tag == "title" and self.bookText <> '':
            self.filteredText += '<book>' + self.bookText + '</book>\n'
            self.bookText = ''
        elif tag == "h2" and self.chapterText <> '':
            if self.chapterText == 'Footnotes':
                self.stopFlag = True
                return
            self.filteredText += '<c>' + self.chapterText + '</c>\n'
            self.chapterText = ''
        elif tag == "i" and self.subjectText <> '':
            self.filteredText += '<s>' + self.subjectText + '</s>\n'
            self.subjectText = ''
        elif tag == "dt" and self.indexText <> '':
            self.filteredText += '<i>' + self.indexText + '</i>'
            self.indexText = ''
        elif tag == "dd" and self.textText <> '':
            self.filteredText += '<t>' + self.textText + '</t>\n'
            self.textText = ''
        elif tag == "sup":
            self.status = self.savedStatus
            self.textText += ' '
            self.supText = ''

    def getFilteredText(self):
        return self.filteredText

for chapter in chapterList:
    print "handling " + chapter
    rawFileName = 'normalized_pages/'+ htmlLinks[chapter]
    f = open(rawFileName, 'r')
    rawText = f.read()
    f.close()
    parser = BibleChapterParser()
    parser.parse(rawText)
    filteredText = parser.getFilteredText()
    filteredFileName = 'filtered_pages/'+ htmlLinks[chapter]
    f = open(filteredFileName, 'w')
    f.write(filteredText)
    f.close()

