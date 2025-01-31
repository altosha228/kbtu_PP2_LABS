# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]



def isRatingAbove5(name):
  selectedMovie = None
  for movie in movies:
    if movie["name"] == name:
      selectedMovie = movie
  if selectedMovie == None:
    print("No movie with name " + name)
  else:
    if selectedMovie["imdb"] > 5.5:
      print(True)
    else:
      print(False)

isRatingAbove5("AlphaJet")
isRatingAbove5("Joking muck")


def getSublistOfRatingAbove5(list):
  newList = [movie for movie in list if movie["imdb"] > 5.5]
  return newList

sublist = getSublistOfRatingAbove5(movies)
# print(sublist)


def getSublistOfCategory(list, categoryName):
  newList = [movie for movie in list if movie["category"] == categoryName]
  return newList
# print(getSublistOfCategory(movies, "Romance"))

def calculateAverage(list):
  sum = 0
  cnt = 0
  for movie in movies:
    sum += movie["imdb"]
    cnt = cnt + 1
  return sum / cnt
# print(calculateAverage(movies))

def calculateAverageInCategory(list, categoryName):
  sum = 0
  cnt = 0
  for movie in movies:
    if movie["category"] == categoryName:
      sum += movie["imdb"]
      cnt = cnt + 1
  return sum / cnt

print(calculateAverageInCategory(movies, "Thriller"))