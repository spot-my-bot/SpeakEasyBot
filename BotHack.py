__author__ = 'zampeta'

import sys, re
import time
import telepot
from luis_apiLanguage import *
from lyrics import get_lyrics
from spotifywords import get_songs
from random import choice, randint

WORDS = {
    'german': [
        ('Strasse', 'Bahn', 'Liebe'),
        ('Bier', 'Autobahn', 'Leberwurst'),
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
        bot_resp= callLUIS(input)
        action,score=parseIntent(bot_resp)
        entities=parseEntities(bot_resp)
        #pass entities as search criteria
        bot.sendMessage(chat_id, 'So you want to learn ' + entities[-1][1])
        i = randint(0, 2)
        j = randint(0, 2)
        songs = get_songs([WORDS[entities[-1][0]][i][j]], 20)
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
        print words
        k = randint(0, len(songs))
        bot.sendMessage(chat_id, song['url'])

TOKEN = '298709323:AAGoMEjB6llvWIlc3HvmXBjO8GC_2JRmJvM' #sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)