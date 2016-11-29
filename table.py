def tables(m,n):
    for i in range (1,n+1):
        out=i*m
        print("{}  x  {} = ".format(i,m),out)
    
if __name__=="__main__":
    tables(5,10)
