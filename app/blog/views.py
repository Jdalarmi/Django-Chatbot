from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('chatbot', read_only=False, logic_adapters=['chatterbot.logic.BestMatch'])

list_to_train = [
    "hi",
    "hi there",
    "What's your name?",
    "I am just a chatbot",
    "What is your favorite food?",
    "I like Pizza"
]

list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

def index(request):
    return render(request, 'blog/index.html')

def specific(request):
    return render(request)


def getresponse(request):
    userMessage = request.GET.get('userMessage')
    return HttpResponse(userMessage)
