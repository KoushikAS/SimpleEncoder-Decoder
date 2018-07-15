def noOfParityBitsInCode(n):
    i=0
    while 2.**i <= n:
        i+=1
    return i

def hammingCorrection(data):
    n=noOfParityBitsInCode(len(data))
    i=0
    list1=list(data)
    
    error=0
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

            total=total+sum(int(e) for e in temp)

            j+=2 
        
        if total%2 >0:
            error+=k 
        i+=1
    if error>=1:
        print("error in ",error," bit after correction data is ",end='') 
        
        if list1[int(error-1)]=='0' or list1[int(error-1)]==0:
            list1[int(error-1)]='1'
        else:
            list1[int(error-1)]='0'
        print(list1)
    else:
        print("No error")
    list2=list()
    i=0
    j=0
    k=0
    
    while i<len(list1): 
        if i!= ((2**k)-1):
            temp=list1[int(i)]
            list2.append(temp)
            j+=1
        else:
            k+=1
        i+=1
    return list2


fp2=open('encoded.txt','rb') 
fp3=open('output.txt','w')

msg=fp2.read()
msg=msg.decode('utf-8')


print("Obtained bits  "+msg)
msg=msg.split()


msg_b=[]
for x in msg:
    res=hammingCorrection(x)
    
    res=''.join(res)
    msg_b.append(res)


msg_b=' '.join(msg_b)
print("decoded msg is "+msg_b)

msg=[]
msg_b=msg_b.split()
for x in msg_b:
    res=chr(int(x,2))
    msg.append(res)

    
msg=''.join(msg)    
print(msg)


