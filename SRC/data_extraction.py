import pandas as pd
import numpy as np
import nltk
import time
import re
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import requests
import urllib
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import warnings
import os
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lem = WordNetLemmatizer()
nltk.data.path.append("/home/yung_nusrat/nltk_data")
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
stop_words = stopwords.words('english')

warnings.filterwarnings('ignore')

class data_ext:
    def data_path(self):
        try:
            data = pd.read_excel(os.path.join("/home/yung_nusrat/for_intern/data", "Input.xlsx"))
            print(data.head())
            return data
        except Exception as e:
            print(f'Error {e}')
    
    def fetch_url(self, url, retries=3, backoff_factor=0.3):
        for i in range(retries):
            try:
                response = requests.get(url)
                response.raise_for_status()
                return response
            except requests.exceptions.RequestException as e:
                print(f"Error fetching URL: {url} | Exception: {e}")
                if i < retries - 1:
                    time.sleep(backoff_factor * (2 ** i))
                else:
                    return None
    
    def data_extract(self):
        data = pd.read_excel('/home/yung_nusrat/for_intern/data/Input.xlsx')
        df = data.copy()
        updated_list = []
        No_Matching_Data = []
        Blank_link = {}

        for i, url in enumerate(df['URL']):
            response_code = self.fetch_url(url)
            if response_code is None:
                Blank_link[f"blackassign00{i+1}"] = url
                Blank = {
                    'URL_ID': f"blackassign00{i+1}",
                    'URL': url
                }
                No_Matching_Data.append(Blank)
                continue

            soup = bs(response_code.text, 'html.parser')
            article_title = soup.find('title').text if soup.find('title') else "No Title"
            
            all_text_element = soup.find("div", class_="td-post-content tagdiv-type")
            if all_text_element is not None:
                all_text = all_text_element.get_text(strip=True, separator='\n')
                firstdata = all_text.splitlines()
            else:
                print(f"No matching element found in the HTML for URL: {url}")
                firstdata = []
                Blank_link[f"blackassign00{i+1}"] = url        
                Blank = {
                    'URL_ID': f"blackassign00{i+1}",
                    'URL': url
                }
                No_Matching_Data.append(Blank)
                
            new_dataframe = {
                "URL_ID": df["URL_ID"][i],
                'URL': url,
                'article_words': f"{article_title} - {firstdata}"
            }
            
            updated_list.append(new_dataframe)

            filename = urllib.parse.quote_plus(url)
            file_path = '/home/yung_nusrat/for_intern/text_files'
            file_full_path = os.path.join(file_path, f"{filename}.txt")
                
            with open(file_full_path, 'w+', encoding='utf-8') as file1:
                file1.writelines(article_title)
                file1.writelines(" ")
                file1.writelines(firstdata if firstdata else 'No data found')

        return pd.DataFrame(updated_list), No_Matching_Data
    
    def Handdle_Blank_link(self, blank_data):
        updated_list = []
        
        for item in blank_data:
            i = item['URL_ID']
            j = item['URL']
            response_code = self.fetch_url(j)
            if response_code is None:
                print(f"Failed to fetch data for URL: {j}")
                continue
                
            soup = bs(response_code.text, 'html.parser')
            article_title = soup.find('title').text if soup.find('title') else "No Title"
            alldiv = soup.find("div", class_="td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type")
            
            if alldiv is not None:
                firstdata = alldiv.get_text(strip=True, separator='\n')
                filename = urllib.parse.quote_plus(j)
                
                file_path = '/home/yung_nusrat/for_intern/text_files'
                file_full_path = os.path.join(file_path, f"{filename}.txt")
                
                with open(file_full_path, 'w+', encoding='utf-8') as file1:
                    file1.writelines(article_title)
                    file1.writelines(" ")
                    file1.writelines(firstdata)             
                
                updated_dict = {
                    'URL_ID': i,
                    'URL': j,
                    'article_words': f"{article_title} - {firstdata}"
                }
                updated_list.append(updated_dict)
            else:
                print(f"No data available for the link: {j}")
        
        return pd.DataFrame(updated_list)
    
    def merged(self, df1, df2):
        if df2.empty:
            # If df2 is empty, create an empty DataFrame with the same columns as df1
            df2 = pd.DataFrame(columns=['URL_ID', 'URL', 'article_words'])
        merged_df = pd.merge(df1, df2, on=['URL_ID', 'URL'], how='left')
        merged_df = merged_df.dropna()
        merged_df.reset_index(drop=True, inplace=True)
        file_path = '/home/yung_nusrat/for_intern/data/final.csv'
        merged_df.to_csv(file_path, index=False)
        return merged_df
