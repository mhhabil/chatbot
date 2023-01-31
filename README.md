# Build a Chatbot with Python

```sh
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

```sh
(venv) $ cd source_code_final
(venv) $ python bot.py
```

Data training can be found in chat.txt.
chat.txt will be cleaned with cleaner.py.

After training, you'll see an interactive prompt that you can chat with:

```text
> hi
Welcome, How can i help you?
> is this infomedia
Yes, this is Infomedia, Your Digital CX Partner.
> do you have
i got three of them, so they are second gen supermarket basils with lots of siblings :)
> very philosophical!
Lol
> did you know?
I really hope they're gone now
> no crops in pots
Ah, gotcha!
```

The bot will learn from the replies you give and improve its accuracy. You can quit the interactive prompt by typing any of the `exit_conditions` defined in `bot.py`.

The folders also include a SQLite database that contains the different phases of training at each step. Because of this, you can inspect the project at different stages and notice how it evolves when you add more data and interactions.
