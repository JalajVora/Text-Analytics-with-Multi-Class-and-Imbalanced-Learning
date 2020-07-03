import pandas as pd

# define data locations
data_dir = 'Gutenberg_English_Fiction_1k/'
target_file = 'master996.csv'
corpus_dir = 'Gutenberg_19th_century_English_Fiction/'

def load_corpus():
    """Loads the sample of the Gutenberg corpus in a pandas dataframe.
    The data frame has the follwing content:

        * bookid (index) \t unique string
        * Book_Name \t title of the book
        * guten_genre \t the books genere (target)
        * content \t string containing the books raw content
    """
    # check if a preprocessed corpus already exists
    try:
        return pd.read_csv('corpus.csv', index_col='book_id')
    except:
        print('could not load corpus.csv. Will create corpus from html files.') 

    # import target
    data = pd.read_csv(data_dir + target_file, sep=';', engine='python')
    data.loc[:]['book_id'] = data['book_id'].apply(lambda book_id: book_id[:-5]) # remove '.epub' ending
    data.set_index('book_id', inplace=True)

    # import corpus
    def get_book_content(book_id):      
        filename = data_dir + corpus_dir + book_id + '-content.html'
        
        with open(filename, encoding='utf-8') as file:        
            try:
                content = file.read()
                
            except UnicodeDecodeError:
                print('UnicodeDecodeError trying to read {}. Returning None.'.format(book_id))
                return None
            
            content = content.replace('<p>','')   
            
        return content

    data['content'] = [get_book_content(book_id) for book_id in data.index]

    return data

def load_meta_data():
    try:
        return pd.read_csv('meta_data.csv', index_col='book_id')
    except:
        print('Could not load meta data')

def save_corpus(corpus: pd.DataFrame):
    corpus.to_csv('corpus.csv')