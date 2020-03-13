from HTMLParser import HTMLParser

bookList = [
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


class BibleBookParser(HTMLParser):
    STATUS_INVALID = -1
    STATUS_BOOK = 0
    STATUS_CHAPTER = 1
    STATUS_SUBJECT = 2
    STATUS_INDEX = 3
    STATUS_TEXT = 4
    status = -1
    bookText = ''
    chapterText = ''
    subjectText = ''
    indexText = ''
    textText = ''
    bookData = []
    currentChapter = None
    currentLine = ''

    def __init__(self):
        HTMLParser.__init__(self)

    def parse(self, html):
        self.status = -1
        self.bookText = ''
        self.chapterText = ''
        self.subjectText = ''
        self.indexText = ''
        self.textText = ''
        self.bookData = []
        self.currentChapter = None
        self.currentLine = ''
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag == "book":
            self.status = self.STATUS_BOOK
        elif tag == "c":
            self.status = self.STATUS_CHAPTER
        elif tag == "s":
            self.status = self.STATUS_SUBJECT
        elif tag == "i":
            self.status = self.STATUS_INDEX
        elif tag == "t":
            self.status = self.STATUS_TEXT
        else:
            self.status = self.STATUS_INVALID
        return

    def handle_data(self, data):
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
        if tag == "book":
            self.bookData.append(self.bookText)
            self.bookText = ''
        elif tag == "c":
            self.currentChapter = []
            self.currentChapter.append(self.chapterText)
            self.bookData.append(self.currentChapter)
            self.chapterText = ''
        elif tag == "s":
            self.subjectText = ''
        elif tag == "i":
            #self.currentLine = self.indexText + '. '
            self.currentLine = ''
            self.indexText = ''
        elif tag == "t":
            self.currentLine += self.textText
            self.textText = ''
            self.currentChapter.append(self.currentLine)

    def getFormattedText(self):
        return self.bookData


bibleData = []
allBookWords = {}
allWords = []

for book in bookList:
    print "loading " + book
    fileName = 'filtered_pages/'+ htmlLinks[book]
    f = open(fileName, 'r')
    html = f.read()
    f.close()
    parser = BibleBookParser()
    parser.parse(html)
    bookData = parser.getFormattedText()
    bibleData.append(bookData)

symbol = ' ,.?-():"\\\'[];`~!@#$%^&*_+{}<>/=0123456789'

def containSymbol(word):
    for c in word:
        if c in symbol:
            return True
    return False

for bookData in bibleData:
    print "parsing " + bookData[0]
    bookWords = []
    for i in range(1, len(bookData)):
        chapterData = bookData[i]
        for line in chapterData:
            lineWords = line.split();
            for word in lineWords:
                word = word.strip(symbol)
                #word = word.lower()
                if len(word)<3 or word.isdigit():
                    continue
                elif containSymbol(word):
                    continue
                else:
                    if word in bookWords:
                        continue
                    else:
                        bookWords.append(word)
    allBookWords[bookData[0]] = bookWords


for bookData in bibleData:
    print "checking words in " + bookData[0]
    bookWords = allBookWords[bookData[0]]
    for word in bookWords:
        if word in allWords:
            continue
        else:
            allWords.append(word)

# recognize names
allNameList = []
allNormalList = []
for word in allWords:
    if (word[0].isupper()) and (not (word.lower() in allWords)):
        allNameList.append(word)
    else:
        allNormalList.append(word.lower())

allNameList = list(set(allNameList))        
allNormalList = list(set(allNormalList))

postFixes = [
    ['s', ''],
    ['es', ''],
    ['ed', 'e'],
    ['ed', ''],
    ['ly', ''],
    ['ing', ''],
    ['ings', ''],
    ['ing', 'e'],
    ['ings', 'e'],
    ['tion', 'te'],
    ['tion', 't'],
    ['ness', ''],
    ['er', ''],
    ['ers', ''],
    ['est', ''],
    ['er', 'e'],
    ['ers', 'e'],
    ['est', 'e'],
    ['able', ''],
    ['ably', ''],
    ['ful', ''],
]

allNormalSet = set(allNormalList)
allOriginalSet = set()
duplicates = dict()

for word in allNormalSet:
    for post in postFixes:
        if (len(word) > len(post[0])) and (word[-len(post[0]):] == post[0]) and ((word[:-len(post[0])] + post[1]) in allNormalSet):
            baseWord = (word[:-len(post[0])] + post[1])
            if baseWord not in duplicates:
                duplicates[baseWord] = set()
            duplicates[baseWord].add(word)
            break
    else:
        allOriginalSet.add(word)

allOriginalSet = sorted(allOriginalSet)

#allNameList.sort()
#print allNameList
#print len(allNameList)
#print '*' * 32
#allNormalList.sort()
#print allOriginalSet
#print len(allOriginalSet)
#print '*' * 32

f = open('volcabulary/Names.txt', 'w')
for word in allNameList:
    f.write(word+'\n')
f.close()
f = open('volcabulary/AllWords.txt', 'w')
for word in allOriginalSet:
    f.write(word+'\n')
f.close()
f = open('volcabulary/Duplicates.txt', 'w')
for duplicate in sorted(duplicates.keys()):
    f.write(duplicate + " : ")
    for w in duplicates[duplicate]:
        f.write(w + ", ")
    f.write("\n")
f.close()


f = open('volcabulary/Samples.txt', 'r')
sampleWords = f.read()
f.close()
sampleWords = sampleWords.split()
sampleWords = set(sampleWords)

knownWords = set()
unknownWords = set()
for word in allOriginalSet:
    if word in sampleWords:
        knownWords.add(word)
    else:
        unknownWords.add(word)

f = open('volcabulary/Known.txt', 'w')
for word in sorted(knownWords):
    f.write(word+"\n")
f.close()

f = open('volcabulary/Unknown.txt', 'w')
for word in sorted(unknownWords):
    f.write(word+"\n")
f.close()


print 'known words: ' + str(len(knownWords))
print 'unknown words: ' + str(len(unknownWords))
