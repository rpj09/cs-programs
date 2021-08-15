def display():

        sfile= open("story.txt",'r')
        a = sfile.readlines()
        print(a)
        vowels='we'
        no=0
        for i in range(len(a)):
            count=a[i].count(vowels)
            no=no+count
        print('no of occurance: ',no)
        sfile.close()
display()
