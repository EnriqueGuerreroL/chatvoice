from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import calendar_ops, event_ops

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    
    return service

    # tecla = 1010
    # while tecla != 0:
    #     tecla = int(input("ingresa tecla: "))
    #     if (tecla == 1): # escribir nuevo evento
    #         print(tecla)
    #     if tecla == 2: # traer metadatos de calendario
    #         # calendar = service.calendars().get(calendarId='primary').execute()

    #         # print(calendar['summary'])
    #         calendar_ops.get_meta()


if __name__ == '__main__':
    service = main()
    # calendar_ops.get_meta(service)
    # event_ops.create(service)
    event_ops.get_next_10(service)