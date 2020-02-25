from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
global website
global inlogid
global jaar
global wachtwoordid
global naamschool
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']
####################################################
####################################################
##                                                ##  
##       █   █ █▀▀ █   ▄▀ ▄▀▄ █▄ ▄█ █▀▀           ##
##       █ █ █ █▀▀ █ ▄ █  █ █ █ █ █ █▀▀           ##  
##        ▀ ▀  ▀▀▀ ▀▀▀  ▀  ▀  ▀   ▀ ▀▀▀           ##
##                                                ##
####################################################
####################################################

#This code is created in dutch because im dutch and Magister is Dutch
#Please Fil out al the FILL ME IN spots below
#Please fil in your magister Agenda wesite url (Example: https://School Name.magister.net/magister/#/agenda)
website = "[FIL ME IN]" 
#Please fil in your username below
inlogid = "[FIL ME IN]"
#Please fil in your password below
wachtwoordid = "[FIL ME IN]"
#Please fil in name of your school below
naamschool = "[FIL ME IN]"
#Please fil in the current year below
jaar = "[FIL ME IN]"
#Please fil in the start time and end time of each class hour
#Please fil in start time of class 1
btijd1 = "08:15"
#Please fil in end time of class 1
etijd1 = "09:05"
#Please fil out the rest
btijd2="09:05"
etijd2="09:55"
#
btijd3="09:55"
etijd3="10:45"
#
btijd4="11:5"
etijd4="11:55"
#
btijd5="11:55"
etijd5="12:45"
#
btijd6="13:10"
etijd6="14:10"
#
btijd7="14:10"
etijd7="15:00"
#
btijd8="15:20"
etijd8="16:10"
#
#Thats al you have to fil in. Please make sure you have python installed with the libraries(Selenium, Google calander and the driver for Selenium)
#Now your set to run the python file and transfer agendas
#
#
#Github: https://github.com/Jasper-crypto/Magister-to-google-calander-PYTHON-
#©Jasper-Crypto
#Main code by:
#©Borek Bandell 2019

def dagverkrijgen():
    global monthletter
    global dag
    global jaartal
    global datumg
    datetransfer = datumtekst.split()
    dag = datetransfer[1]
    maand = datetransfer[2]
    jaartal = jaar
    if(maand == "januari"):
        monthletter = "1"

    elif(maand == "februari"):
        monthletter = "2"

    elif(maand == "maart"):
        monthletter = "3"

    elif(maand == "april"):
        monthletter = "4"

    elif(maand == "mei"):
        monthletter = "5"

    elif(maand == "juni"):
        monthletter = "6"

    elif(maand == "juli"):
        monthletter = "7"

    elif(maand == "augustus"):
        monthletter = "8"

    elif(maand == "september"):
        monthletter = "9"

    elif(maand == "oktober"):
        monthletter = "10"

    elif(maand == "november"):
        monthletter = "11"

    elif(maand == "december"):
        monthletter = "12"
    
    jaartalg = str(jaartal)
    monthletterg = str(monthletter)
    dagg = str(dag)
    #Hoe de datum in google komt:
    datumg = jaartalg+"-"+monthletterg+"-"+dagg
    
