#============================== CODE ==================================#
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
      's','t','u','v','w','x','y','z']
umlauts=['ä','ö','ü']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=[',','.','!','?',':','-','_','"',"'",'%',' ']
reserved=['^','$']

code = alphabet + umlauts + symbols + reserved + numbers

#========================= GENERAL FUNCTIONS ==========================#

#Takes a String and transforms each uppercase letter into lowercase and adds ^ befor. e.g. H --> ^h
#Transforms textbreak into the character $
def transformString (string):
    string = string.replace('\n',reserved[1])
    k=len(string)
    i=0
    while i < (k):
        if string[i].isupper() == True:
            string=string[0:i]+reserved[0]+string[i].lower()+string[(i+1):k]
            k+=1
        i+=1
    return string

#Takes a string and adds for each character the index of the character in the code to a list
def CodeIt(string, lst_code):
    var= []
    for x in string:
        var.append(lst_code.index(x))
    return var

#Adds or subtracts the elements of two lists together and creates new list
def calculateLists(lst_input,task,lst_key):
    lst_var=[]
    i=0
    for x in range(len(lst_input)):
        
        if task == 'crypt':
            lst_var.append(lst_input[x]+lst_key[i])
        else:
            lst_var.append(lst_input[x]-lst_key[i])
            
        if (i+1) == len(lst_key): #when list from key is shorter, it starts again
            i=0
        else:
            i+=1

    return lst_var

#Creates a string out of the elements of a list
def StringOutOfList (lst):
    return ''.join(lst)

#========================= EXPLICIT FUNCTIONS ==========================#

#------------------------- Function Encrypt   --------------------------#
def encrypt(txt,key):
    txt = transformString(txt)
    key = transformString(key)

    var = txt
    for _ in range(2):
        for x in var:
            if x not in code:
                error = 'error'
                return error
        var = key

    lst_txt = CodeIt(txt,code)
    lst_key = CodeIt(key,code)


    lst_added = calculateLists(lst_txt,'crypt',lst_key)


    lst_crypted=[]
    for x in lst_added:
        if x > (len(code)-1):
            x-=len(code)
        lst_crypted.append(code[x])

    isCrypted= StringOutOfList(lst_crypted)

    return isCrypted

#------------------------- Function Decrypt   --------------------------#

def decrypt(crypted,key):
    key = transformString(key)
    
    var = key
    for _ in range(2):
        for x in var:
            if x not in code:
                error = 'error'
                return error
        var = crypted

    lst_crypted = CodeIt(crypted,code)
    lst_key = CodeIt(key,code)

    lst_dif = calculateLists(lst_crypted,'decrypt',lst_key)


    lst_decrypted=[]
    for x in lst_dif:
        if x < 0:
            x+= len(code)
        lst_decrypted.append(code[x])

    for x in lst_decrypted:
        if x == reserved[0]:
            k = lst_decrypted.index(x)+1
            lst_decrypted[k] = lst_decrypted[k].upper()
            lst_decrypted.remove(x)
        elif x == reserved[1]:
            k = lst_decrypted.index(x)
            lst_decrypted[k] ='\n'

    isDecrypted= StringOutOfList(lst_decrypted)

    return isDecrypted
