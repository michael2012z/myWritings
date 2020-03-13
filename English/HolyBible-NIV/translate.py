# -*- coding:utf-8 -*-  
import urllib
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

f = open("volcabulary/Learnt.txt", 'r')
wordList = f.read()
wordList = wordList.split()
f.close()
#print wordList

translationList = []
print "translating "

for word in wordList:
    try:
        print word,
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
        translationList.append((word, target["translateResult"][0][0]['tgt'], target["smartResult"]['entries']))
    except Exception, e:
        print 'not found'

f = open('volcabulary/Translation.txt', 'w')
for translation in translationList:
    s = translation[0] + " || " + translation[1] + " || " 
    for m in translation[2]:
        if m.strip() <> '':
            s += m + '; '
    print s
    f.write(s+'\n')
f.close()

