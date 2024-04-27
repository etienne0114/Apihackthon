import requests
from django.shortcuts import render

#using api


#using api
#fetch javascript object notation
#fetch json data
def home(request):
  response = requests.get("https://api.github.com/users/octocat")
  data = response.json()
  results = {
      key: data[key]
      for key in
      ["login", "blog", "company", "email", "followers", "following"]
  }
  # Example 2
  reponse2 = requests.get('https://dog.ceo/api/breeds/image/random')
  data2 = reponse2.json()
  result2 = data2["message"]

  return render(request, 'templates/index.html', {
      'results': results,
      'result2': result2
  })
