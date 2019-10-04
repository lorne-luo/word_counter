import operator
import os
from collections import defaultdict

import click
import spacy

nlp = spacy.load('en_core_web_sm')


def validate_file(file_path):
    """validate input file existed"""

    if not os.path.isfile(file_path):
        return None
    return file_path


def read_line(file):
    """Generator to read a large file lazily"""
    while True:
        line = file.readline()
        if not line:
            break
        yield line


@click.command()
@click.argument('filename', nargs=1)
@click.option('--minimum', default=0, help='minimum count of words')
@click.option('--stop_words', default='', help='stop words will be ignored, split by comma')
def main(filename, minimum, stop_words):
    # verify input filename
    file_path = validate_file(filename)
    if not file_path:
        print('Please input a valid relative filename or absolute path.')
        return

    # clean up stop words
    stop_words = stop_words.split(',')
    stop_words = [x.strip() for x in stop_words]

    result = defaultdict(int)

    # read file
    with open(filename) as file_handler:
        for line in read_line(file_handler):
            # skip blank line
            if not line:
                continue

            doc = nlp(line)
            for token in doc:
                # punctutation, space, line change will be ignore
                if token.is_punct or token.is_space:
                    continue

                word = token.text.lower()
                # skip stop words
                if word in stop_words:
                    continue
                result[word] += 1

    # sort by count
    sorted_x = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
    
    for word, count in sorted_x:
        if count > minimum:
            print(word, count)


if __name__ == "__main__":
    main()
