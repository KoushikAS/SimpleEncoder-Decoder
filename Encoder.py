def noOfParityBits(n):
    i=0
    while 2.**i <= n+i: 
        i+=1
    return i

def appendParityBits(data):
    n=noOfParityBits(len(data))
    i=0 
    j=0 
    k=0 
    msg=list()
    while i <n+len(data):
        if i== (2.**j -1):
            msg.insert(i,'0')
            j+=1
        else:
            msg.insert(i,data[k])
            k+=1
        i+=1
    return msg

def hammingCodes(data):
    n=noOfParityBits(len(data))
    list1=appendParityBits(data) 
    i=0 
    k=1 
    while i<n:
        k=2.**i
        j=1
        total=0
        while j*k -1 <len(list1):
            if j*k -1 == len(list1)-1: 
                lower=j*k -1
                temp=list1[int(lower):len(list1)]
            elif (j+1)*k -1>=len(list1):
                lower=j*k -1
                temp=list1[int(lower):len(list1)]
            elif (j+1)*k -1<len(list1)-1:
                lower=(j*k)-1
                upper=(j+1)*k -1
                temp=list1[int(lower):int(upper)]

            for x in temp:
                total=total+int(x)
            
            j+=2
        if total%2 >0:
            list1[int(k)-1]='1' 
            
        i+=1
    return list1

fp=open('input.txt','r') 
fp1=open('encoded.txt','wb')

msg=fp.read()
print("input is "+msg)
msg_b=' '.join(format(ord(x), 'b') for x in msg)
print(msg_b)
msg_b=msg_b.split()

msg_h=[]
for x in msg_b:
    res=hammingCodes(x)
    res=''.join(res)
    msg_h.append(res)
    

msg_h=' '.join(msg_h)
print("encoded msg is "+msg_h)

fp1.write(msg_h.encode('utf-8')) 
fp.close()
fp1.close()
