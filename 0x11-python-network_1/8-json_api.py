#!/usr/bin/python3
''' script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
import requests
import sys


if __name__ == "__main__":
    letter ="" if len(sys.argv) == 1 else sys.argv[1]
    payload = {'q': letter}
        q = sys.argv[1]
    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        json_response = response.json()
        if json_response == {}:
            print('No result')
        else:
            print('[{}] {}'.format(json_response.get('id'), json_reponse.get('name')))

    except ValueError:
        print('Not a valid JSON')
