# -*- coding: utf-8 -*-
from HTMLParser import HTMLParser

#[
#    (root, root-meaning, unit, [word1, word2, ....]),
#    ...
#]

def loadMWVB():
    vocabulary = []
    f = open("Merriam-Webster's Vocabulary Builder.txt", 'rt')
    lines = f.read()
    # debug
    # lines += '\nUnit 31\nXXX: xxx\nequinox\nmeter\npolyphonic\nprocure\n'
    lines = lines.split('\n')[1:]
    unit = ''
    root = ''
    item = None
    for line in lines:
        if line.find("Unit ") == 0:
            unit = line[len("Unit "):]
        elif line.find(": ") > 0:
            root = line
            root = root.split(': ')
            item = (root[0], root[1], unit, [])
            vocabulary.append(item)
        else:
            word = line
            item[3].append(word)
    return vocabulary


class EnglishDictionary(HTMLParser):
    handling_eng_d = False
    handling_eng_dc = False
    handling_chn_d = False
    handling_eng_e = False
    handling_chn_e = False
    handling_cl = False
    handling_cf = False
    handling_phon = False
    handling_hw = False
    handling_dr = False
    text = ''
    phon = ''
    cf = ''
    hw = ''
    prefix = ''
    alt_list = []
    alt_word = ''
    alt_phon = ''
    in_dr_g = False
    dic = {}
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.html = None
        for i in range(ord('a'), ord('z')+1):
            self.dic[chr(i)] = []


    def clean(self):
        self.html = None
        self.handling_eng_d = False
        self.handling_eng_dc = False
        self.handling_chn_d = False
        self.handling_eng_e = False
        self.handling_chn_e = False
        self.handling_cl = False
        self.handling_cf = False
        self.handling_phon = False
        self.handling_hw = False
        self.handling_dr = False
        self.text = ''
        self.phon = ''
        self.hw = ''
        self.cf = ''
        self.prefix = ''
        self.alt_word = ''
        self.alt_phon = ''
        self.in_dr_g = False
        self.alt_list = []

    def preHandle(self, html):
        filteredHtml = html
        filteredHtml = filteredHtml.replace('<span class="bra">', '')
        filteredHtml = filteredHtml.replace('</span bra>', '')
        return filteredHtml
    
    def load(self):
        #f = open("tmp.xml")
        f = open("O7.xml")
        htmls = f.read()
        htmls = htmls.split('\n')
        for html in htmls:
            if html.find('\t<head>') < 0:
                continue
            word, html = html.split('\t<head>')
            html = self.preHandle(html)
            try:
                self.clean()
                self.feed(html)
                self.dic[word[0].lower()].append((word.strip(), self.hw.strip(), self.phon.strip(), self.text.strip(), self.alt_list))
            except Exception, e:
                e
                
    def handle_starttag(self,tag,attrs):
        if tag == 'div' and len(attrs) == 1 and attrs[0] == ('class', 'dr_g'):
            self.in_dr_g = True
        elif tag == 'span' and len(attrs) == 1 and attrs[0] == ('class', 'cl'):
            self.handling_cl = True
        elif tag == 'span' and len(attrs) == 1 and attrs[0] == ('class', 'dr'):
            self.handling_dr = True
        elif tag == 'span' and len(attrs) == 1 and attrs[0] == ('class', 'cf'):
            self.handling_cf = True
        elif tag == 'span' and len(attrs) == 1 and attrs[0] == ('class', 'd'):
            if len(self.text) != 0:
                self.prefix = '\n'
            self.handling_eng_d = True
        elif tag == 'span' and len(attrs) == 1 and attrs[0] == ('class', 'dc'):
            self.handling_eng_dc = True
        elif tag == 'span' and len(attrs) == 1 and attrs[0] == ('class', 'chn'):
            self.handling_chn_d = True
        elif tag == 'span' and len(attrs) == 1 and attrs[0] == ('class', 'sentence_eng'):
            self.prefix = '\n - '
            self.handling_eng_e = True
        elif tag == 'span' and len(attrs) == 1 and attrs[0] == ('class', 'sentence_chi'):
            self.prefix = '\n   '
            self.handling_chn_e = True
        elif tag == 'span' and len(attrs) == 1 and attrs[0] == ('class', 'hw'):
            self.handling_hw = True
        elif tag == 'a' and len(attrs) == 2 and attrs[0] == ('class', 'i_phon'):
            self.handling_phon = True

    def handle_endtag(self,tag):
        if tag == 'div' and self.in_dr_g == True:
            self.in_dr_g = False
            self.alt_list.append((self.alt_word, self.alt_phon))
        elif tag == 'span' and self.handling_cl == True:
            self.handling_cl = False
        elif tag == 'span' and self.handling_dr == True:
            self.handling_dr = False
        elif tag == 'span' and self.handling_cf == True:
            self.handling_cf = False
        elif tag == 'span' and self.handling_eng_d == True:
            self.handling_eng_d = False
        elif tag == 'span' and self.handling_eng_dc == True:
            self.handling_eng_dc = False
        elif tag == 'span' and self.handling_chn_d == True:
            self.handling_chn_d = False
        elif tag == 'span' and self.handling_eng_e == True:
            self.handling_eng_e = False
        elif tag == 'span' and self.handling_chn_e == True:
            self.handling_chn_e = False
        elif tag == 'span' and self.handling_hw == True:
            self.handling_hw = False
        elif tag == 'a' and self.handling_phon == True:
            self.handling_phon = False

            
    def handle_data(self, data):
        if len(data) != 0:
            self.text += self.prefix
            self.prefix = ''
            self.text += self.cf
            self.cf = ''
        if self.handling_eng_d:
            self.text += data
        elif self.handling_eng_dc:
            self.text += data
        elif self.handling_cl:
            self.text += data
        elif self.handling_cf:
            self.cf = data
        elif self.handling_chn_d:
            self.text += data
        elif self.handling_eng_e:
            self.text += data
        elif self.handling_chn_e:
            self.text += data
        elif self.handling_dr and self.in_dr_g:
            self.alt_word = data
        elif self.handling_phon:
            if self.in_dr_g == False:
                self.phon += '/' + data + '/ '
            else:
                self.alt_phon = '/' + data + '/ '
        elif self.handling_hw:
            self.hw += data 

            
    def translate (self, word):
        head = word[0].lower()
        if ord(head) < ord('a') or ord(head) > ord('z'):
            print 'wrong format'
        l = self.dic[head]
        for item in l:
            candidates = []
            candidates.append(item[0].lower())
            for alt in item[4]:
                candidates.append(alt[0].replace('∙', '').strip().lower())
            if word.lower() in candidates:
                return item
        return (None, '', '', None, [])

    def findByRoot (self, root):
        candidates = []
        head = root[0].lower()
        if ord(head) < ord('a') or ord(head) > ord('z'):
            print 'wrong format'
        for l in self.dic.values():
            for item in l:
                word = item[0]
                if word.find(root) >= 0:
                    candidates.append(word)
        return candidates


