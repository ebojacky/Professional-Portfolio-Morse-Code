from morse_code_data import morse_code_map


def generate_morse(input_text):
    input_text = input_text.strip()
    res = ""
    for char in input_text:
        if char == " ":
            res += " /"
        else:
            res += " " + morse_code_map[char.upper()]

    return f"Morse Code: {res.strip()}"


def interpret_morse(input_morse):
    input_morse = input_morse.strip()

    morse_keys = list(morse_code_map.keys())
    morse_values = list(morse_code_map.values())

    res = []
    for word in input_morse.split(" / "):
        decoded_word = ""

        for char in word.split(" "):
            decoded_word += morse_keys[morse_values.index(char)]

        res.append(decoded_word)

    return f"Code Text: {' '.join(res)}"


welcome = """
╦ ╦┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ┌┬┐┌─┐  ╔╦╗┌─┐┬─┐┌─┐┌─┐  ╔═╗┌─┐┌┬┐┌─┐
║║║├┤ │  │  │ ││││├┤    │ │ │  ║║║│ │├┬┘└─┐├┤   ║  │ │ ││├┤ 
╚╩╝└─┘┴─┘└─┘└─┘┴ ┴└─┘   ┴ └─┘  ╩ ╩└─┘┴└─└─┘└─┘  ╚═╝└─┘─┴┘└─┘  
"""

while True:
    print(welcome)
    choice = input("Press 1 to generate Morse Code.\nPress 2 to Interpret a Morse Code.\n:")

    try:

        if choice == "1":
            text = input("Input the text: ")
            print(generate_morse(text))

        elif choice == "2":
            morse = input("Input the morse code: ")
            print(interpret_morse(morse))

        else:
            print("Wrong Choice!")

    except Exception as e:

        print(f"An Error Occurred: {e}")

    again = input("Press Y to run programme again.\nPress any other key to quit.\n:")
    if again.upper() != "Y":
        break