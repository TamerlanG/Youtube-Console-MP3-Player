from __future__ import print_function, unicode_literals

from PyInquirer import prompt

from api import search
from player import play_song
from pyfiglet import Figlet

from config import command_style

EXIT_TOGGLE = False


def main():
    questions = [
        {
            'type': 'input',
            'name': 'query',
            'message': 'Search:',
        }
    ]

    query = prompt(questions, style=command_style)

    search_results = search(query.get("query"))

    choice = list_search_results(search_results)

    play_song(choice['search'])

    return prompt_to_continue()


def list_search_results(search_list):
    questions = [
        {
            'type': 'list',
            'name': 'search',
            'message': 'Search Results:',
            'choices': search_list,
        },
    ]

    answer = prompt(questions, style=command_style)

    return answer


def prompt_to_continue():
    questions = [
        {
            'type': 'confirm',
            'message': 'Do you want to continue?',
            'name': 'continue',
            'default': True,
        },
    ]

    answer = prompt(questions, style=command_style)

    return not answer['continue']


if __name__ == '__main__':
    # Big Header
    f = Figlet(font='slant')
    print(f.renderText('MP3 Player'))

    # Main Life Cycle Loop
    while True:

        if EXIT_TOGGLE:
            break

        EXIT_TOGGLE = main()

    print("Thanks for using!!")
