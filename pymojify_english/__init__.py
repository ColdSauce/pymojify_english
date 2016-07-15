import json
FILE_NAME = "emojis.json"

def pymojify(paragraph):
    return u"".join(map(lambda e: get_emoji_for_word(_purify(e)) + " " , paragraph.split()))[:-1]
    
def _purify(word):
    return u''.join(map(lambda w: '' if not w.isalpha() else w, word))

def get_emoji_for_word(word):
    with open(FILE_NAME, 'r') as emojify:
        data = json.load(emojify)
        for key in data['keys']:
            value = data[key]
            keywords = value["keywords"]
            if word in keywords:
                return value["char"]
    return word
