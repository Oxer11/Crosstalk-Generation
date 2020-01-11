import os
import re
from tqdm import tqdm
import thulac

fout = open('crosstalk.txt', 'wb')
thu1 = thulac.thulac()

for fname in os.listdir('./data'):
    fin = open('./data/' + fname, 'rb')
    lst_line = None
    for line in fin:
        line = line.decode('gbk')
        line = line[line.find('：') + 1:].strip()
        line = ' '.join([x[0] for x in thu1.cut(line, text=False)]) + '\n'
        # pattern = re.compile('.')
        # line = ' '.join(pattern.findall(line)) + '\n'
        if lst_line is not None:
            fout.write(lst_line.encode('utf-8'))
            fout.write(line.encode('utf-8'))
            lst_line = None
        else:
            lst_line = line
