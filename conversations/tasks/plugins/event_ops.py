import cfg


def get_next_10():
    import datetime

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Próximos 10 eventos: ')
    events_result = cfg.service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
    events = events_result.get('items', [])
    # delta = datetime.timedelta(hours=7)

    if not events:
        print('No se encontraron eventos.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        # start_date = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S%z')
        # print("- ",start, event['summary'], event['id'])
        print(" -", event['summary'], ":\n\t",
              event['description'], "\n\t Fecha:", start)
    print("* * * * *")
    return 'say "Muy bien, y ahora..."'


def val_date():
    from datetime import datetime, date, timezone
    import dateparser
    """
    Valida los rangos de las fechas proporcionadas por el usuario
    """

    # valid = False
    # while not valid:
    #     userIn = input("USER: ")
    #     try:
    #         # d = datetime.strptime(userIn, "%d %m %Y %H %M")
    #         d = datetime.strptime(userIn, "%d %m %Y").date()
    #         print(d)
    #         valid = True
    #     except:
    #         # print("! La fecha debe ser válida y estar en el formato dd mm aaaa HH MM\n")
    #         print("! La fecha debe ser válida y estar en el formato dd mm aaaa\n")
    # return f'set_slot newtask_date "{d}"'


    d = None
    while True:
        if d == None:
            d = str(dateparser.parse(input("USER: ")))[0:10]
            print(d)
        else: break
    return f'set_slot newtask_date "{d}"'


def create_event(ev_sum, ev_desc,ev_date):
    event = {
        'summary': ev_sum,
        'description': ev_desc,
        'start': {
            # 'dateTime': '2021-03-05T09:00:00',
            'date': ev_date,
            'timeZone': 'America/Mexico_City',
        },
        'end': {
            # 'dateTime': '2021-03-05T11:00:00',
            'date': ev_date,
            'timeZone': 'America/Mexico_City',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=1'
        ]
    }

    event = cfg.service.events().insert(calendarId='primary', body=event).execute()
    print(' -Enlace al evento: %s' % (event.get('htmlLink')))
    return f'say "Muy bien, y ahora..."'


def create():
    event = {
        'summary': 'Reunión de colaboradores',
        # 'location': 'Calle 20-1 Col. X, Municipio, Estado',
        'description': 'Reunión con colaboradores',
        'start': {
            'dateTime': '2021-02-19T09:00:00-07:00',
            'timeZone': 'America/Mexico_City',
        },
        'end': {
            'dateTime': '2021-02-19T17:00:00-07:00',
            'timeZone': 'America/Mexico_City',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=1'
        ],
        'attendees': [
            {'email': 'lpage@example.com'},
            {'email': 'sbrin@example.com'},
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    event = cfg.service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))


def fun_aux2():
    cfg.aux = ":v"
    return f'say "DESDE EVENT OPS {cfg.aux}"'


if __name__ == '__main__':
    pass  # get_next_10()
