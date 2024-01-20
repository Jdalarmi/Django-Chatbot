from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('chatbot', read_only=False,
              logic_adapters=[{

                  'import_path': 'chatterbot.logic.BestMatch',
                  'default_response': 'Sorry, I dont know what that means',
                  'maximum_similarity_threshold': 0.95
              }])

list_to_train = [
    "hi",
    "hi there",
    "Whats your name?",
    "I am just a chatbot",
    "What is your favorite food?",
    "I like Pizza",
    "What's your favorite sport?",
    "swimming",
    "do you have children?",
    "No! you crazy mothafucka!!"
]

list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

def index(request):
    return render(request, 'blog/index.html')

def specific(request):
    return render(request)


def getresponse(request):
    userMessage = request.GET.get('userMessage')
    chat_response = str(bot.get_response(userMessage))
    return HttpResponse(chat_response)
