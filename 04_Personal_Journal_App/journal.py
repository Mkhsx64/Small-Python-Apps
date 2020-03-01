import os


def load(name):
    return []


def save(name, journal_data):
    filename = os.path.abspath(os.path.join('./journals', name + '.jrl'))
    print('would load from here {}'.format(filename))
    #fout = open(filename, 'w')


def add_entry(text, journal_data):
    journal_data.append(text)

