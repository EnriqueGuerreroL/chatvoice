import cfg


def get_next_10():
    """
    Obtiene los siguientes diez registros (eventos) en el calendario de Google
    del usuario y los imprime en pantalla.
    """
    import datetime

    # Llamada API
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    print('Próximos 10 eventos: ')
    events_result = cfg.service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No se encontraron eventos.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(" -", event['summary'], ":\n\t",
              event['description'], "\n\t Fecha:", start)
    print("* * * * *")
    return 'say "Muy bien, y ahora..."'


def val_date():
    """
    Procesa la fecha que ingresa el usuario para ser utilizable en la creación
    de la tarea.
    """
    from datetime import datetime
    import dateparser

    valid = False
    while not valid:
        # dateparser para recibir fecha
        date_in = str(dateparser.parse(input("USER: ")))[0:10]
        try:
            # se valida fecha
            date_in = datetime.strptime(date_in, "%Y-%m-%d").date()
            print("Fecha: ", date_in)
            valid = True
        except:
            print("¡La fecha debe ser válida!\n")
    # devuelve sentencia que reconoce el manejador de la conversación
    # se almacena la fecha en el slot dinámico newtask_date
    return f'set_slot newtask_date "{date_in}"'


def create_event(ev_sum, ev_desc, ev_date):
    """
    Crea el evento en el calendario principal de Google con los datos recibidos.
    ev_sum: título del evento
    ev_desc: descripción del evento
    ev_date: fecha del evento (sin hora)
    """
    event = {
        'summary': ev_sum,
        'description': ev_desc,
        'start': {
            'date': ev_date,
            'timeZone': 'America/Mexico_City',
        },
        'end': {
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


if __name__ == '__main__':
    pass
