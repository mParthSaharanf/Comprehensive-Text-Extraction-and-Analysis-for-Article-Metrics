# Comprehensive-Text-Extraction-and-Analysis-for-Article-Metrics

## Project Overview
The objective of this project is to extract textual data from given URLs and perform text analysis to compute various metrics. The analysis includes sentiment analysis, word complexity, and average word length. The results are saved in text files and a final CSV file.

## Approach
Data Extraction

    Read Input Data:
        Load the URLs from an Excel file located at /home/yung_nusrat/for_intern/data/Input.xlsx.

    Scrape Articles:
        For each URL, use the requests library to fetch the web page content and BeautifulSoup to parse the HTML.
        Extract the article text from specific HTML elements.

Handle Blank Links

    Identify Missing Data:
        Check if the expected HTML elements are missing. If so, log these URLs for further processing.

    Attempt Alternative Extraction:
        Reattempt data extraction for URLs with missing data using different HTML elements or methods.

Text Preprocessing

    Tokenization:
        Tokenize the text into words using NLTK's word_tokenize.

    Stopwords Removal:
        Remove common English stopwords using NLTK's stopword list.

    Lemmatization:
        Lemmatize tokens to their base form using NLTK's WordNetLemmatizer.

Text Analysis

    Sentiment Analysis:
        Use predefined positive and negative word lists to calculate sentiment scores.

    Word Complexity:
        Calculate the percentage of complex words (words with more than two syllables).

    Average Word Length:
        Compute the average length of words in the text.

Saving Results

    Text Files:
        Save the extracted articles as text files in the /home/yung_nusrat/for_intern/text_files directory.

    CSV File:
        Save the final analysis results in a CSV file located at /home/yung_nusrat/for_intern/data/final.csv.

## Prerequisites

Ensure you have Python 3.x installed. This project uses several Python libraries, listed in `requirements.txt`.

## Setup

1. **Clone the Repository**:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create and Activate Virtual Environment (Optional but recommended)**:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Download NLTK Data**:
    Open a Python shell and run:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    ```

## Running the Project

1. **Ensure the Excel file `Input.xlsx` is placed in the `data` directory.**

2. **Run the Main Script**:
    ```bash
    python3 training.py
    ```

3. **Outputs**:
    - Extracted text files will be saved in the `text_files` directory.
    - The final merged CSV file will be saved in the `data` directory as `final.csv`.

## Dependencies

- beautifulsoup4==4.9.3
- nltk==3.5
- numpy==1.19.5
- pandas==1.2.1
- requests==2.25.1
- urllib3==1.26.5

These dependencies are also listed in the `requirements.txt` file.

## Notes

- Make sure you have a stable internet connection while running the script, as it involves fetching data from the provided URLs.
- If you encounter any issues, check the error messages and ensure that all dependencies are installed correctly.



