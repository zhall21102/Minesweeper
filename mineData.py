def openData(dataset):
    out=[]
    f=open(dataset)
    data=f.read()
    data=data.split("\n")
    f.close()
    for game in data:
        if game!='':
            out=game.split('-')
            #print(out)
            print(interpret(out))
    return out

def interpret(data):
    total=0
    for e in range(len(data)):
        if data[e]=='0x9FC2E5' or data[e]=='0x99B8D7':
            total+=1
    if total!=0:
        return total



def clear(dataset):
    file = open(dataset,"w")
    file.truncate(0)
    file.close()

H='Harddata.txt'
M='Meddata.txt'
E='Easydata.txt'

openData(E)
clear(E)

#openData(M)
#clear(M)

#openData(H)
#clear(H)


#gray= 0x9FC2E5 and 0x99B8D7
#green= 0x51D7AA and 0x49D1A2
