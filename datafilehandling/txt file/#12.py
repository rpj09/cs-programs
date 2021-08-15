def display():
        sfile= open("story.txt",'r')
        a = sfile.readlines()
        print(a)
        count=0
        for i in range(len(a)):
            b=a[i]    
            now=b.split()
            print(now)
            for i in range(len(now)):
                result= (b[i]).endswith('e')
                if result == True:
                    count=count+1
        print(count)
        sfile.close()
display()
