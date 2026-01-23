#!/usr/bin/python3
def text_indentation(text):
    new_text = text.replace('.', '.\n\n')
    new_text1 = new_text.replace('?', '?\n\n')
    new_text2 = new_text1.replace(':', ':\n\n')
    try:
        if not isinstance(text, str):
            raise TypeError("text must be a string")
    finally:
        print(new_text2)
