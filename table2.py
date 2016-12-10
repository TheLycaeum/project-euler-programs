def sq_tables(n):
    for i in range(1,n+1):
        print(i,end="\t")    
    print("")
    print("-----"*7)
    for j in range(2,n+1):
        for k in range(1,n+1):
            print(j*k,end="| \t")
        
        print("\n")
if __name__=="__main__":
    sq_tables(10)
