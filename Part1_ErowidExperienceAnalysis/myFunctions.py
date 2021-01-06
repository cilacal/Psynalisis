import pickle
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
import os

# GET data, SAVE and LOAD objects
def getErowidExperiences(contents, separately = False, pre_process_text = False, word_class = None, drugs = None):
    experiences = {}

    if not isinstance(contents, dict):
        raise ValueError("The first parameter should be a dictionary.")
        
    for drug in contents.keys():
        if drugs != None and drug in drugs:
            if separately:
                experiences[drug] = [clean_and_filter_text(exp["text"], word_class) if pre_process_text else exp["text"] for exp in contents[drug]]
            else:
                experiences[drug] = ' '.join([clean_and_filter_text(exp["text"], word_class) if pre_process_text else exp["text"] for exp in contents[drug]])
        else: 
            continue
        
    return experiences

# Disclaimer: https://stackoverflow.com/questions/19201290/how-to-save-a-dictionary-to-a-file
def save_obj(obj, name, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

    with open(folder + name + '.pkl', 'wb+') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        
def load_obj(name, folder):
    with open(folder + name + '.pkl', 'rb') as f:
        return pickle.load(f)

# CLEAN text and FILTER by word class
class lemmaTokenizer:
    ignore_tokens = [',',';',':','"',"'",'`','.','˝','\\','/','+', '?', '!', '”', '“', '’', '...','``',"''"]
    def __init__(self):
        self.wnl = nltk.WordNetLemmatizer()
    def __call__(self, doc):
        return [self.wnl.lemmatize(self.wnl.lemmatize(t,"v")) for t in nltk.word_tokenize(doc) if t not in self.ignore_tokens]

def clean_and_filter_text(text, word_class = None):
    text = text.lower()
    text = re.sub(r'\w*\d\w*','', text).strip()
    text = re.sub("&lt;/?.*?&gt;&le&ge+\\\\",'', text).strip()
    text = lemmatize_and_filter_text(text, word_class)

    return text
 
def lemmatize_and_filter_text(text, word_class = None):
    tokenizer = lemmaTokenizer()
    lemmatized_tokens = tokenizer(text)
    
    if word_class != None:
        lemmatized_tokens = filter_tag(lemmatized_tokens, word_class)
            
    return ' '.join(lemmatized_tokens)
    
def filter_tag(tokens, tag):
    tagged_text = nltk.pos_tag(tokens)
    return [tuplet[0] for tuplet in tagged_text if tuplet[1] == mapTag(tag)]
    
def mapTag(tag):
    if tag not in ('adjective', 'verb', 'conjuction', 'noun', 'adverb'):
        print("The 'tag' parameter should be either 'adjective', 'verb', 'conjuction', 'noun', 'adverb'.")
        raise ValueError

    tagMap = {"adjective": "JJ",
              "verb": "VB",
              "conjuction": "CC",
              "noun": "NN",
              "adverb": "RB"}
    
    return tagMap[tag]

# REGROUP TEXT and FILTER keys

def without_keys(d, keys):
    return {x: d[x] for x in d if x not in keys}

def create_one_array(d):
    arr = []
    for k in d.keys():
        [arr.append(experience) for experience in d[k]]
    
    return arr

def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse = True)

def extract_topn_from_vector(feature_names, sorted_items, topn = 10):
    
    sorted_items = sorted_items[:topn]
    
    score_vals = []
    feature_vals = []
    
    for i, score in sorted_items:
        score_vals.append(round(score,3))
        feature_vals.append(feature_names[i])
        
    results = {}
    for i in range(len(feature_vals)):
        results[feature_vals[i]] = score_vals[i]
        
    return results

# VISUALIZATION

def plotCloud(frequencies = None, text = None,make_plot = True):
    if text == None and frequencies == None:
        raise ValueError("Either the 'text' or the 'frequencies' parameter should be defined!")
    
    if text != None and not isinstance(text, str):
        raise TypeError("ExperiencesAll['experiencesAll_&wordclass']['&drug'] should be given for the text parameter.")
    
    if frequencies != None and not isinstance(frequencies, dict):
        raise TypeError("The parameter 'frequencies' should be a dictionary with the top words as keys and the TF-IDF scores as values.")

    wordcloud = WordCloud(max_font_size=45, relative_scaling=0.5)
    if text != None:
        wordcloud = wordcloud.generate_from_text(text)
    else:
        wordcloud = wordcloud.generate_from_frequencies(frequencies = frequencies)
    
    
    plt.ioff()
    
    plt.figure(figsize = (10,10))
    plt.imshow(wordcloud)
    plt.axis("off")
    
    if make_plot:
        plt.show()
        return
    
    plt.ion()
    
    return plt
