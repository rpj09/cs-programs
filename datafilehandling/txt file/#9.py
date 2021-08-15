def display():

        sfile= open("story.txt",'r')

        a = sfile.readlines()
        print(a)
        print('no of lines is',len(a))
        length=0
        for i in range(len(a)):
            a[i]=a[i][::-1]
            print(a[i])
        '''
        for i in range(len(a)):
            b=(a[i]).split(' ')
            for j in range(len(b)):
                length=length+len(b[j])
        print('no of characters in file is ',length-len(a))
        '''
        sfile.close()
display()
