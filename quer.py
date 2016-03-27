with open("topics.401-450.trec8","r") as myfile:
          data = myfile.read().replace('\n',' ')



data = data.split()

number = 0
for i in range(len(data)):
    if (data[i] == 'Number:'):
        number = data[i+1]
        number = int(number)
        break


b=[]
for i in data:
	i =i.replace(',',' ')
	i =i.replace('?',' ')
	i =i.replace("'",' ')
	i =i.replace('(',' ')
	i =i.replace(')',' ')
	i =i.replace('.',' ')
	i =i.replace(':',' ')
	i =i.replace('-',' ')
	i =i.replace('/',' ')
	i =i.replace('&',' ')
	i =i.replace('Description',' ')
	b.append(i)

data=[]
data=b
t= []
flag = False
temp =[]




for i in range(len(data)-2):

    if ( data[i] == '<title>'):
        flag = True


    if ( flag ):
        if (data[i+1]!='<desc>' and data[i+1]!="<narr>" and data[i+1]!='Narrative '):
            temp.append(data[i+1])
        #else :
            #temp.append(data[i+2])


    if ( data[i] == '< top>'):
        flag = False
        temp.remove(data[i])
        temp.remove(data[i+1])
       #temp.remove('Description:')
        t.append(temp)
        temp = []



result = []
f = open("narr_topics_451-450.txt","w")

f.write('<parameters>')
f.write('<index>/home/miltiadis/Desktop/Omada7</index>')
f.write('<rule>method:dirichlet,mu:1000</rule>')
f.write('<count>1000</count>')
f.write('<trecFormat>true</trecFormat>')
for i in t:
    result.append(' '.join(i))
    a = '<query>' + '<type>' + 'indri' + '</type>'  +'<number>'+str(number)+ '</number>' +'<text>' + ' '.join(i)+ '</text>' +'</query>' + '\n'
    f.write(a)
    number +=1

f.write('</parameters>')
f.close
