def tables(m,n):
    for i in range (1,n+1):
       
        print("{}  x  {} = {}".format(i,m, i*m))
    
if __name__=="__main__":
    tables(5,10)
