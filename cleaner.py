import re

def remove_common_unused_text(chat_file):
  date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)"
  white_space = r"\s-\s"
  username = r"([\w\s]+)"
  ending_text = r":\s"
  pattern = date_time + white_space + username + ending_text

  with open(chat_file, "r") as file:
    content = file.read()
    cleaned_file = re.sub(pattern, "", content)
    return tuple(cleaned_file.split("\n"))

def remove_non_message(export_text):
  messages = export_text[1:-1]
  filter_media = ("<Media omitted",)
  return tuple((msg for msg in messages if msg not in filter_media))


def clean_chat(chat_file):
   message_corpus = remove_common_unused_text(chat_file)
   cleaned = remove_non_message(message_corpus)
   return cleaned