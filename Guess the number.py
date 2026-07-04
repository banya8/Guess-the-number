import random
def gencode():
    set_code=[]
    for i in range(4):
        val= random.randint(0,9)
        set_code.append(val)
        
    return set_code
def getcode():
    code=input("Enter a 4 digit number to guess it:")

    return code

def play_code():

    gen_code =gencode()
    i=0
    while i<5:
        result= " "
        get_code=[int(c) for c in getcode()]
        if len(get_code)!=4:
            print("Please enter a 4 digit number.")

            continue

        if gen_code==get_code:
          print("Congratulations! You have guessed the Code successfully.!",gen_code)
         
          break
        for element in get_code:
            if element in gen_code:
                if get_code.index(element)== gen_code.index(element):
                   result+="R"
                else:
                    result+="Y"
            else:
                result+="B"
        print(result)
        i+=1
    else:
        print("Oops!You ran out of trys!\n here's the code:",gen_code)
    
play_code()
        


        

