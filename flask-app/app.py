from flask import Flask, render_template
import urllib.request,json
app = Flask (__name__)

@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url) 
    data = response.read()
    characters_dict = json.loads(data)

    return render_template("characters.html", characters_list=characters_dict["results"])

@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url) 
    data = response.read()
    characters_dict = json.loads(data)

    return render_template("profile.html", profile=characters_dict)

@app.route ('/lista')
def get_list_characters(): #resultado da busca
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url) #acesso a url
    characters_data = response.read() # lê os characteres
    characters_dict = json.loads(characters_data) # carrega os characteres através do json

    characters_list = [] #lista os characteres

    for character in characters_dict["results"]: #loop para iterar os nomes e status
        character = {
            "name": character["name"],
            "status": character["status"]
        }

        characters_list.append(character)

    return{"characters":characters_list}