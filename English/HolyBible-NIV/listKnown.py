numOfSamples = 3
sampleDir = 'volcabulary/samples/'

symbol = ' ,.?-():"\\\'[];`~!@#$%^&*_+{}<>/=0123456789'

def containSymbol(word):
    for c in word:
        if c in symbol:
            return True
    return False

allWords = set()
for i in range(numOfSamples):
    sampleFileName = sampleDir+'sample'+str(i).zfill(2)+'.txt'
    print 'loading ' + sampleFileName
    f = open(sampleFileName, 'r')
    content = f.read()
    f.close()
    words = content.split()
    for word in words:
        word = word.strip(symbol)
        word = word.lower()
        if len(word)<3 or word.isdigit():
            continue
        elif containSymbol(word):
            continue
        else:
            if word in allWords:
                continue
            else:
                allWords.add(word)

print sorted(allWords)

f = open('volcabulary/Samples.txt', 'w')
for word in sorted(allWords):
    f.write(word + ' ')
f.close()


