def div_num():
    x=2519
    while True:
        for i in range(2,21):
            if x%i==0:
                i+=2
            else:
                x+=1
        return x 
if __name__=='__main__':
    print(div_num())
