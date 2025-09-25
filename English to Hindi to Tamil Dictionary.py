eng_hindi = {'Name':'Naam' , 'Book':'Kithab' , 'Hand':'Haath', 'Horse':'Ghoda'}
hindi_tamil = {'Naam':'Peyar' , 'Kithab':'Putthagam' , 'Haath':'Kai', 'Ghoda':'Kudhurai'}
print("English\t\tHindi\t\tTamil")
for key in eng_hindi:
    print(key,"=\t\t",eng_hindi[key],"=\t\t",hindi_tamil[eng_hindi[key]])
