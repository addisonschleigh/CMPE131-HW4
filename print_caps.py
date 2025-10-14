def allcaps(text):
    def wrapper():
        result = text()
        return result.upper()
    return wrapper