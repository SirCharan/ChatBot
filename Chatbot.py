#Import Necessary Stuff
from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import os


chatbot= ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(chatbot)

#Enter Corpus File Path
corpus_path = 'chatterbot-corpus-master\chatterbot-corpus-master\chatterbot_corpus\data\english/'

for file in os.listdir(corpus_path):
    trainer.train(corpus_path + file)

#Chat Away
while True:
    message = input('You:')
    reply = chatbot.get_response(message)
    print('ChatBot:', reply)