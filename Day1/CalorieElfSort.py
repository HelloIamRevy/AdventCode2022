#indents matter in py
def ElfSort(inputarray): #will sort array and output Largest Sum Integer def is how you define an method and then end with colon
    
    pass #pass lets you cheat good thing

def Parseinput(textinput):    # will take text file and make an array
    NotElfArray = []   #in py this is a list works like array but not array didnt end up using this but still good notes
     
    EverythingString = open(textinput, "r").read() #open is a funtion little r is to read read() is also a funtion
    
    #print("{} \n\n:output of text file: ".format(EverythingString)) #last thing is the main method so have everything else be above it
           #\n is new line and is an escape charcter 
    tempvar = EverythingString.split("\n\n") # splits string by what you define in arg always returns list
    return tempvar
    
    
    
    
    
    
    #__enviormentvariable__   double underscore max says python makes it. 
    
    #Where I left off brought in everything as a string













#leaving off on elfsort

Elfarray = Parseinput("input.txt")
CalorieElf = ElfSort(Elfarray)
print(CalorieElf) 
    
    
    
    


