# Basic redaction - add fuzzy matching 
from fuzzywuzzy import fuzz



# Convert string to list 
def convert(lst):
    return (lst[0].split())

# Convert list to string 
def convert_string(lst):
    string = ""
    for i in range(len(lst)):
        string += lst[i]
        string += " "
    return string

# Turn letters (not punctuation) into redacted * 
def star(query):
    redact = ""
    for x in range(len(query)):
        if (ord(query[x]) > 64):
            redact += "*"
        else:
            redact += query[x]
    return redact 

def redact(text, query): 
    # Fuzzy matching 
    fuzzy = False 
    #Similarity threshold 
    ratio_thresh = 70 
   
    # Put each word in list for ease 
    text_split = convert([text])

    # Iterate through text and match to keywords, if match redact 
    for i in range(len(text_split)):
        for j in range(len(query)):
            if (text_split[i][0].lower() != query[j][0].lower()):
                continue
            else:  
                if (text_split[i].lower() == query[j].lower()) or (fuzzy == True and (fuzz.ratio(text_split[i], query[j]) > ratio_thresh)): 
                    text_split[i] = star(text_split[i])
                else: 
                    break

    return(text_split)

# # List of words to be redacted
# query = ["cat", "farm"] 
# # Text to redact from 
# text = "The cat (Felis catus) is a domestic species of small carnivorous mammal.[1][2] It is the only domesticated species in the family Felidae and is often referred to as the domestic cat to distinguish it from the wild members of the family.[4] A cat can either be a house cat, a farm cat or a feral cat; the latter ranges freely and avoids human contact.[5] Domestic cats are valued by humans for companionship and their ability to kill rodents. About 60 cat breeds are recognized by various cat registries.[6]"
# text_split = redact(text, query)

# Put list back to text 
# redacted_text = convert_string(text_split)
# print(redacted_text)  




