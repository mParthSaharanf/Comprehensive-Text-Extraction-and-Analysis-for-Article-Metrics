import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

class Analysis:
    def __init__(self):
        self.lem = WordNetLemmatizer()
    
    def StopWords_data(self, file_path='/home/yung_nusrat/for_intern/StopWords/'):
        stopword_auditor = open(f'{file_path}/StopWords_Auditor.txt', 'r', encoding='ISO-8859-1')
        StopWords_Currencies = open(f'{file_path}/StopWords_Currencies.txt', 'r', encoding='ISO-8859-1')
        StopWords_DatesandNumbers = open(f'{file_path}/StopWords_DatesandNumbers.txt', 'r', encoding='ISO-8859-1')
        StopWords_Generic = open(f'{file_path}/StopWords_Generic.txt', 'r', encoding='ISO-8859-1')
        StopWords_GenericLong = open(f'{file_path}/StopWords_GenericLong.txt', 'r', encoding='ISO-8859-1')
        StopWords_Geographic = open(f'{file_path}/StopWords_Geographic.txt', 'r', encoding='ISO-8859-1')
        StopWords_Names = open(f'{file_path}/StopWords_Names.txt', 'r', encoding='ISO-8859-1')
        
        return stopword_auditor, StopWords_Currencies, StopWords_DatesandNumbers, StopWords_Generic, StopWords_GenericLong, StopWords_Geographic, StopWords_Names
    
    def MasterDictionar_data(self, file_path='/home/yung_nusrat/for_intern/MasterDictionary'):
        # Negative Dictionary
        file_neg = open(f'{file_path}/negative-words.txt', 'r', encoding='ISO-8859-1')
        neg_split = file_neg.read().split()
        
        # Positive Dictionary
        file_pos = open(f'{file_path}/positive-words.txt', 'r', encoding='ISO-8859-1')
        pos_split = file_pos.read().split()
        
        return pos_split, neg_split
    
    def text_corpus(self, x):
        stopword_auditor, StopWords_Currencies, StopWords_DatesandNumbers, StopWords_Generic, StopWords_GenericLong, StopWords_Geographic, StopWords_Names = self.StopWords_data()
        
        string_format = str(x).lower()
        lower_words = re.sub('[^a-zA-Z]+', ' ', string_format).strip()
        
        token = word_tokenize(lower_words)
        token_word = [t for t in token if t not in (stopword_auditor, StopWords_Currencies, StopWords_DatesandNumbers, StopWords_Generic, StopWords_GenericLong, StopWords_Geographic, StopWords_Names)]
        lemmatized = [self.lem.lemmatize(w) for w in token_word]
        
        return lemmatized
    
    def count_syllables(self, word):
        vowels = "aeiouy"
        exceptions = ["es", "ed"]
        count = 0
        previous_char_was_vowel = False
        
        for exception in exceptions:
            if word.endswith(exception):
                return 0
        
        for char in word.lower():
            if char in vowels:
                if not previous_char_was_vowel:
                    count += 1
                previous_char_was_vowel = True
            else:
                previous_char_was_vowel = False
        
        return count
    
    def calculate_complexity_percentage(self, words):
        num_complex_words = sum(1 for word in words if self.count_syllables(word) >= 2)
        total_words = len(words)
        percentage_complex_words = (num_complex_words / total_words) * 100
        
        return percentage_complex_words, num_complex_words
    
    def count_syllables_per_word(self, words):
        syllables_per_word = {word: self.count_syllables(word) for word in words}
        
        return syllables_per_word
    
    def Personal_pronoun_count(self, words_list):
        list_of_words = ['i', 'we', 'my', 'ours', 'us']
        list_words_counts = 0
        
        for words in words_list:
            if words in list_of_words:
                list_words_counts += 1
        
        return list_words_counts
    
    def Average_Word_Length(self, words):
        count = sum(len(word) for word in words)
        avg_word_length = count / len(words)
        return avg_word_length


