L=[1,2,4,8,16,32,64,128,256,512,1024,32768,65536,4294967296]
dic = {}
for i in L:
        if len(str(i)) in dic :
            dic[len(str(i))].append(i)
        else:
            dic[len(str(i))] = [i]
print(dic)