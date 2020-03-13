import urllib
import json
import sys
from HTMLParser import HTMLParser
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

reload(sys)
sys.setdefaultencoding('utf-8')

bibleData = []
allWords = []
translationDic = {}
unknownWordStemSet = set()
nameSet = set()

bookShortNameList = {
    "ge": "Genesis",
    "ex": "Exodus",
    "lev": "Leviticus",
    "nu": "Numbers",
    "dt": "Deuteronomy",
    "jos": "Joshua",
    "jdg": "Judges",
    "ru": "Ruth",
    "1sa": "1 Samuel",
    "2sa": "2 Samuel",
    "1ki": "1 Kings",
    "2ki": "2 Kings",
    "1ch": "1 Chronicles",
    "2ch": "2 Chronicles",
    "ezr": "Ezra",
    "ne": "Nehemiah",
    "est": "Esther",
    "job": "Job",
    "ps": "Psalms",
    "pr": "Proverbs",
    "ecc": "Ecclesiastes",
    "ss": "Song of Songs",
    "isa": "Isaiah",
    "jer": "Jeremiah",
    "la": "Lamentations",
    "eze": "Ezekiel",
    "da": "Daniel",
    "hos": "Hosea",
    "joel": "Joel",
    "am": "Amos",
    "ob": "Obadiah",
    "jnh": "Jonah",
    "mic": "Micah",
    "na": "Nahum",
    "hab": "Habakkuk",
    "zep": "Zephaniah",
    "hag": "Haggai",
    "zec": "Zechariah",
    "mal": "Malachi",
    "mt": "Matthew",
    "mk": "Mark",
    "lk": "Luke",
    "jn": "John",
    "ac": "Acts",
    "ro": "Romans",
    "1co": "1 Corinthians",
    "2co": "2 Corinthians",
    "gal": "Galatians",
    "eph": "Ephesians",
    "php": "Philippians",
    "col": "Colossians",
    "1th": "1 Thessalonians",
    "2th": "2 Thessalonians",
    "1ti": "1 Timothy",
    "2ti": "2 Timothy",
    "tit": "Titus",
    "phm": "Philemon",
    "heb": "Hebrews",
    "jas": "James",
    "1pe": "1 Peter",
    "2pe": "2 Peter",
    "1jn": "1 John",
    "2jn": "2 John",
    "3jn": "3 John",
    "jude": "Jude",
    "rev": "Revelation",
}

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


englishStopwords = stopwords.words('english')
stemmer = PorterStemmer()

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
    lemmatizer = None
    symbol = ' ,.?-():"\\\'[];`~!@#$%^&*_+{}<>/=0123456789'

    def __init__(self):
        HTMLParser.__init__(self)
        self.lemmatizer = WordNetLemmatizer()

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

        
    def containSymbol(self, word):
        for c in word:
            if c in self.symbol:
                return True
        return False

    def splitLine(self, line):
        lineWords = word_tokenize(line)
        filteredLineWords = []
        for word in lineWords:
            word = word.strip(self.symbol)
            if len(word)<3 or self.containSymbol(word):
                    continue
            else:
                if word in filteredLineWords:
                    continue
                else:
                    filteredLineWords.append(word)
        return filteredLineWords
        
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
            lineWords = self.splitLine(self.currentLine)
            lineWords = list(set(lineWords) - set(englishStopwords))
            self.currentChapter.append((self.currentLine, lineWords))

    def getFormattedText(self):
        return self.bookData


def loadBooks():
    print "loading books ..."
    i = 0
    for book in bookList:
        i += 1
        if i == 3:
            print ".",
            i = 0
        fileName = 'filtered_pages/'+ htmlLinks[book]
        f = open(fileName, 'r')
        html = f.read()
        f.close()
        parser = BibleBookParser()
        parser.parse(html)
        bookData = parser.getFormattedText()
        bibleData.append(bookData)
    print ""

