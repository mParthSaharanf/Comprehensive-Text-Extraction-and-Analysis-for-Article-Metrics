# Comprehensive-Text-Extraction-and-Analysis-for-Article-Metrics

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

## License

This project is licensed under the MIT License.

