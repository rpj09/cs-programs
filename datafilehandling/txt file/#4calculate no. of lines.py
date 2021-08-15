def display():

        sfile= open("story.txt",'r')

        a = (sfile.readlines())
        print(a)
        print('no of lines in a is',len(a))              
        sfile.close()
display()
