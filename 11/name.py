import requests

res = requests.get('https://www.gutenberg.org/files/27062/27062-0.txt')
type(res)
print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:250])