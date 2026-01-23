#!/usr/bin/python3
"""
Add indentation
"""


def text_indentation(text):
    """
    Add indentation to a text next ., ? and :
    Parametres
    text: string
    Return:
    text with 2 new lines after each of these characters: ., ? and :
    Raise:
    TypeError
    """
    new_text = text.replace('.', '.\n\n')
    new_text1 = new_text.replace('?', '?\n\n')
    new_text2 = new_text1.replace(':', ':\n\n')
    try:
        if not isinstance(text, str):
            raise TypeError("text must be a string")
    finally:
        print(new_text2)
