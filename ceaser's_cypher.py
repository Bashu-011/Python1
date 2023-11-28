alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(input_text, shift_number, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
            shift_number *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_number
            end_text += alphabet[new_position]
        else:
             end_text += char
    print(f"The {cipher_direction}d text is {end_text}")


if_continue = True
while if_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    ceaser(input_text=text, shift_number=shift, cipher_direction=direction)
    restart = input("To continue type yes and to stop type no: ").lower()
    if restart == 'no':
        if_continue = False
        print("Bye. Thanks for playing")


        
'''def encrypt(plain_text, shift_number):
    encoded_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift_number
        encoded_text += alphabet[new_position]
    print(f"This is the encoded message {encoded_text}")


def decrypt(encoded, shift_number):
    decoded_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        decoded_text += alphabet[new_position]
    print(f"This is the decoded message: {decoded_text}")

if direction == 'encode':
    encrypt(plain_text=text, shift_number=shift)
elif direction == "decode":
    decrypt(encoded=text, shift_number=shift)
else:
    print("Wrong input")'''
