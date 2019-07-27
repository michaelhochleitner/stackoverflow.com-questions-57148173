from nltk import word_tokenize, pos_tag, ne_chunk
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('words')
nltk.download('words')

with open('doesntwork.txt', 'r') as file: 
    data = file.read()
    data2 = data.split()
    tokens = nltk.word_tokenize(data)
    text = nltk.Text(tokens)

def categorize_words():
    print(pos_tag((tokens)))
output = categorize_words()
#following lines don't work for me therefore I commented them out to avoid confusion
#file = open("wordsfromdoesntwork.txt", "w")
#file.write(str(output))
#file.close()
