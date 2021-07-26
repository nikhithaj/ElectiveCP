str="nikhitha"

def char(str):
    i={}
    for k in str:
        if k in i:
            i[k] +=1
        else:
            i[k] =1
    print(i)
char(str)            
     

