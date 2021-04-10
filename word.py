fp=open('para.txt','r')
for line in fp:
    word=line.split(' ')
    print(word)
fp.close()
