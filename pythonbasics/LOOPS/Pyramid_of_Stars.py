start= int(11/2)
end=int(11/2-1)
for i in range(0,5):
    print("\t")
    for j in range(0,5):
        if j in range(start,end):
            print(" * ",end='')
        else:
            print(" ",end="")    
    start-=1
    end+=1
    print()        



        
        
        
       