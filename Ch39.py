#Program to replace words
def replace_words(sent,o,n):
    return sent.replace(o,n)
    
sent = input("Enter a sentence: ")
o = input("Enter the word to be replaced: ")
n = input("Enter the new word: ")

updated_sent = replace_words(sent,o,n)

print("The updated sentence: ", updated_sent)

# Enter a sentence: Privacy Shutter in Webcam
# Enter the word to be replaced: in
# Enter the new word: on
# The updated sentence:  Privacy Shutter on Webcam
