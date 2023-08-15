alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def caesar(text, shift):
  message = []
  length = len(alphabet)
  for letter in text:
    if letter in alphabet:
      if direction == "encode":
        position = ((alphabet.index(letter) + shift) % (length))
      elif direction == "decode":
        position = ((alphabet.index(letter) - shift) % (length))
      message.append(alphabet[position])
  print("".join(message))

caesar(text=text, shift=shift)

