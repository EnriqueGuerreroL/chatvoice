from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import event_ops, cfg


# Si se modifica SCOPES, eliminar el archivo token.pickle
SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():
    """
    Login en Google
    """
    
    creds = None
    # token.pickle almacena los access y refresh tokens del usuario, se crea
    # automáticamente cuando el flujo de autorización se completa por primera vez.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # Si no hay credenciales válidas disponibles, el usuario debe iniciar sesión.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Guarda las credenciales para próximas ejecuciones
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    # A través del objeto service se tiene acceso a los recursos que
    # se exponen con la API
    cfg.service = build('calendar', 'v3', credentials=creds)
    return 'say "Autenticando..."'


if __name__ == '__main__':
    main()