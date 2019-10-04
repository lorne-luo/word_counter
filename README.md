# Tennis Calculator

This project could report word frequencies of given file. 

## Requirements

This project require Python version 3.6 or above due to used [f-string formatting](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) which is a new feature since Python 3.6.
- Python 3.6 or above
- Git

## Installation
Simply git clone this repo and run `main.py`
```
git clone https://github.com/lorne-luo/word_counter.git
cd word_counter
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm  # this step is important to download segment model
```

## How to run
Check options
```
>>> python main.py  --help
Usage: main.py [OPTIONS] FILENAME

Options:
  --minimum INTEGER  minimum count of words
  --stop_words TEXT  stop words will be ignored, split by comma
  --help             Show this message and exit.
```

Example:
```
python main.py demo.txt --minimum 10 --stop_words  and,it
```
 
## How to test
Simply run
```
python3 -m unittest discover
```
