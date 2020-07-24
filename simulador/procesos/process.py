import simpy

class Process(object):
    '''
    Clase para modelar procesos.

    Args:
        sys: el sistema al cual pertenece el proceso.
        name: el nombre del proceso.
        blackbox: la sección de código que determina el comportamiento del
            proceso.
    '''

    def __init__(self, sys, name, blackbox):
        self.sys = sys
        self.env = sys.env
        self.name = name
        self.neighbors = None
        self.blackbox = blackbox
        self.action = self.env.process(self.blackbox(self))

    def set_neighbors(self, neighbors):
        '''Establece los vecinos de un proceso

        Args:
            neighbors: un diccionario con los vecinos del proceso
        '''
        self.neighbors = neighbors

    def send_all(self, message):
        '''Envía un mensaje a todos los vecinos del proceso.

        Args:
            message: el mensaje a enviar.
        '''
        for process in self.neighbors:
            self.sys.deliver(message, process)

    def wait_to_infinity(self):
        '''[Auxiliar] Hace que el proceso espere indefinidamente.'''
        yield self.env.timeout(simpy.core.Infinity)

    def wait_time(self, time):
        '''[Auxiliar] Hace que el proceso espere un tiempo determinado.

        Args:
            time: el tiempo que el proceso debe esperar.
        '''
        yield self.env.timeout(time)

    def wait(self, time=None):
        '''Hace que el proceso espere cierto tiempo. Si no se especifica un
        tiempo, el proceso esperará indefinidamente.

        Args:
            time: (opcional) el tiempo a esperar.
        '''
        if time is None:
            return self.env.process(self.wait_to_infinity())
        else:
            return self.env.process(self.wait_time(time))

    def show(self, message):
        '''Imprime en consola un cierto mensaje, con el nombre del proceso
        y el tiempo actual del entorno.

        Args:
            message: el mensaje a imprimir.
        '''
        print('Process %s | %s | at t=%d' % (self.name, message, self.env.now))

    def __str__(self):
        return self.name
