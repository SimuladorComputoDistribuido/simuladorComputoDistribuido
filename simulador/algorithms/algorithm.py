import simpy

def pop(process):
    '''Algoritmo: El proceso espera cada dos unidades de tiempo, e imprime "POP"

    Args:
        process: el proceso que maneja el algoritmo.
    '''
    while True:
        process.show("START")
        yield process.wait(2)
        process.show("POP")

def ping(process):
    '''Algoritmo: El proceso hace "PING" y manda un mensaje a sus vecinos,
    espera después respuesta.

    Args:
        process: el proceso que maneja el algoritmo.
    '''
    while True:
        process.show("PING")
        process.send_all("<OK-F>")
        try:
            yield process.wait()
        except simpy.Interrupt as msg:
            process.show("RE " + msg.cause)

def pong(process):
    '''Algoritmo: El proceso espera a recibir mensaje, al hacerlo, hace "PONG"
        y manda un mensaje a sus vecinos.

    Args:
        process: el proceso que maneja el algoritmo.
    '''
    while True:
        try:
            yield process.wait()
        except simpy.Interrupt as msg:
            process.show("PONG " + msg.cause)
            process.send_all("Backward")

def simple_flood_leader(process):
    '''Algoritmo: Versión simple (para líder) de algoritmo de inundación.

    Args:
        process: el proceso que maneja el algoritmo.
    '''
    process.show("SENT <M>")
    process.send_all("<M>")
    try:
        yield process.wait()
    except simpy.Interrupt as msg:
        pass

def simple_flood(process):
    '''Algoritmo: Versión simple de algoritmo de inundación.

    Args:
        process: el proceso que maneja el algoritmo.
    '''
    flag = False
    while True:
        try:
            yield process.wait()
        except simpy.Interrupt as msg:
            if not flag:
                process.show("RE " + msg.cause)
                process.send_all("<M>")
                flag = True
