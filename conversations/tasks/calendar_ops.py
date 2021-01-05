# from googleapiclient.discovery import build

def get_meta(service):
    calendar = service.calendars().get(calendarId='primary').execute()
    print(calendar['id'])
    print(calendar['kind'])

