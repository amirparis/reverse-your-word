name=str(input('enter your word : ')) 
ar=list(name)
for i in range(len(ar)-1,-1,-1) :
    print(ar[i] , end='' )
