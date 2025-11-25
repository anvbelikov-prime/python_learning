tap_code_map = {"a": ". .",  "b": ". ..",  "c": ". ...",  "d": ". ....",  "e": ". .....",  "f": ".. .",  "g": ".. ..",  "h": ".. ...",  "i": ".. ....",  "j": ".. .....",  "l": "... .",  "m": "... ..",  "n": "... ...",  "o": "... ....",  "p": "... .....",  "q": ".... .",  "r": ".... ..",  "s": ".... ...",  "t": ".... ....",  "u": ".... .....",  "v": "..... .",  "w": "..... ..",  "x": "..... ...",  "y": "..... ....",  "z": "..... .....", }

def tap_code_to_english(input_code):
    tap_code_inverted_map = {code: letter for letter, code in tap_code_map.items()}
    return ' '.join([''.join([tap_code_inverted_map.setdefault(c, '') for c in word.split('  ')]) for word in input_code.split('   ')])

print(tap_code_to_english(".. ...  .. ....   .. ...  .. ...."))
print(tap_code_to_english(". ...  ... ....  ... ....  ... ."))
print(tap_code_to_english(""))
