# Importing the required libaries
import pandas as pd
import pickle
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from nltk.corpus import stopwords 
import string
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize 
from sklearn.pipeline import  Pipeline
from sklearn.model_selection import train_test_split
import zipfile
import pickle


# Opening previously saved csv file that was collected through API's

zf = zipfile.ZipFile('style.zip')
style_data = pd.read_csv(zf.open('style.csv'))


# Function to clean the text information

def clean(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, ' ') # Remove Punctuation
    lowercased = text.lower() # Lower Case
    tokenized = word_tokenize(lowercased) # Tokenize
    words_only = [word for word in tokenized if word.isalpha()] # Remove numbers
    stop_words = set(stopwords.words('english')) # Make stopword list
    without_stopwords = [word for word in words_only if not word in stop_words] # Remove Stop Words
    lemma=WordNetLemmatizer() # Initiate Lemmatizer
    lemmatized = [lemma.lemmatize(word) for word in without_stopwords] # Lemmatize
    return lemmatized

# Apply to all texts
style_data['tags_clean'] = style_data.tags.apply(clean)
style_data['tags_clean'] = style_data['tags_clean'].astype('str')

# Train Test Split

X = style_data['tags_clean']
y = style_data['style']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)


# Fitting the model
sgd = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None)),
               ])

sgd.fit(X_train, y_train)

pickle.dump(sgd, open('model_sgd_python.pkl','wb'))