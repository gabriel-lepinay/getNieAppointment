##
## Gabriel Lepinay, 2023
## getNieAppointment
## File description:
## main
##

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def loadingDrivers():
    print("Loading drivers...", end=" ")
    try:
        driver = webdriver.Firefox()
    except Exception as e:
        print("Failed.\n", e)
        return None
    print("Success.")
    return driver

def openWebsite(driver, url):
    print("Opening website...", end=" ")
    try:
        driver.get(url)
    except Exception as e:
        print("Failed.\n", e)
        return False
    print("Success.")
    return True

def fillForm(driver, id, input):
    form_field = driver.find_element(By.ID, id)
    form_field.send_keys(input)

def clickButton(driver, id):
    button = driver.find_element(By.ID, id)
    button.click()

def getStatus(driver):
    status = driver.find_element(By.CLASS_NAME, "mf-msg__info")
    print(status.text)

def scrollToID(driver, id):
    element = driver.find_element(By.ID, id)
    driver.execute_script("arguments[0].scrollIntoView();", element)

def main(args):
    driver = loadingDrivers()
    if driver == None:
        sys.exit(84)
    if openWebsite(driver, "https://icp.administracionelectronica.gob.es/icpplustieb/index") == False:
        sys.exit(84)

    fillForm(driver, "form", "Barcelona")
    sleep(1)
    clickButton(driver, "btnAceptar")

    fillForm(driver, "tramiteGrupo[0]", "POLICIA-CERTIFICADOS Y ASIGNACION NIE")
    sleep(1)
    scrollToID(driver, "portadaForm")
    sleep(0.5)
    clickButton(driver, "btnAceptar")

    scrollToID(driver, "btnEntrar")
    sleep(0.5)
    clickButton(driver, "btnEntrar")

    clickButton(driver, "rdbTipoDocPas")
    sleep(0.5)
    fillForm(driver, "txtIdCitado", args[1]) # Passport id
    sleep(1)
    fillForm(driver, "txtDesCitado", " ".join(sys.argv[2:])) # Complete name
    sleep(1)
    scrollToID(driver, "btnEnviar")
    clickButton(driver, "btnEnviar")

    sleep(2)
    scrollToID(driver, "btnEnviar")
    clickButton(driver, "btnEnviar")
    sourceCode = driver.page_source
    no_appointment = "En este momento no hay citas disponibles"
    with open("code.html", "+w", encoding="utf-8") as fichier:
        if no_appointment not in sourceCode:
            print("Appointment available.")
            fichier.write(sourceCode)
            while (1):
                continue
        else:
            print("No appointment available.")
            driver.close()
            driver.quit()
    sleep(2)
    fichier.close()

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        print("Usage:\n\tpython3 getnie.py <passport_id> <complete_name>\nExample:\n\tpython3 getnie.py 74QM70193 Mobi Jeffrey Glaçons")
        sys.exit(0)
    if len(sys.argv) < 3:
        print("Argument error. Use -h for help.")
        sys.exit(84)
    main(sys.argv)