def lesachtg():
    tijdstip = uurachttekst
    if(tijdstip == "1"):
        btijd = btijd1
        etijd = etijd1
    elif(tijdstip == "2"):
        btijd = btijd2
        etijd = etijd2
    elif(tijdstip == "3"):
        btijd = btijd3
        etijd = etijd3
    elif(tijdstip == "4"):
        btijd = btijd4
        etijd = etijd4
    elif(tijdstip == "5"):
        btijd = btijd5
        etijd = etijd5
    elif(tijdstip == "6"):
        btijd = btijd6
        etijd = etijd6
    elif(tijdstip == "7"):
        btijd = btijd7
        etijd = etijd7
    elif(tijdstip == "8"):
        btijd = btijd8
        etijd = etijd8
    
    beginacht = datumg+"T"+btijd+":00+01:00"
    eindacht= datumg+"T"+etijd+":00+01:00"
    #-
    #-
    service = build('calendar', 'v3', credentials=creds)
    #Calendar API
    event = {
      'summary': uurachttekst+ " - " + lokaalacht.text+ " - " + lesachttekst,
      'location': lokaalacht.text,
      'description': '',
      'start': {
        'dateTime': beginacht,
        'timeZone': 'Europe/Amsterdam',
      },
      'end': {
        'dateTime': eindacht,
        'timeZone': 'Europe/Amsterdam',
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Les in google gezet: '+ uurachttekst+ " - " + lokaalacht.text+ " - " + lesachttekst)
    print("Dit zijn alle lessen voor vandaag")
    print("Subscribe to Jelyko TCG")
    print("Python coded by Jelyko TCG")
    print("GitHub: ")

def lesacht():
    global lesachttekst
    global uurachttekst
    global lokaalacht
    try:
        #achtste les
        lesacht = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[9]/td[3]/span/span[2]")
        lesachttekst = lesacht.text
        uuracht = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[9]/td[3]/span/span[1]")
        uurachttekst = uuracht.text
        lokaalacht = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[9]/td[3]/span/span[3]")
        print("Achtste les: "+uurachttekst+ " - " + lokaalacht.text+ " - " + lesachttekst)
        lesachtg()
    except :
        print("Dit zijn alle lessen voor vandaag")

def leszeveng():
    tijdstip = uurzeventekst
    if(tijdstip == "1"):
        btijd = btijd1
        etijd = etijd1
    elif(tijdstip == "2"):
        btijd = btijd2
        etijd = etijd2
    elif(tijdstip == "3"):
        btijd = btijd3
        etijd = etijd3
    elif(tijdstip == "4"):
        btijd = btijd4
        etijd = etijd4
    elif(tijdstip == "5"):
        btijd = btijd5
        etijd = etijd5
    elif(tijdstip == "6"):
        btijd = btijd6
        etijd = etijd6
    elif(tijdstip == "7"):
        btijd = btijd7
        etijd = etijd7
    elif(tijdstip == "8"):
        btijd = btijd8
        etijd = etijd8
    
    beginzeven = datumg+"T"+btijd+":00+01:00"
    eindzeven= datumg+"T"+etijd+":00+01:00"
    #-
    #-
    service = build('calendar', 'v3', credentials=creds)
    #Calendar API
    event = {
      'summary': uurzeventekst+ " - " + lokaalzeven.text+ " - " + leszeventekst,
      'location': lokaalzeven.text,
      'description': '',
      'start': {
        'dateTime': beginzeven,
        'timeZone': 'Europe/Amsterdam',
      },
      'end': {
        'dateTime': eindzeven,
        'timeZone': 'Europe/Amsterdam',
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Les in google gezet: '+ uurzeventekst+ " - " + lokaalzeven.text+ " - " + leszeventekst)     

def leszeven():
    global leszeventekst
    global uurzeventekst
    global lokaalzeven
    try:
        #zevende les
        leszeven = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[8]/td[3]/span/span[2]")
        leszeventekst = leszeven.text
        uurzeven = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[8]/td[3]/span/span[1]")
        uurzeventekst = uurzeven.text
        lokaalzeven = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[8]/td[3]/span/span[3]")
        print("Zevende les: "+ uurzeventekst+ " - " + lokaalzeven.text+ " - " + leszeventekst)
        leszeveng()
        lesacht()
    except :
        print("Dit zijn alle lessen voor vandaag")
    
def leszesg():
    tijdstip = uurzestekst
    if(tijdstip == "1"):
        btijd = btijd1
        etijd = etijd1
    elif(tijdstip == "2"):
        btijd = btijd2
        etijd = etijd2
    elif(tijdstip == "3"):
        btijd = btijd3
        etijd = etijd3
    elif(tijdstip == "4"):
        btijd = btijd4
        etijd = etijd4
    elif(tijdstip == "5"):
        btijd = btijd5
        etijd = etijd5
    elif(tijdstip == "6"):
        btijd = btijd6
        etijd = etijd6
    elif(tijdstip == "7"):
        btijd = btijd7
        etijd = etijd7
    elif(tijdstip == "8"):
        btijd = btijd8
        etijd = etijd8
    
    beginzes = datumg+"T"+btijd+":00+01:00"
    eindzes= datumg+"T"+etijd+":00+01:00"
    #-
    #-
    service = build('calendar', 'v3', credentials=creds)
    #Calendar API
    event = {
      'summary': uurzestekst+ " - " + lokaalzes.text+ " - " + leszestekst,
      'location': lokaalzes.text,
      'description': '',
      'start': {
        'dateTime': beginzes,
        'timeZone': 'Europe/Amsterdam',
      },
      'end': {
        'dateTime': eindzes,
        'timeZone': 'Europe/Amsterdam',
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Les in google gezet: '+ uurzestekst+ " - " + lokaalzes.text+ " - " + leszestekst) 

def leszes():
    global leszestekst
    global uurzestekst
    global lokaalzes
    try:
        #zesde les
        leszes = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[7]/td[3]/span/span[2]")
        leszestekst = leszes.text
        uurzes = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[7]/td[3]/span/span[1]")
        uurzestekst = uurzes.text
        lokaalzes = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[7]/td[3]/span/span[3]")
        print("Zesde les:   "+ uurzestekst+ " - " + lokaalzes.text+ " - " + leszestekst)
        leszesg()
        leszeven()
    except :
        print("Dit zijn alle lessen voor vandaag")

def lesvijfg():
    tijdstip = uurvijftekst
    if(tijdstip == "1"):
        btijd = btijd1
        etijd = etijd1
    elif(tijdstip == "2"):
        btijd = btijd2
        etijd = etijd2
    elif(tijdstip == "3"):
        btijd = btijd3
        etijd = etijd3
    elif(tijdstip == "4"):
        btijd = btijd4
        etijd = etijd4
    elif(tijdstip == "5"):
        btijd = btijd5
        etijd = etijd5
    elif(tijdstip == "6"):
        btijd = btijd6
        etijd = etijd6
    elif(tijdstip == "7"):
        btijd = btijd7
        etijd = etijd7
    elif(tijdstip == "8"):
        btijd = btijd8
        etijd = etijd8
    
    beginvijf = datumg+"T"+btijd+":00+01:00"
    eindvijf= datumg+"T"+etijd+":00+01:00"
    #-
    #-
    service = build('calendar', 'v3', credentials=creds)
    #Calendar API
    event = {
      'summary': uurvijftekst+ " - " + lokaalvijf.text+ " - " + lesvijftekst,
      'location': lokaalvijf.text,
      'description': '',
      'start': {
        'dateTime': beginvijf,
        'timeZone': 'Europe/Amsterdam',
      },
      'end': {
        'dateTime': eindvijf,
        'timeZone': 'Europe/Amsterdam',
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Les in google gezet: '+ uurvijftekst+ " - " + lokaalvijf.text+ " - " + lesvijftekst)     

def lesvijf():
    global lesvijftekst
    global uurvijftekst
    global lokaalvijf
    try:
        #vijfde les
        lesvijf = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[6]/td[3]/span/span[2]")
        lesvijftekst = lesvijf.text
        uurvijf = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[6]/td[3]/span/span[1]")
        uurvijftekst = uurvijf.text
        lokaalvijf = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[6]/td[3]/span/span[3]")
        print("Vijfde les:  "+ uurvijftekst+ " - " + lokaalvijf.text+ " - " + lesvijftekst)
        lesvijfg()
        leszes()
    except :
        print("Dit zijn alle lessen voor vandaag")
        
def lesvierg():
    tijdstip = uurviertekst
    if(tijdstip == "1"):
        btijd = btijd1
        etijd = etijd1
    elif(tijdstip == "2"):
        btijd = btijd2
        etijd = etijd2
    elif(tijdstip == "3"):
        btijd = btijd3
        etijd = etijd3
    elif(tijdstip == "4"):
        btijd = btijd4
        etijd = etijd4
    elif(tijdstip == "5"):
        btijd = btijd5
        etijd = etijd5
    elif(tijdstip == "6"):
        btijd = btijd6
        etijd = etijd6
    elif(tijdstip == "7"):
        btijd = btijd7
        etijd = etijd7
    elif(tijdstip == "8"):
        btijd = btijd8
        etijd = etijd8
    
    beginvier = datumg+"T"+btijd+":00+01:00"
    eindvier= datumg+"T"+etijd+":00+01:00"
    #-
    #-
    service = build('calendar', 'v3', credentials=creds)
    #Calendar API
    event = {
      'summary': uurviertekst+ " - " + lokaalvier.text+ " - " + lesviertekst,
      'location': lokaalvier.text,
      'description': '',
      'start': {
        'dateTime': beginvier,
        'timeZone': 'Europe/Amsterdam',
      },
      'end': {
        'dateTime': eindvier,
        'timeZone': 'Europe/Amsterdam',
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Les in google gezet: '+ uurviertekst+ " - " + lokaalvier.text+ " - " + lesviertekst)    

def lesvier():
    global lesviertekst
    global uurviertekst
    global lokaalvier
    try:
        #vierde les
        lesvier = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[5]/td[3]/span/span[2]")
        lesviertekst = lesvier.text
        uurvier = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[5]/td[3]/span/span[1]")
        uurviertekst = uurvier.text
        lokaalvier = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[5]/td[3]/span/span[3]")
        print("Vierde les:  "+uurviertekst+ " - " + lokaalvier.text+ " - " + lesviertekst)
        lesvierg()
        lesvijf()
    except :
        print("Dit zijn alle lessen voor vandaag")

def lesdrieg():
    tijdstip = uurdrietekst
    if(tijdstip == "1"):
        btijd = btijd1
        etijd = etijd1
    elif(tijdstip == "2"):
        btijd = btijd2
        etijd = etijd2
    elif(tijdstip == "3"):
        btijd = btijd3
        etijd = etijd3
    elif(tijdstip == "4"):
        btijd = btijd4
        etijd = etijd4
    elif(tijdstip == "5"):
        btijd = btijd5
        etijd = etijd5
    elif(tijdstip == "6"):
        btijd = btijd6
        etijd = etijd6
    elif(tijdstip == "7"):
        btijd = btijd7
        etijd = etijd7
    elif(tijdstip == "8"):
        btijd = btijd8
        etijd = etijd8
    
    begindrie = datumg+"T"+btijd+":00+01:00"
    einddrie= datumg+"T"+etijd+":00+01:00"
    #-
    #-
    service = build('calendar', 'v3', credentials=creds)
    #Calendar API
    event = {
      'summary': uurdrietekst+ " - " + lokaaldrie.text+ " - " + lesdrietekst,
      'location': lokaaldrie.text,
      'description': '',
      'start': {
        'dateTime': begindrie,
        'timeZone': 'Europe/Amsterdam',
      },
      'end': {
        'dateTime': einddrie,
        'timeZone': 'Europe/Amsterdam',
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Les in google gezet: '+ uurdrietekst+ " - " + lokaaldrie.text+ " - " + lesdrietekst)



def lesdrie():
    global lesdrietekst
    global uurdrietekst
    global lokaaldrie
    try:
        #derde les
        lesdrie = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[4]/td[3]/span/span[2]")
        lesdrietekst = lesdrie.text
        uurdrie = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[4]/td[3]/span/span[1]")
        uurdrietekst = uurdrie.text
        lokaaldrie = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[4]/td[3]/span/span[3]")
        print("Derde  les:  "+uurdrietekst+ " - " + lokaaldrie.text+ " - " + lesdrietekst)
        lesdrieg()
        lesvier()
    except :
        print("Dit zijn alle lessen voor vandaag")

def lestweeg():
    global maand
    tijdstip = uurtweetekst
    if(tijdstip == "1"):
        btijd = btijd1
        etijd = etijd1
    elif(tijdstip == "2"):
        btijd = btijd2
        etijd = etijd2
    elif(tijdstip == "3"):
        btijd = btijd3
        etijd = etijd3
    elif(tijdstip == "4"):
        btijd = btijd4
        etijd = etijd4
    elif(tijdstip == "5"):
        btijd = btijd5
        etijd = etijd5
    elif(tijdstip == "6"):
        btijd = btijd6
        etijd = etijd6
    elif(tijdstip == "7"):
        btijd = btijd7
        etijd = etijd7
    elif(tijdstip == "8"):
        btijd = btijd8
        etijd = etijd8
    
    begintwee = datumg+"T"+btijd+":00+01:00"
    eindtwee = datumg+"T"+etijd+":00+01:00"
    #-
    #-
    service = build('calendar', 'v3', credentials=creds)
    #Calendar API
    event = {
      'summary': uurtweetekst+ " - " + lokaaltwee.text+ " - " + lestweetekst,
      'location': lokaaltwee.text,
      'description': '',
      'start': {
        'dateTime': begintwee,
        'timeZone': 'Europe/Amsterdam',
      },
      'end': {
        'dateTime': eindtwee,
        'timeZone': 'Europe/Amsterdam',
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Les in google gezet: '+ uurtweetekst+ " - " + lokaaltwee.text+ " - " + lestweetekst)


def lestwee():
    #tweede les
    global uurtweetekst
    global lestweetekst
    global lokaaltwee
    lestwee = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[3]/td[3]/span/span[2]")
    lestweetekst = lestwee.text
    uurtwee = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[3]/td[3]/span/span[1]")
    uurtweetekst = uurtwee.text
    lokaaltwee = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[3]/td[3]/span/span[3]")
    print("Tweede les:  "+ uurtweetekst+ " - " + lokaaltwee.text+ " - " + lestweetekst)
    lestweeg()
    lesdrie()



def leseeng():
    global maand
    dagverkrijgen()
    tijdstip = uureentekst
    #default begin: '2019-02-26T06:00:00+01:00'
    #default eind:  '2019-02-26T07:00:00+01:00'
    if(tijdstip == "1"):
        btijd = btijd1
        etijd = etijd1
    elif(tijdstip == "2"):
        btijd = btijd2
        etijd = etijd2
    elif(tijdstip == "3"):
        btijd = btijd3
        etijd = etijd3
    elif(tijdstip == "4"):
        btijd = btijd4
        etijd = etijd4
    elif(tijdstip == "5"):
        btijd = btijd5
        etijd = etijd5
    elif(tijdstip == "6"):
        btijd = btijd6
        etijd = etijd6
    elif(tijdstip == "7"):
        btijd = btijd7
        etijd = etijd7
    elif(tijdstip == "8"):
        btijd = btijd8
        etijd = etijd8
    
    
    begineen = datumg+"T"+btijd+":00+01:00"
    eindeen = datumg+"T"+etijd+":00+01:00"
    #-
    #-
    service = build('calendar', 'v3', credentials=creds)
    #Calendar API
    event = {
      'summary': uureentekst+ " - " + lokaaleen.text+ " - " + leseentekst,
      'location': lokaaleen.text,
      'description': '',
      'start': {
        'dateTime': begineen,
        'timeZone': 'Europe/Amsterdam',
      },
      'end': {
        'dateTime': eindeen,
        'timeZone': 'Europe/Amsterdam',
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Les in google gezet: '+ uureentekst+ " - " + lokaaleen.text+ " - " + leseentekst)

def leseen():
    global uureentekst
    global leseentekst
    global lokaaleen
    #eerste les
    leseen = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[2]/td[3]/span/span[2]")
    leseentekst = leseen.text
    uureen = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[2]/td[3]/span/span[1]")
    uureentekst = uureen.text
    lokaaleen = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[2]/td[3]/span/span[3]")
    print("Eerste les:  "+ uureentekst+ " - " + lokaaleen.text+ " - " + leseentekst)
    leseeng()
    lestwee()


def datum():
    global datumtekst
    #De datum verkrijgen
    datum = driver.find_element_by_xpath("//*[@id=\"afsprakenLijst\"]/div[2]/table/tbody/tr[1]/td/p/span/strong")
    datumtekst = datum.text
    print("          "+datumtekst)
    leseen()


def verzamelen():
    #tijd om rooster te laden
    #default tijd = 4
    time.sleep(9)
    print("Datum en lessen inladen...")
    datum()
    
def inloggen():
    id_box = driver.find_element_by_id("username")
    id_box.send_keys(inlogid)
    #vult gebruikersnaam in
    print("Clicking next")
    time.sleep(.3)
    enterknop = driver.find_element_by_id("username_submit")
    enterknop.click()
    #klikt op doorgaan knop
    print("Inserting password")
    time.sleep(.3)
    ww_box = driver.find_element_by_id("password")
    ww_box.send_keys(wachtwoordid)
    #vult wachtwoord in
    time.sleep(.3)
    print("Clicking next")
    enterknop2 = driver.find_element_by_id("password_submit")
    enterknop2.click()
    print("Loading schedule")
    #druk op doorgaan
    verzamelen()

def openmagister():
    global driver
    driver = webdriver.Chrome()
    driver.get(website)
    #open chrome in magister
    print("GitHub: ")
    print("Subscribe to Jelyko TCG")
    print("Python file coded by Jelyko TCG")
    print("Loading magister")
    time.sleep(2)
    #website tijd geven om te laden, anders is de code te snel en komer er errors
    print("inserting name")
    inloggen()
    


def gstarten():
    global creds
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    


gstarten()
openmagister()
