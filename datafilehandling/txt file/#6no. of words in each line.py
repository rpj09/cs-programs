def display():
        sfile= open("story.txt",'r')
        a = sfile.readlines()
        print(a)
        print('no of lines in a is',len(a))
        for i in range(len(a)):
            b=a[i]    
            now=b.split()
            print('no. of words in line ',i+1,' =',len(now))
        sfile.close()
display()
