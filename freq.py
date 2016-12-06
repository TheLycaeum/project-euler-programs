def freq(s):
    dict={}
    for j in set(s):
        x=s.count(j,0,len(s))
        dict[j]=x
    print(dict)

    
if __name__=="__main__":
    freq("This is my string")
        
