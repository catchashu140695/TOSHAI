import json

json_data = '''[
  {
    "title": "Epic Fail Compilation: Hilarious Moments Caught on Camera!",
    "description": "Watch these epic fails and laugh out loud! From funny accidents to unexpected mishaps, this compilation will keep you entertained. #shorts #youtube #youtubeshorts #funny #fails #epic #hilarious #comedy",
    "tags": "#shorts #youtube #youtubeshorts #funny #fails #epic #hilarious #comedy"
  },
  {
    "title": "Crazy Cats Doing Ridiculous Things!",
    "description": "Get ready to laugh with these crazy cats! From ninja-like moves to hilarious antics, this compilation is guaranteed to make you smile. #shorts #youtube #youtubeshorts #funny #cats #crazycats #animalcomedy #petantics",
    "tags": "#shorts #youtube #youtubeshorts #funny #cats #crazycats #animalcomedy #petantics"
  },
  {
    "title": "Unexpected Dance Battles in Public Places!",
    "description": "You won't believe your eyes with these unexpected dance battles! From street corners to shopping malls, watch people break into dance and bring smiles to everyone around. #shorts #youtube #youtubeshorts #funny #dance #dancing #publicdance #dancebattle #unexpected",
    "tags": "#shorts #youtube #youtubeshorts #funny #dance #dancing #publicdance #dancebattle #unexpected"
  },
  {
    "title": "Hilarious Kids' Reactions to Everyday Situations!",
    "description": "Kids say and do the funniest things! Watch as these kids react to everyday situations with pure innocence and hilarity. #shorts #youtube #youtubeshorts #funny #kids #reactions #innocence #comedy",
    "tags": "#shorts #youtube #youtubeshorts #funny #kids #reactions #innocence #comedy"
  },
  {
    "title": "Funny Dog Fails That Will Make Your Day!",
    "description": "You can't help but laugh at these funny dog fails! From clumsy puppies to mischievous dogs, this compilation is a guaranteed mood-booster. #shorts #youtube #youtubeshorts #funny #dogs #dogfails #puppyfails #animalcomedy",
    "tags": "#shorts #youtube #youtubeshorts #funny #dogs #dogfails #puppyfails #animalcomedy"
  }
]'''

videos = json.loads(json_data)

for video in videos:
    print("Title:", video["title"])
    print("Description:", video["description"])
    print("Tags:", video["tags"])
    print()
