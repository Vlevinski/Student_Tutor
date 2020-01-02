# https://stackoverflow.com/questions/57163173/rotn-encoder-and-decoder-but-decoder-not-working
#  https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm

message = 'GIEWIVrotterdamGMTLIVrHIQS' #encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

for key in range(len(LETTERS)):
   translated = ''
   for symbol in message:
      if symbol in LETTERS:
         num = LETTERS.find(symbol)
         num = num - key
         if num < 0:
            num = num + len(LETTERS)
         translated = translated + LETTERS[num]
      else:
         translated = translated + symbol

print('Hacking key #%s: %s' % (key, translated))

