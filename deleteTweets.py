import tweepy
from datetime import datetime

# Credenciales de la API de Twitter
API_KEY = "YOUR_API_KEY"
API_SECRET_KEY = "YOUR_API_SECRET_KEY"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"

# Autenticación con Tweepy
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Verifica la conexión
try:
    api.verify_credentials()
    print("Autenticación exitosa")
except Exception as e:
    print(f"Error de autenticación: {e}")
    exit()

# Fecha límite (tweets anteriores a esta serán eliminados)
DELETE_BEFORE_DATE = datetime(2019, 1, 1)

# Eliminar tweets anteriores a una fecha específica
def delete_tweets_before_date():
    try:
        # Obtén los tweets de tu cuenta
        tweets = api.user_timeline(count=200, tweet_mode="extended")

        while len(tweets) > 0:
            for tweet in tweets:
                # Convierte la fecha del tweet a un objeto datetime
                tweet_date = tweet.created_at
                
                # Comprueba si el tweet es anterior a la fecha límite
                if tweet_date < DELETE_BEFORE_DATE:
                    try:
                        api.destroy_status(tweet.id)
                        print(f"Tweet eliminado: {tweet.id} | Fecha: {tweet_date}")
                    except Exception as e:
                        print(f"Error al eliminar tweet {tweet.id}: {e}")
                else:
                    print(f"Tweet conservado: {tweet.id} | Fecha: {tweet_date}")
            
            # Vuelve a obtener los tweets restantes
            tweets = api.user_timeline(count=200, tweet_mode="extended")
        
        print("¡Los tweets anteriores a la fecha especificada han sido eliminados!")
    except Exception as e:
        print(f"Error al obtener o eliminar tweets: {e}")

# Llama a la función
delete_tweets_before_date()
