import time

def timestamp(msg):
    def wrapper(*args, **kwargs):
        print(time.ctime())
        return msg(*args, **kwargs)
    return wrapper