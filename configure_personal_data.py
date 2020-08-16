import spotipy.util as util

username = 'henryctheo'
client_id ='8a22b2b52abc44a3bb7349ed82328eb9'
client_secret = '48a2a3cb77b24d268622d9d56a4b8b23'
redirect_uri = 'http://localhost:7777/callback'
scope = 'user-read-recently-played'

token = util.prompt_for_user_token(username=username, 
                                   scope=scope, 
                                   client_id=client_id,   
                                   client_secret=client_secret,     
                                   redirect_uri=redirect_uri)
