# -*- coding: utf-8 -*-
#coding=utf-8
data = [ i for i in "1234567890"]
cal = {"+":1,"-":1,"*":2,"/":2}
cal1 = {"(":0}
def parse(source):
    result = []
    c = []
    slist = [i for i in source]
    for item in slist:
        if item in data:
            result.append(item)
        elif not c and item in cal.keys():
            c.append(item)
            continue
        elif c and item in cal.keys():
            for x in range(c.__len__()):
                z=c[-1]
                temp = cal[z] if cal[z] else cal1[z]
                if temp >= cal[item]:
                    result.append(c.pop())
                else:
                    c.append(item)
                    break
            if not c:
                c.append(item)
        elif item == ")":
            for x in range(c.__len__()):
                if c[-1] == "(":
                    c.pop()
                    break
                else:
                    result.append(c.pop())
        elif item == "(":
            c.append(item)
        #print(result,c)
    for x in range(c.__len__()):
        result.append(c.pop())
    return result

def caculate(source):
    num = []
    for i in source:
        if i in data:
            num.append(i)
        else:
            num1=num.pop()
            num2=num.pop()
            num.append(str(eval("%s%s%s"%(num2,i,num1))))
    return num[0]

if __name__ == "__main__":
    sourcestr = "5+(3-1)*2-6/2"
    print("orig:%s"%sourcestr)
    re1 = parse(sourcestr)
    print("niBolan:%s"%" ".join(re1))
    result = caculate(re1)
    print('result:%s'%result)
