##
## EPITECH PROJECT, 2023
## getNieAppointment
## File description:
## timeIpChange
##

import requests
from time import time, sleep

def getIpAdresse():
    r = requests.get('http://ifconfig.me')
    return (r.text)

def getExecutionTime(debut, fin):
    temps_execution = fin - debut
    heures = int(temps_execution // 3600)
    minutes = int((temps_execution % 3600) // 60)
    secondes = int(temps_execution % 60)
    heures = int(temps_execution // 3600)
    minutes = int((temps_execution % 3600) // 60)
    secondes = int(temps_execution % 60)
    print("Execution time: {}h {}m {}s".format(heures, minutes, secondes))

def main():
    actualAdress = getIpAdresse()
    print("Actual IP adress: {}".format(actualAdress))
    address = getIpAdresse()
    debut = time()
    while (address == actualAdress):
        address = getIpAdresse()
        sleep(3)
    fin = time()
    print("IP adress changed from {} to {}".format(actualAdress, address))
    getExecutionTime(debut, fin)

if __name__ == "__main__":
    main()