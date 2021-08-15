def display():

        sfile= open("story.txt",'r')
        a = sfile.read()
        print(a)
        a = a.replace('this','that')
        print(a)
        sfile.close()
        sfile= open("story.txt",'w')
        sfile.writelines(a)
        sfile.close()
display()
