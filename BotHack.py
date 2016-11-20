__author__ = 'zampeta'

import sys, re
import time
import telepot
from luis_apiLanguage import *
from lyrics import get_lyrics
from spotifywords import get_songs
from random import choice, randint, seed
from TranslateDict import translate


WORDS = {
    'german': [
        ('Strasse', 'Bahn', 'Liebe'),
        ('Feuerwerk', 'Schinken', 'Leberwurst'),
        ('Bruttosozialprodukt', 'Kneipe', 'Pommes'),
    ],
    'spanish': [
        ('Strasse', 'Bahn', 'Liebe'),
        ('Bier', 'Autobahn', 'Leberwurst'),
        ('Bruttosozialprodukt', 'Kneipe', 'Pommes'),
    ],
    'italian': [
        ('Strasse', 'Bahn', 'Liebe'),
        ('Bier', 'Autobahn', 'Leberwurst'),
        ('Bruttosozialprodukt', 'Kneipe', 'Pommes'),
    ]
}

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text':
        input = str(msg['text']).lower()
        if input == 'hi' or input == 'hey' or input =='hello':
            bot.sendMessage(chat_id,'Hey '+ msg['from']['first_name']+'!')
            time.sleep(1.5)
            bot.sendMessage(chat_id,'I am Marco Polo, or just Marc. With me, you get to discover new foreign music AND enhance your vocabulary. You will learn rare words, words that will make other language learners marvel at your knowledge!')
            time.sleep(3.5)
            bot.sendMessage(chat_id,'But first of all, tell me what language you plan to study.')
        else:
            bot_resp= callLUIS(input)
            action,score=parseIntent(bot_resp)
            entities=parseEntities(bot_resp)
            #pass entities as search criteria
            bot.sendMessage(chat_id, 'Ok, ' + entities[-1][1] + ' it is!')
            bot.sendMessage(chat_id,'I  will crammed through the lyrics of some interesting!\n')
            time.sleep(1.5)
            bot.sendMessage(chat_id, 'Give me a second ...')
            seed()
            i = randint(0, 2)
            j = randint(0, 2)
            songs = get_songs([WORDS[entities[-1][0]][i][j]], 20)
            print [WORDS[entities[-1][0]][i][j]]
            lyrics = None
            song = None
            k = 0
            while not lyrics:
                song = songs[k]
                lyrics = get_lyrics(song['artist'], song['name'])
                k += 1
            lyrics = lyrics.split()
            words = set([])
            while len(words) < 3:
                word = choice(lyrics)
                if len(word) > 4:
                    words.add(word)
            # find the right one
            #print words
            k = randint(0, len(songs))
            wordlist = list(words)
            bot.sendMessage(chat_id, song['url'])
            bot.sendMessage(chat_id,' Just listen to it and get back to me!')
            bot.sendMessage(chat_id, 'Now I  gonna ask you some words that you might recognize from the song you just heard. If you don\'t know them already let\'s learn them!')
            bot.sendMessage(chat_id, 'What does ' + wordlist[1] + ' mean in English?')
            print wordlist[1]
            time.sleep(1.5)
            best_match=translate(str(wordlist[1]), 'de', 'en')[0]
            bot.sendMessage(chat_id, 'It means ' + best_match[1] + ' in English')
            time.sleep(1.5)
            bot.sendMessage(chat_id, 'Great e!!')
            print best_match

TOKEN = '298709323:AAGoMEjB6llvWIlc3HvmXBjO8GC_2JRmJvM' #sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)