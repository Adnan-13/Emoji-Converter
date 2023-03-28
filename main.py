def convert_emojis(msg: str) -> str:
    words = msg.split(' ')
    emojis = {
        ':)': '😊',
        ':(': '😢',
        ':/': '😕',
        ':D': '😁',
        ':P': '😛',
        ':O': '😮',
        ':*': '😘',
        ':|': '😐',
        '>:(': '😠',
        ':@': '😡',
        'o_o': '😲',
        ':3': '😸',
        '>_<': '😣',
        ':S': '😖',
        'O_O': '😱',
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


message = input('Enter a message: ')
message = convert_emojis(message)
print(message)
