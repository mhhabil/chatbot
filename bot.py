from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_chat

FILE = 'chat.txt'

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
cleaned_file = clean_chat(FILE)
trainer.train(cleaned_file)
trainer.train([
  "Hi",
  "Welcome, How can i help you?"
])
trainer.train([
  "Is this infomedia?",
  "Yes, this is Infomedia, Your Digital CX Partner."
])

exit_conditions = (":q", ":quit", "exit")
while True:
  query = input("> ")
  if query in exit_conditions:
    break
  else:
    print(chatbot.get_response(query))