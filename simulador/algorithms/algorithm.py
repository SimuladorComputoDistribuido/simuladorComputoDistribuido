import simpy

def pop(process):
    while True:
        process.show("START")
        yield process.wait(2)
        process.show("POP")

def ping(process):
    while True:
        process.show("PING")
        process.send_all("<OK-F>")
        try:
            yield process.wait()
        except simpy.Interrupt as msg:
            process.show("RE " + msg.cause)

def pong(process):
    while True:
        try:
            yield process.wait()
        except simpy.Interrupt as msg:
            process.show("PONG " + msg.cause)
            process.send_all("Backward")

def simple_flood_leader(process):
    process.show("SENT <M>")
    process.send_all("<M>")
    try:
        yield process.wait()
    except simpy.Interrupt as msg:
        pass

def simple_flood(process):
    flag = False
    while True:
        try:
            yield process.wait()
        except simpy.Interrupt as msg:
            if not flag:
                process.show("RE " + msg.cause)
                process.send_all("<M>")
                flag = True
