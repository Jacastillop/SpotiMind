import spotipy
import spotipy.util as util
import pandas as pd


# Solicita las credenciales de Spotify
username = "u1t6q502i3pyg7zktsi029nnf"
scope = "user-top-read"
client_id = "c0106e614a6e4d2ebca46fd5401e7be4"
client_secret = "dfb41a1a744f416db305ca6185074c2d"
redirect_uri = "http://localhost:8080"

# Obtiene un token de acceso
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

# Crea una instancia de la clase Spotipy
sp = spotipy.Spotify(auth=token)

# Hace una búsqueda en la API de Spotify
top50 = sp.current_user_top_tracks(time_range='short_term', limit=50)

tracks = top50['items']
track_ids = []
track_names = []
features = []

for track in tracks:
    track_id = track['id']
    track_name = track['name']
    audio_features = sp.audio_features(track_id)
    
    track_ids.append(track_id)
    track_names.append(track_name)
    features.append(audio_features[0])
    
top50_df = pd.DataFrame(features,index = track_names)

print(top50_df.to_markdown())
    
for i, item in enumerate(top50['items'],1):
    print(i, item['name'], '//', item['artists'][0]['name'])
