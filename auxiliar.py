'''
    Funiones auxiliares

'''
def distance(lat1, long1, lat2, long2):
    '''
        Permet calcular la distacia entre el ultim node fins el node objectiu

        Autor: Erick Cruz Cedeño 

        Registre de canvis:
        11/04/2020 - Creació    - Erick Cruz Cedeño
        12/04/2020 - Modificacó - Erick Cruz Cedeño
        Parametres:
            latitud1 i longitu1 que seran las del ultim aeroport de la llista y latitud2 i longitut 2 que seran las del aeroport de Desti

        retorna:
            La distacia de entre aquest 2 punts, arrodonits a 2 decimals
    '''

    from math import radians, acos, sin, cos

    r= 6378 #radio tierra
    #convertir grados decimales a radianes
    lat1, long1, lat2, long2 = radians(lat1), radians(long1), radians(lat2), radians(long2)

    #hiversine
    dist = acos (sin(lat1) * sin (lat2) + cos(lat1) * cos(lat2) * cos(long2-long1)) * r

    return round(dist,2)

def time(distancia, averageSpeed = 600):
    '''
        Ens permetra fer un calcul Estimat de temps entre un Aeroport al Aeroport de Desti, partint de la formula de VELOCITAT = DISTACIA /TEMP
            Autor: Erick Cruz Cedeño

        Registre de canvis:
        12/04/2020 - Creació - Erick Cruz Cedeño
        Parametres:
            disctancia es un float.
            AverageSpeed es la velocidad mitjana que es permetra calcular un cost estiimat de temps per el punt de X---Desti
        Retorna:
            una cadena de caracter en format hh:mm que despres aquesta cridara a la funcio hh_to_ss que permetra pasar el temps en deciamal a segons

    '''
    #t=d/v
    temps = str(distancia/averageSpeed)  #resultado en horas
    h, ms = temps.split(".")
    if len(h) < 2:
        h = '0'+ h
    ms = '0.'+ ms
    ms = round(float(ms)*60)
    ms = int(ms)
    hhmm = h +':'+ str(ms)
    return hh_to_ss(hhmm)

def hh_to_ss(value):
    '''
        Permet fer un conversio de hores y minuts a segons total
        Autor: Erick Cruz Cedeño

    Registre de canvis:
    12/04/2020 - Creació - Erick Cruz Cedeño


    Parametres:
        solicita un volor que es de type string
    ------
        retorna una enter, que son el segons totals
    '''

    hh, mm = value.split(":")
    hh =int(hh)
    mm = int(mm)
    h_s = (hh*60)*60
    m_s = mm*60
    totalseg = h_s + m_s
    return totalseg

def ss_to_hhmm(value):
    '''
        Permet converti el segons que es un valor enter a un string en format hh:mm
         Autor: Erick Cruz Cedeño

    Registre de canvis:
    12/04/2020 - Creació - Erick Cruz Cedeño

    Parametres:
        value es un enter
    Retorna:
        retorna un string en format hh:mm
    '''
    #segons = int(value %60)
    minuts = int((value /60)%60)
    horas = int((value/60)/60)

    if len(str(minuts)) < 2:
        minuts = "0" + str(minuts)

    if len(str(horas)) < 2:
        horas = "0" + str(horas)

    return str(horas) + ":" + str(minuts)