def printEntry(vocab, rootIndex):
    entry = vocab[rootIndex]
    print '\033[1;36m' + "index: " + str(rootIndex) + "/" + str(len(vocab))
    print "unit : " + entry[2]
    print "root : " + entry[0]
    print '\033[0m'
    for w in entry[3]:
        print '\033[1;32m  ' + w + '\033[0m'
        print

def adhocTranslation(w):
    word, hw, phon, text, alt_list = dic.translate(w)
    if word == None:
        text = "Not Found"
    else:
        hw = ' | ' + hw
    alt_text = ''
    for alt in alt_list:
        alt_text += '\033[1;32m' + ' | ' + alt[0] + '\033[0m' + '\033[1;35m' + alt[1] + '\033[0m'
    print '\033[1;32m' + w + hw + '\033[0m' + ' \033[1;35m' + phon + '\033[0m' + alt_text
    print '\033[1;33m' + text + '\033[0m'
    print

    
def printTranslation(vocab, rootIndex):
    entry = vocab[rootIndex]
    print '\033[1;36m' + "index: " + str(rootIndex) + "/" + str(len(vocab))
    print "unit : " + entry[2]
    print "root : " + entry[0] + " : " + entry[1]
    print '\033[0m'
    for w in entry[3]:
        adhocTranslation(w)

def printWordsWithRoot(root):
    words = dic.findByRoot(root)
    for word in words:
        start = word.find(root)
        end = start + len(root)
        print word[:start] + '\033[1;32m' + root + '\033[0m' + word[end:]
    
        
if __name__ == '__main__':
    print 'loading vocabulary ...'
    vocab = loadMWVB()

    print 'loading dictionary ...'
    dic = EnglishDictionary()
    dic.load()
    print 'dictionary ready'
    print
    
    quitCommand = False
    rootIndex = -1
    while quitCommand == False:
        commandLine = raw_input("> ").split(' ')
        command = commandLine[0]
        if command == "q":
            quitCommand = True
        elif command == "n":
            rootIndex += 1
            rootIndex %= len(vocab)
            printEntry(vocab, rootIndex)
        elif command == "p":
            rootIndex -= 1
            rootIndex %= len(vocab)
            printEntry(vocab, rootIndex)
        elif command == "t":
            rootIndex %= len(vocab)
            printTranslation(vocab, rootIndex)
        elif command == "c":
            rootIndex %= len(vocab)
            printEntry(vocab, rootIndex)
        elif command == "j":
            rootIndex += 10
            rootIndex %= len(vocab)
        elif command == "jj":
            rootIndex += 50
            rootIndex %= len(vocab)
        elif command == "h":
            print '\033[1;36m' + "n(ext), p(revious), t(ranslate), c(urrent), j(ump), jj(ump), a(dhoc), r(oot)"
            print '\033[0m'
        elif command == "a" and len(commandLine) == 2:
            adhocTranslation(commandLine[1])
        elif command == "r" and len(commandLine) == 2:
            printWordsWithRoot(commandLine[1])
        elif len(command) == 0:
            continue
        else:
            print '\033[1;36m' + "unknown command"
            print "try:\nn(ext), p(revious), t(ranslate), c(urrent), j(ump), jj(ump), a(dhoc)"
            print '\033[0m'

