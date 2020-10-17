def countWords():
    fileName = input("Enter a file name : ")
    file = open(fileName, "r")
    noOfWords = 0
    for i in file:
        w = i.split(" ", 2)
        noOfWords = noOfWords+len(w)
    
    print(noOfWords)


countWords()