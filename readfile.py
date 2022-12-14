from aeroport import Aeroport

def cargar_dadas(fileTXT):
    """
        Mostrar per pantalla la informació llegida línia a línia des del fitxer. En el cas en què es produeixi un error en
        la lectura del fitxer s'utilitza try-except. Si no es pot llegir de manera correcta el fitxer, la funció mostra un
        error indicant el motiu.

        Autor: Erick Cruz Cedeño

        Registre de canvis:
        29/03/2020 - Creació        - Erick Cruz Cedeño
        2/04/2020  - modificació    - Erick Cruz Cedeño        ···
        Paràmetres
        ------------
        fitxer: File_Type str
              fitxer que conté les dades de la xarxa de vols

        Retorna:
               Un objecte de la classe Aeroport que conté les dades del fitxer.
               Si no es poden llegir les dades retornarà un objecte buit.
        """

    try:
        file = open(fileTXT, 'r')
        dic_aeroport = {}
        for text in file:  #text es la primera linea del archivo,--> BCN,barcelona,latitud,longitu, FRD 12:34 MAD 00:45\n
            dic_conection = {}
            values = text.split(',')    #values = [BCN, Barcelona , latitud , longitud ,'FRD 12:34 MAD 00:45\n' ]
            l_conection = values[-1].split()    #l_conection=['FRD', '12:34', 'MAD', '00:45']
            for key in range(0 ,len(l_conection) ,2):   #star 0, stop len(l_conection), step--> cada 2
                dic_conection[l_conection[key] ] =l_conection[key +1]   #insertamos elementos con su clave- valor en el diccionari de conecciones
            aero = Aeroport(values[0], values[1], values[2], values[3], dic_conection)  #creamos objeto aeropueto
            dic_aeroport[aero.get_IATA() ] = aero   #calve=IATA, valor=OBJETO AEROPUERTO

        file.close()
        return dic_aeroport

    except FileNotFoundError:
        print('Fichero inexistente')


def printadic(dic):
    '''parametro : diccionario de los aeropuetos
        imprime cada valor del diccionario

        Autor: Erick Cruz Cedeño

        Registre de canvis:
        2/04/2020  - creació    - Erick Cruz Cedeño

        '''
    print('---------------')
    print('Red de Aeropuertos:')
    for item in dic:
        print(dic[item])    #ES UNA CLASS AERO
    print('---------')
