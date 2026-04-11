
alphabets = ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I',
              'J','K', 'L', 'M', 'N', 'O',
              'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y', 'Z']
def encryption (t , s ):
    cipher_text = ""           # Create a empty_String. For Toadd a new shifting aplhabets.
    for letter in t:
        position = alphabets.index(letter)     
        new_position = position + s
        new_letter = alphabets[new_position]
        cipher_text += new_letter
    print(cipher_text)

direction =  (input("Enter a encryption or decryption = ")).lower()
if direction == "encryption" :

    text = input("enter a message = ").upper()
    shift = int(input("How to Shift a number = "))
    encryption(t = text, s = shift)
else:
    print("You selecte a wong option. ")



