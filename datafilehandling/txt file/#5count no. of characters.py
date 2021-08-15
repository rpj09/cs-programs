def display():

        sfile= open("story.txt",'r')

        a = sfile.readlines()
        print(a)
        print('no of lines in a is',len(a))
        now=0
        for i in range(len(a)):
            b=len(a[i])
            now=now+b
        print('no of character is',now-len(a))
        sfile.close()
display()
