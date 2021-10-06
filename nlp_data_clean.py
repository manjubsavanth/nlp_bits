import re
from nltk.corpus import stopwords
stop_words = stopwords.words("english")
def text_preprocessing(x):
    # Lowercase the text
    x = x.lower()
    # Remove stop words
    x = ' '.join([word for word in x.split(' ') if word not in stop_words])
    # Remove unicode characters
    x = x.encode('ascii', 'ignore').decode()
    # Remove URL
    x = re.sub(r'https*\S+', ' ', x)
    # Remove mentions
    x = re.sub(r'@\S+', ' ', x)
    # Remove Hashtags
    x = re.sub(r'#\S+', ' ', x)
    # Remove ticks and the next character
    x = re.sub(r'\'\w+', '', x)
    # Remove punctuations
    x = re.sub('[%s]' % re.escape(string.punctuation), ' ', x)
    # Remove numbers
    x = re.sub(r'\w*\d+\w*', '', x)
    # Replace the over spaces
    x = re.sub(r'\s{2,}', ' ', x)
    return x
