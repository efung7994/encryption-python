alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(text, shift):
  message = []
  length = len(alphabet)
  for letter in text:
    if letter in alphabet:
      position = ((alphabet.index(letter) +shift) % (length))
      message.append(alphabet[position])
  print("".join(message))

def decrypt(text, shift):
  message = []
  length = len(alphabet)
  for letter in text:
    if letter in alphabet:
      position = ((alphabet.index(letter) - shift) % (length))
      message.append(alphabet[position])
  print("".join(message))

if direction == "encode":
  encrypt(text=text, shift=shift)
if direction == "decode":
  decrypt(text=text, shift=shift)
