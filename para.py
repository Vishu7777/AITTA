fp=open('para.txt','r')
buffer=fp.read()
text=buffer.split('.')
for i in text:
    print(i)
fp.close()
