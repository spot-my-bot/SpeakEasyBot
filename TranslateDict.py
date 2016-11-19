__author__ = 'zampeta'
from dictcc import Dict, AVAILABLE_LANGUAGES

def ensure_unicode(string):
    if hasattr(string, "decode"):
        return string.decode("utf-8")
    return string



def translate(word,from_lan, to_lan):
    word=ensure_unicode(word)
    result = Dict.translate(word,from_lan, to_lan)
    trans=[]
    for i, (input_word, output_word) in enumerate(result.translation_tuples):
        #print (input_word, output_word)
        trans.append((input_word, output_word) )
    return trans


#best_match=translate("tscss", 'de', 'en')[0]
#print best_match[0]