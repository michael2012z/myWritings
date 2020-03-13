# -*- coding: utf-8 -*-
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

#coding:utf-8    

d = "C:\\Users\\efengzh\\Downloads\\"
fsim = d + "han_sim.txt"
ftra = d + "han_tra.txt"
fsimin = open(fsim, "r", encoding="utf-8")
simin_text = fsimin.read()
ftrain = open(ftra, "r", encoding="utf-8")
train_text = ftrain.read()
simlines = simin_text.split('\n')
tralines = train_text.split('\n')

fboth = d + "han_both.txt"
fbothout = open(fboth, "w", encoding="utf-8")

for j in range(0, 3):
    fbothout.write(tralines[j*2]+'\n')
    print(tralines[j*2]+'\n')
    s = ''
    for i in range(0, len(tralines[j*2 + 1])):
        if simlines[j*2+1][i] != tralines[j*2+1][i]:
            s += simlines[j*2+1][i]
            s += tralines[j*2+1][i]
    fbothout.write(s+'\n')
    print(s+'\n')

fbothout.close()