def loadVolcabulary():
    global unknownWordStemSet
    global nameSet
    print "loading volcabulary ..."
    allWordList = buildAllWordList()
    allWordSet = buildAllWordSet(allWordList)
    nameSet = buildNameSet(allWordSet)
    pureWordList = buildPureWordList(allWordList, nameSet)
    pureWordSet = buildPureWordSet(pureWordList)
    unknownWordStemSet = buildUnknownWordStemSet(pureWordSet)
    #print unknownWordStemSet
    #print len(unknownWordStemSet)


def loadTranslation():
    f = open("volcabulary/Translation.txt", 'r')
    translationList = f.read()
    f.close()
    translationList = translationList.split('\n')
    for translation in translationList:
        if translation.find(' ::: ') < 0:
            continue
        k, v = translation.split(' ::: ')
        translationDic[k.lower()] = v

    
def searchInBook(targetWord, targetBook, chapterNo=0):
    bookShortNames = bookShortNameList.keys()
    if not targetBook in bookShortNames:
        print '"' + targetBook + '" is not a valid book name'
        return
    print "searching " + targetWord + ' in ' + targetBook
    bookFullName = bookShortNameList[targetBook]
    targetWord = targetWord.lower()
    for bookData in bibleData:
        if bookFullName == bookData[0]:
            for i in range(1, len(bookData)):
                if chapterNo == 0 or chapterNo == i:
                    chapterData = bookData[i]
                    for j in range(1, len(chapterData)):
                        line = chapterData[j]
                        lineText = line[0]
                        lineWords = line[1]
                        lineWordsLower = []
                        for word in lineWords:
                            lineWordsLower.append(word.lower())
                        lineWordsSet = set(lineWordsLower)
                        if targetWord in lineWordsSet:
                            print chapterData[0] + ': ' + str(j) + '. ' + lineText.replace(targetWord, '\033[91m'+targetWord+'\033[0m')
        
def searchInAllBooks(targetWord):
    bookShortNames = bookShortNameList.keys()
    for targetBook in bookShortNames:
        searchInBook(targetWord, targetBook)

class WordCounter(dict):
    def __missing__(self, key):
        return 0

