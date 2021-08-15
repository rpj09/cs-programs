def display():

        sfile= open("story.txt",'r')

        a = sfile.readlines()
        print(a)
        length=0
        for i in range(len(a)):
            b=(a[i]).split(' ')
            for j in range(len(b)):
                length=length+len(b[j])
        print('no of characters in file is ',length-len(a))
        sfile.close()
display()
