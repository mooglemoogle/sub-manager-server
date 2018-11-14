from api import runApi
from db import initialize

def startDB():
    initialize()

def startServer():
    runApi()

def main():
    startDB()
    startServer()

if __name__ == "__main__":
    main()