def listUnknownInBook(targetBook, chapterNo=0):
    bookShortNames = bookShortNameList.keys()
    if not targetBook in bookShortNames:
        print '"' + targetBook + '" is not a valid book name'
        return
    print "searching " + targetBook
    bookFullName = bookShortNameList[targetBook]
    bookUnknownWords = WordCounter()
    for bookData in bibleData:
        if bookFullName == bookData[0]:
            for i in range(1, len(bookData)):
                if chapterNo == 0 or chapterNo == i:
                    chapterData = bookData[i]
                    for j in range(1, len(chapterData)):
                        lineWords = chapterData[j][1]
                        for word in lineWords:
                            if not word in nameSet and \
                               stemmer.stem(word).lower() in unknownWordStemSet:
                                bookUnknownWords[word.lower()] += 1
    bookUnknownWordList = sorted(bookUnknownWords.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
#    for word in bookUnknownWordList:
#        print word[0] + ' : ' + str(word[1]),
#    print ''
    return bookUnknownWords

def listUnknownInAllBooks():
    allUnknownWords = WordCounter()
    bookShortNames = bookShortNameList.keys()
    for book in bookShortNames:
        bookUnknownWords = listUnknownInBook(book)
        for (key, value) in bookUnknownWords.items():
            allUnknownWords[key] += value
    allUnknownWordList = sorted(allUnknownWords.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
    for word in allUnknownWordList:
        print word[0] + ' : ' + str(word[1]),
    print ''
    return allUnknownWords

def printBook(targetBook, chapterNo=0):
    bookShortNames = bookShortNameList.keys()
    if not targetBook in bookShortNames:
        print '"' + targetBook + '" is not a valid book name'
        return
    print "printing " + targetBook
    bookFullName = bookShortNameList[targetBook]
    for bookData in bibleData:
        if bookFullName == bookData[0]:
            for i in range(1, len(bookData)):
                if chapterNo == 0 or chapterNo == i:
                    chapterData = bookData[i]
                    for j in range(1, len(chapterData)):
                        print str(j) + '. ' + chapterData[j][0]
    print ''

def translateWord(words):
    # tmp use
    translationDic = {}
    for word in words:
        print word + ": "
        word = word.lower()
        if word in translationDic.keys():
            print translationDic[word]
        else:
            try:
                url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'
                data = {}
                data['type'] = 'AUTO'
                data['i'] = word
                data['doctype'] = 'json'
                data['xmlVersion'] = '1.6'
                data['keyfrom'] = 'fanyi.web'
                data['ue'] = 'UTF-8'
                data['typoResult'] = 'true'
                data = urllib.urlencode(data)
                response = urllib.urlopen(url, data)
                html = response.read()
                target = json.loads(html)
                result = target["translateResult"][0][0]['tgt']
                print result
                result = target["smartResult"]['entries']
                for l in result:
                    if l.strip() <> '':
                        print l
            except Exception, e:
                print 'not found'


def buildAllWordList():
    allWordList = []
    for bookData in bibleData:
        for i in range(1, len(bookData)):
            chapterData = bookData[i]
            for j in range(1, len(chapterData)):
                allWordList.extend(chapterData[j][1])
    return allWordList
    
def buildAllWordSet(allWordList):
    return set(allWordList)
                
def buildNameSet(allWordSet):
    nameSet = set()
    for word in list(allWordSet):
        if word.istitle() and not (word.lower() in allWordSet):
            nameSet.add(word)
    return nameSet

def buildPureWordList(allWordList, nameSet):
    pureWordList = []
    for w in allWordList:
        if not w in nameSet:
            pureWordList.append(w.lower())
    return pureWordList

def buildPureWordSet(pureWordList):
    return set(pureWordList)

def buildUnknownWordStemSet(pureWordSet):
    knownWordsFile = open('volcabulary/KnownEnglishWords.txt')
    knownWords = knownWordsFile.read()
    knownWords = knownWords.split('\r\n')
    knownWordSet = set()
    for w in knownWords:
        knownWordSet.add(stemmer.stem(w).lower())
    #print knownWordSet
    unknownWordSet = set()
    for w in pureWordSet:
        if not stemmer.stem(w) in knownWordSet:
            unknownWordSet.add(w)
    return unknownWordSet
        
def printStatistics():
    allWordList = buildAllWordList()
    allWordSet = buildAllWordSet(allWordList)
    nameSet = buildNameSet(allWordSet)
    pureWordList = buildPureWordList(allWordList, nameSet)
    pureWordSet = buildPureWordSet(pureWordList)
    unknownWordSet = buildUnknownWordSet(pureWordSet)
    print unknownWordSet
    print len(unknownWordSet)
#    freq = nltk.FreqDist(pureWordList)
#    for key,val in freq.items():
#        print (str(key) + ':' + str(val))
#    print bibleData[0]
#    print len(bibleData)


import pygame

def audioPlay(targetBook, chapter):
    bookShortNames = bookShortNameList.keys()
    if not targetBook in bookShortNames:
        print '"' + targetBook + '" is not a valid book name'
        return
    bookFullName = bookShortNameList[targetBook]
    print "play " + bookFullName + " " + str(chapter)
    audioFileName = 'audio/' + bookFullName + '/' + bookFullName + ' ' + str(chapter).zfill(2) + '.mp3'
    pygame.mixer.init()
    track = pygame.mixer.music.load(audioFileName)
    pygame.mixer.music.play()
 
def audioPause():
    pygame.mixer.music.pause()

def audioResume():
    pygame.mixer.music.unpause()

def audioStop():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()


loadBooks()
loadVolcabulary()
loadTranslation()
# command loop
while(True):
    cmdInput = raw_input('input: ')
    cmdInput = cmdInput.split()
    if len(cmdInput) == 0 :
        continue
    if (cmdInput[0] in ('h', 'help')):
        print 'i - statistics of Holy Bible words'
        print 'u in <book> [chapter] - list Unknown words in a book'
        print 's <word> in <book> - Search a word in a book'
        print 's <word> - Search a word in all books'
        print 't <word> - Translate a word'
        print 'p <book> [chapter] - Print a book'
        print 'a pl <book> [chapter] - Play audio'
        print 'a pa - Pause audio'
        print 'a re - Resume audio'
        print 'a st - Stop audio'
        print 'q - quit'
        print 'book list: \n Old Testament:\n"ge": "Genesis", "ex": "Exodus", "lev": "Leviticus", "nu": "Numbers", "dt": "Deuteronomy", "jos": "Joshua", "jdg": "Judges", "ru": "Ruth", "1sa": "1 Samuel", "2sa": "2 Samuel", "1ki": "1 Kings", "2ki": "2 Kings", "1ch": "1 Chronicles", "2ch": "2 Chronicles", "ezr": "Ezra", "ne": "Nehemiah", "est": "Esther", "job": "Job", "ps": "Psalms", "pr": "Proverbs", "ecc": "Ecclesiastes", "ss": "Song of Songs", "isa": "Isaiah", "jer": "Jeremiah", "la": "Lamentations", "eze": "Ezekiel", "da": "Daniel", "hos": "Hosea", "joel": "Joel", "am": "Amos", "ob": "Obadiah", "jnh": "Jonah", "mic": "Micah", "na": "Nahum", "hab": "Habakkuk", "zep": "Zephaniah", "hag": "Haggai", "zec": "Zechariah", "mal": "Malachi"\n New Testament:\n"mt": "Matthew", "mk": "Mark", "lk": "Luke", "jn": "John", "ac": "Acts", "ro": "Romans", "1co": "1 Corinthians", "2co": "2 Corinthians", "gal": "Galatians", "eph": "Ephesians", "php": "Philippians", "col": "Colossians", "1th": "1 Thessalonians", "2th": "2 Thessalonians", "1ti": "1 Timothy", "2ti": "2 Timothy", "tit": "Titus", "phm": "Philemon", "heb": "Hebrews", "jas": "James", "1pe": "1 Peter", "2pe": "2 Peter", "1jn": "1 John", "2jn": "2 John", "3jn": "3 John", "jude": "Jude", "rev": "Revelation"'
    elif (cmdInput[0] == 'i'):
        if len(cmdInput) == 1:
            # printStatistics()
            listUnknownInAllBooks()
        else:
            print 'wrong command'
    elif (cmdInput[0] == 'u'):
        if len(cmdInput) == 3 and cmdInput[1] == 'in':
            listUnknownInBook(cmdInput[2])
        elif len(cmdInput) == 4 and cmdInput[1] == 'in' and cmdInput[3].isdigit():
            listUnknownInBook(cmdInput[2], int(cmdInput[3]))
        else:
            print 'wrong command'
    elif (cmdInput[0] == 'p'):
        if len(cmdInput) == 2:
            printBook(cmdInput[1])
        elif len(cmdInput) == 3 and cmdInput[2].isdigit():
            printBook(cmdInput[1], int(cmdInput[2]))
        else:
            print 'wrong command'
    elif (cmdInput[0] == 'a'):
        if cmdInput[1] in set(['pl', 'p']) and len(cmdInput) == 4:
            audioPlay(cmdInput[2], int(cmdInput[3]))
        elif cmdInput[1] in set(['pa', 'a']):
            audioPause()
        elif cmdInput[1] in set(['re', 'r']):
            audioResume()
        elif cmdInput[1] in set(['st', 's']):
            audioStop()
        else:
            print 'wrong command'
    elif (cmdInput[0] == 't'):
        if len(cmdInput) > 1:
            translateWord(cmdInput[1:])
        else:
            print 'wrong command'
    elif (cmdInput[0] == 's'):
        if len(cmdInput) == 2:
            searchInAllBooks(cmdInput[1])
        elif len(cmdInput) == 4 and cmdInput[2] == 'in':
            searchInBook(cmdInput[1], cmdInput[3])
        elif len(cmdInput) == 5 and cmdInput[2] == 'in':
            searchInBook(cmdInput[1], cmdInput[3], int(cmdInput[4]))
        else:
            print 'wrong command'
    elif (cmdInput[0] == 'q'):
        break
    else:
        print 'unknown command'
    
 
