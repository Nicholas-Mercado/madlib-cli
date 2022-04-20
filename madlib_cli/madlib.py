import re
def read_template(file):
    try:
        with open(file) as f:
            content = f.read().strip()
            return content
    except FileNotFoundError as e:
        print('Sorry, could not find that file', e)
        raise

def parse_template():
    
    pass


def merge():
    pass

def welcome():
    print("Welcome to My Madlibs")
