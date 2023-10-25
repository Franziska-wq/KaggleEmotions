import nltk
from nltk.corpus import stopwords, words
from nltk.stem.porter import *
from nltk import word_tokenize

#nltk.download('stopwords')

################ Global variables ################
# paths for the files
data_path = "./data/"
result_path = "./results/"
export_path = data_path + "categories/"
corpus = data_path + "corpus/"

train_file = data_path + "train.txt"
test_file = data_path + "test.txt"
val_file = data_path + "val.txt"
complete_file = data_path + "complete.txt"


################ Useful functions ################

# process text files so that a list is returned with [<sentence>,<emotion>]
def read_file(file_path: str, delim: str):
    data = []
    with open(file_path,'r') as file:
        for line in file:
            data.append(line.strip().split(delim))
    return data

# write text to file
def write_to_file(file_path: str, content: str, new: bool):
    if new: file = open(file_path,'w')
    else: file = open(file_path,'a')
    file.write(content)
    file.close()
    
# perform Stemming and remove Stopwords
def preprocess(sentences, append=False):
    cleaned = []
    break_p = False
    
    for sentence in sentences:
        if not type(sentences) == list: 
            sentence = sentences
            break_p = True
        stop_words = list(set(stopwords.words('english')))
        stop_words.extend(['im', 'ive','dont','cant'])
        stemmer = PorterStemmer()
    
        word_tokens = word_tokenize(sentence)
        cleaned_words = [stemmer.stem(w) for w in word_tokens if not w.lower() in stop_words]
        if break_p:
            return cleaned_words
        
        if append:
            cleaned.append(cleaned_words)
        else:
            cleaned.extend(cleaned_words)
    return cleaned