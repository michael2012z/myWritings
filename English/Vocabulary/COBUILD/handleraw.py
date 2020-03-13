# -*- coding: utf-8 -*-

f_in_prefix = 'cobuild-'
f_in_suffix = '-star.txt'
f_out_prefix = 'frequency-level-'
f_out_suffix = '.txt'
for i in range(5, 2, -1):
    f_in = open(f_in_prefix + str(i) + f_in_suffix, 'rt', encoding="utf-8")
    f_out = open(f_out_prefix + str(i) + f_out_suffix, 'wt')
    lines = f_in.read()
    lines = lines.split('\n')
    for line in lines:
        if len(line) == 0:
            continue
        word = line[:line.find('[')]
        print(word)
        f_out.write(word+'\n')
    f_in.close()
    f_out.close()
	
for i in range(2, 0, -1):
    f_in = open(f_in_prefix + str(i) + f_in_suffix, 'rt', encoding="utf-8")
    f_out = open(f_out_prefix + str(i) + f_out_suffix, 'wt')
    lines = f_in.read()
    lines = lines.split('\n')
    for line in lines:
        if len(line) < 2:
            continue
        word = line
        print(word)
        f_out.write(word+'\n')
    f_in.close()
    f_out.close()
	