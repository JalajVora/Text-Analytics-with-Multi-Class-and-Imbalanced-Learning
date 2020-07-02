import nltk
import string
#for word tokens and stopwords:
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

#for stemming and lemmatization:
from nltk.stem import WordNetLemmatizer 
from nltk.stem import PorterStemmer 
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer() 
stemmer = PorterStemmer()
usedStoppwords = stopwords.words('english')


def prepare_texts(texts, use_stemming = False, additional_stopwords = [], additional_punctuation = ""):
    
    usedStoppwords.extend(additional_stopwords)
    punct = string.punctuation + additional_punctuation
    
    print("Text Count: ",len(texts)," Progress: ")
    data_content_filtered = []
    count = 0
    for text in texts:
        print(str(count)+", ", sep=' ', end='', flush=True)
        count = count +1       
        text_tokens = word_tokenize(text) #creates a word token list    
        #remove punctuation
        text_tokens_filtered_punct = [w for w in text_tokens if w not in punct]
        #lemmatize and remove stoppwords
        text_tokens_filtered = [lemmatizer.lemmatize(w) for w in text_tokens_filtered_punct if not w in usedStoppwords]
        #if stemming wanted, stem
        if(use_stemming):
            text_tokens_stemmed = [stemmer.stem(w) for w in text_tokens_filtered]    
        text_filtered = (" ").join(text_tokens_filtered)
        data_content_filtered.append(text_filtered)
    print("")
    return data_content_filtered