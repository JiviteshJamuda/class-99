sentences=input("enter your sentences")
characters=0
wordCount=1
for i in sentences :
    characters=characters+1
    if(i == " ") :
        wordCount=wordCount+1
        print(wordCount)