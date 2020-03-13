
l = ['equinox', 'meter', 'polyphonic', 'procure', 'portfolio', 'moribund', 'motify', 'motification']

f = open("O7.xml")
htmls = f.read()
htmls = htmls.split('\n')
ff = open("O7t.xml", 'w')
for html in htmls:
    if html.find('\t<head>') < 0:
        continue
    word, text = html.split('\t<head>')
    if (word in l):
        ff.write(html + "\n")

