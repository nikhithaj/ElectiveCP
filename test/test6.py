# def pattern(n):
#     for i in range(n+1):
#         for j in range(1,i+1):
#             print(j,end=" ")
#         print()  
# pattern(4)
          
# def pattern(n):
#     n=n+1
#     for i in range(n):
#          for j in range(1,n-i):
#             print(j,end=" ")
#          print()  
# pattern(4)    

# def pattern(n):
#     n=n+1
#     arr=[]
#     for i in range(n):
#         ar=[]
#         for j in range(1,n-i):
#             ar.append(j)
#         arr.append(ar)    
#     print(arr)  
# pattern(4)     
  
def pattern(n):
    n=n+1
    arr=[]
    for i in range(n):
        ar=[]
        for j in range(1,n-i):
            ar.append(j)
        arr.append(ar)    
    print(arr)  
pattern(4)    


