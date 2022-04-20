import re


def read_template(file):
    try:
        with open(file) as f:
            content = f.read().strip()
            return content
    except FileNotFoundError as e:
        print('Sorry, could not find that file', e)
        raise


def parse_template(template_string):
    # couldnt figure out how to get the brakects to include
    # pattern_outer = "(.*?)\{.*?\}'"
    # results_outer = re.sub(r"\{[^)]*\}", "", templet_string)

    pattern_inside_bracket = "{(.*?)}"
    results_inside_bracket = tuple(re.findall(
        pattern_inside_bracket, template_string))
    # print(results_inside_bracket)

    # Lauren Murphy helped me with this code
    stripped_str = template_string
    for word in results_inside_bracket:
        stripped_str = stripped_str.replace(word, "", 1)

    return(stripped_str, results_inside_bracket)


def merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    pass


def welcome():
    print("Welcome to My Madlibs")


parse_template('It was a {Adjective} and {Adjective} {Noun}.')
