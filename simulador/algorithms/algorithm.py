import simpy

def sample(process):
    while True:
        print('Time at %d' % process.env.now)
        time = 1
        yield process.env.timeout(time)
        print('Ping at %d' % process.env.now)

def ping(process):
    while True:
        print('Ping %s at t=%d' % (process.name, process.env.now))
        process.send_all("Forward")
        try:
            yield process.env.process(process.wait())
        except simpy.Interrupt as msg:
            print('RECEIVED %s , msg: %s at t=%d' % (process.name, msg.cause, process.env.now))

def pong(process):
    while True:
        #print('Waiting %s ' % process.name)
        try:
            yield process.env.process(process.wait())
        except simpy.Interrupt as msg:
            print('Pong %s , msg: %s at t=%d' % (process.name, msg.cause, process.env.now))
            process.send_all("Backward")

def simple_flood_leader(process):
    while True:
        send_all("v")

def simple_flood(process):
    flag = False
    while True:
        try:
            yield process.env.process(process.wait())
        except simpy.Interrupt as msg:
            print('Pong %s , msg: %s at t=%d' % (process.name, msg.cause, process.env.now))
            process.send_all("Backward")
