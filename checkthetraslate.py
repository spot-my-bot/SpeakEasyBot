from dictcc import Dict, AVAILABLE_LANGUAGES

def translate(word,from_lan, to_lan):
    result = Dict.translate(word,from_lan, to_lan)
    trans=[]
    for i, (input_word, output_word) in enumerate(result.translation_tuples):
        #print (input_word, output_word) 
        trans.append((input_word, output_word) )
    return trans
        

best_match=translate("strasse", 'de', 'en')[0]
print best_match[0]