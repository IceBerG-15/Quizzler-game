import requests

api_link='https://opentdb.com/api.php?amount=10&category=18&type=boolean'
response = requests.get(api_link)
question_data=response.json()['results']





