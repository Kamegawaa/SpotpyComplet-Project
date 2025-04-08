import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

def init_spotify():
    client_id = os.getenv("373d93278b914791ac10362cf36158ef")
    client_secret = os.getenv("cd1af896d41e4966aa6f742542783a1c")

    if not client_id or not client_secret:
        raise Exception("Credenciais não encontradas. Verifique seu .env")

    auth_manager = SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp
