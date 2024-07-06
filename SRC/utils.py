import pandas as pd
import nltk
from .structure import Analysis  

class Col_Structure:
    
    def Col_Structure_Primary(self, data):
        updated_list = []
        
        for i, j, column in zip(data['URL_ID'], data['URL'], data['article_words']):
            # Returns A tokenized Words
            preprocessed_word = Analysis().text_corpus(column)
            
            # Existing Dictionary In text file
            positive_dictionary, negative_dictionary = Analysis().MasterDictionar_data()
            
            # 1. Positive Score
            positive_count = sum(1 for ps_words in preprocessed_word if ps_words in positive_dictionary)
            positive_score = positive_count
            
            # 2. Negative Score
            negative_count = sum(1 for ng_words in preprocessed_word if ng_words in negative_dictionary)
            negative_score = negative_count
            
            # 3. Polarity Score
            polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001 )
            
            # 4. Subjective Score
            subjective_score = (positive_score + negative_score) / ((len(preprocessed_word)) + 0.000001 )
            
            # 5. Average Sentence Length
            total_sentences = len(nltk.tokenize.sent_tokenize(column))
            avg_sentence_length = round(len(preprocessed_word) / total_sentences, 0)
            
            # 6. Percentage of complex words and 9. Complex Word Count
            Percentage_of_Complex_words, total_num_of_complex_words_count = Analysis().calculate_complexity_percentage(preprocessed_word)
            
            # 7. Fog Index
            FOG_Index = 0.4 * (avg_sentence_length + Percentage_of_Complex_words)
            
            # 8. Average Number of Words Per Sentence
            Average_Number_of_Words_Per_Sentence = round(len(column.split()) / total_sentences, 0)
            
            # 10. Word Count
            Word_Count = len(preprocessed_word)
            
            # 11. Syllable Per Word
            syllable_per_word = Analysis().count_syllables_per_word(preprocessed_word)
            
            # 12. Personal Pronouns
            personal_pronouns = Analysis().Personal_pronoun_count(preprocessed_word)
            
            # 13. Average Word Length
            word_length = Analysis().Average_Word_Length(preprocessed_word)
            avg_word_length = round(word_length / len(preprocessed_word), 0)
            
            final_dict = {
                'URL_ID'                            : i,
                'URL'                               : j,
                'article_words'                     : column,
                'POSITIVE_SCORE'                    : positive_score,
                'NEGATIVE_SCORE'                    : negative_score,
                'POLARITY_SCORE'                    : polarity_score,
                'SUBJECTIVITY_SCORE'                : subjective_score,
                'AVG_SENTENCE_LENGTH'               : avg_sentence_length,
                'PERCENTAGE_OF_COMPLEX_WORDS'       : Percentage_of_Complex_words,
                'FOG_INDEX'                         : FOG_Index,
                'AVG_NUMBER_OF_WORDS_PER_SENTENCE'  : Average_Number_of_Words_Per_Sentence,
                'COMPLEX_WORD_COUNT'                : total_num_of_complex_words_count,
                'WORD_COUNT'                        : Word_Count,
                'SYLLABLE_PER_WORD'                 : syllable_per_word,
                'PERSONAL_PRONOUNS'                 : personal_pronouns,
                'AVG_WORD_LENGTH'                   : avg_word_length
            }
            updated_list.append(final_dict)
            
        df = pd.DataFrame(updated_list)
        output_file = "/home/yung_nusrat/for_intern/data/Output.csv"  
        df.to_csv(output_file, index=False)
        
        return df
