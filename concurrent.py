from threading import Thread


def startThread(func, arg):
    t = Thread(target = func, args=(arg,))
    t.daemon = True
    t.start()
