from typing import Optional
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return { "time": datetime.now() }

@app.get("/phonebook/{name}")
def read_item(name: str):
    if name in phonebook:
        return {"name": name, "phone_number": phonebook[name]}
    else:
        return {"name": name, "phone_number": "number not found!"}

phonebook = {"neha" : "609-123-1456", "max" : "487-290-9784", "bob" : "347-986-0218"}

@app.get("/songdirectory/{name}")
def read_item(name: str):
    return {f'{songs[name][0]} was made in {songs[name][1]} and was a part of the {songs[name][2]} album'}

songs = {"WayV" : ["MoonWalk", "2019", "Take Over the Moon"], "Taemin" : ["Criminal", "2020", "Never Gonna Dance Again"], "Witcher" : ["Toss a Coin to Your Witcher", "2020", "The Witcher"]}

@app.get("/palindrome/{name}")
def read_item(name: str):
    if name == name[::-1]:
        return {f'{name} is a palindrome'}
    else:
        return {f'{name} is not a palindrome :('}
