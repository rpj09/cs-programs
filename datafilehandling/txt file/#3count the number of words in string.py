def display():

        sfile= open("story.txt",'r')

        a = (sfile.read()).split()
        print(a)
        for i in range(len(a)):
            if a[i][0] in 'Aa':
                print(a[i])               
        sfile.close()
display()
