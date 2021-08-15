def display():

        sfile= open("story.txt",'r')

        a = sfile.read()
        print(a)
        vowels='AEIOUaeiou'
        no_of_vowels=0
        no_of_conso=0
        for i in vowels:
            count=a.count(i)
            no_of_vowels=no_of_vowels+count
        for i in a:
            coun=a.count(i)
            no_of_conso=no_of_conso+coun
        
        print('no of vowels : ',no_of_vowels)
        print('no of consonants',no_of_conso-no_of_vowels)
        
    
        sfile.close()
display()
