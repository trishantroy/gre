import urllib2
from timeit import timeit

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def getMnemonics(fw, line):
    word = line[:-1]
    word_length = len(word)
    if word_length > 1:
        #print word
        contents = urllib2.urlopen("https://mnemonicdictionary.com/?word=" + word).read()
        parsed_html = BeautifulSoup(contents, "html.parser")
        body = parsed_html.body
        meaning = body.find('div', attrs={'style':'padding-bottom:0px;'})
        if meaning is not None:
            meaning = meaning.text
        mnemonic = body.find('div', attrs={'class':'card-text'})
        if mnemonic is not None:
            mnemonic = mnemonic.text
        if meaning is not None and mnemonic is not None:
            card_content = meaning + mnemonic
            modified_card_content = card_content.replace("Definition ", "Definition ")
            #print modified_card_content.encode('ascii', 'ignore')
            fw.write(word + "\n")
            fw.write(modified_card_content.encode('ascii', 'ignore'))
            fw.write("$@#")
        else:
            print "manually add mnemonic for word " + word

fr = open("barrons800.txt", "r")
fw = open("barrons800_mnemonics2.txt", "w")
fw2 = open("barrons800_timings2.txt", "w")
lines = fr.readlines()

i = 0
for line in lines:
    fw2.write(line[:-1] + "\t-\t")
    try:
        fw2.write(str(timeit(lambda: getMnemonics(fw, line), number=1)) + "\n")
    except:
        print line
#    if i == 10:
#        break
    i += 1
    print i

fr.close()
fw.close()
fw2.close()

