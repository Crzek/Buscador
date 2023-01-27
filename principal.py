
from readfile import cargar_dadas, printadic
from way import Way

def A_Star(dicAero, iataOrigen, iataDesti):
    '''
        Algorisme Cerca A*, permetra obtenir rutes obtimes que imprimeix per pantalla, de moment fataria acabar-ho

        Autor: Erick Cruz Cedeño

    Registre de canvis:
    11/04/2020 - Creació - Erick Cruz Cedeño
    12/04/2020 - Modificació - Erick Cruz Cedeño
    28/04/2020 - Modificació - Erick Cruz Cedeño
    Parametres:
        diccionari de l'Aeroport, codi aeroport d-origen , codi aeroport desti

    '''
    w_list =[]
    initial_way = Way(iataOrigen) #node iniciale
    w_list.append(initial_way) #inserta en la lista

    while w_list[0].Route[-1] != iataDesti and len(w_list) != 0:
        extract = w_list.pop(0) #extraer el 1r camino
        l_expant = extract.expandRoute(dicAero,iataDesti) #expanderlo el que has sacado con el metodo de la clase Way
        # Eliminar els cicles
        l_expant = delWays(l_expant)
        # Eliminar camins redundants (pas opcional)
        w_list = w_list + l_expant #concatenar la lista expant a la w_list
        w_list.sort()   #ordenar lista de forma ascentente segun funcio f
        print_ways(w_list)

    if len(w_list) > 0:
        #mostrar ruta optima #w_list[0].print_route()
        print_Sol(w_list)
    else:
        print('No hi ha cap ruta optima ')

def delWays(list):
    '''
        funcio que permet eliminar objetes le las llista, pero abans em de verificar si la lista esta repetida, per aixo cridem un metode de la clase WAY(checkWay)
        aquest retorna un numero 0 o 1, 0 no es repeteix y 1 es repeteix y despres es retorna la llista nova sense elements repetits
        Autor: Erick Cruz Cedeño

    Registre de canvis:
        28/04/2020 - Creació - Erick Cruz Cedeño

    Parametres:
        list es una llista de objectes camins
    '''

    for objectWay in list:
        rep = objectWay.check_ways()    # retorna un  bool
        if rep:
            list.remove(objectWay)

    return list

def print_ways(list):
    '''
            Permet imprimir el camins, que seran las iteracions que realitze per trobar el la ruta optima

            Autor: Erick Cruz Cedeño

            Registre de canvis:
        29/04/2020 - Creació de la funció- Erick Cruz Cedeño
        parametre:
        list: que es la llista de camins

    '''
    for i in list:
        print(i)
    print("---------")

def print_Sol(list, solucions = 1):
    '''
        mostra per pantalla el contingut de la llista de forma que es visualitza cada element en una línia.

        Autor: Erick Cruz Cedeño

        Registre de canvis:
        11/04/2020 - Creació de la funció- Erick Cruz Cedeño

        Parametres:
            list: un llista on es troben les solocions optimes
            solucions = 1 :es una varible que per defecte et dona una solucio, en cas del que l'usuria vulgui mes 1
    '''
    print('----------')
    if solucions != 1:      #en caso de que quiera una alternatiba de solucion
        s_list = list[0:solucions]
        for cami in s_list:
            cami.print_route()
            print('---------------')

    else:       #printa la 1r  solucio optima
        print('Llista de cami optim.')
        for i in range(solucions):
            list[0].print_route()
            print('---------------')

def mostra_menu(dicAero):
    """
        Mostrar per pantalla el menu amb les opcions disponibles.
        Es demana a l'usuari que triï una de les opcions. En cas correcte retorna la opcion seleccionada i si el nombre no es correcta fa un recursió

        Autor: Erick Cruz Cedeño

        Registre de canvis:
        30/03/2020 - Creació de la funció- Erick Cruz Cedeño
        02/04/2020 - modificació - Erick Cruz···
        Paràmetres
        ------------
        Retorna:
                Opcio escollida
                Si es tria una opció no vàlida, s'indica un missatge d'error i es dona la possibilitat de triar una nova
                fins que es triï l'opcio de sortir.
        """
    print('Menú:')
    print('1. Buscar Vuelo')
    print('2. Información')
    print('3. Salir. Selecciona una opción')


    opcio = int(input('Introduce numero:'))
    if opcio >= 1 and opcio <= 3:
        return opcio
    else:
        print('ERROR. Introduce un numero entre 1-3.')
        mostra_menu(dicAero)

def runOpcio(opcio,dicAero):
    """
        Execució de l'opció escollida

        Autor: Erick Cruz Cedeño

        Registre de canvis:
        30/04/2020 - Creació de la funció- Erick Cruz Cedeño

        ···
        Paràmetres
        ------------
        opcio: int
            número de l'opció escollida

        Retorna:
            Opcio escollida
        """

    if opcio==1:#buscar vuelo
        buscaVol(dicAero)
    elif opcio==2:#informacio
        menuinformacio(dicAero)
    elif opcio==3:#salir
        exit()

def buscaVol(dicAero):
    """
       l'usuari introduira el codis de origen y desti y fará una verificacio si son correctes, en cas que no es fa un recursió

        Autor: Erick Cruz Cedeño

        Registre de canvis:
        30/04/2020 - Creació de la funció- Erick Cruz Cedeño
        12/04/2020 - modificació - Erick Cruz Cedeño
        ···
        Paràmetres
        ------------
        Retorna:
            Informació del vol buscat

        """

    origen = input("Introdueix el codi IATA del aeroport d'origren:").upper()
    desti = input("Introdueix el codi IATA del aeroport de destinació:").upper()
    ok = check_iata(dicAero, origen, desti)
    while ok == 1 :  #1 es que hi ha algun error al origen o desti
        buscaVol(dicAero)
    A_Star(dicAero,origen,desti)

def check_iata(dicAero, origen=None, desti=None):
    '''
        Ens permetra fer una verificacio si ya el valors introduits dels codis son correctes o erronis
    Autor: Erick Cruz Cedeño

    Registre de canvis:
    12/04/2020 - Creació - Erick Cruz Cedeño
    29/04/2020 - Modificacio -Erick Cruz Cedeño
    ···
    Paràmetres
        dicAero: diccionari de Aeroport


    Retorna:
        0-1 , 0 significa que que els codis introduits per l'usuari estan correctes y 1 que hi ha algun error
    '''

    if (origen is not None) and (desti is not None):
        origen_ok = dicAero.get(origen)
        desti_ok = dicAero.get(desti)

        if (origen_ok is None) and (desti_ok is None):
            print("Origen y desti Erronis")
            return 1

        elif (origen_ok is not None) and (desti_ok is None):   #origenok= aero, destiok = NONE
            print('Desti  Erroni')
            return 1

        elif (desti_ok is not None) and (origen_ok is None):
            print('Origen Erroni')
            return 1

        elif (origen_ok is not None) and (desti_ok is not None):#correcto
            return 0


    elif (desti is None) and (origen is not None):
        origen_ok = dicAero.get(origen)

        if origen_ok is not None:
            return 0

        else:
            print('Codi incorrecte')
            return

def menuinformacio(dicAero):
    """
    Execució de l'opció 2 per buscar la informació corresponent corresponent i es torna al menu principal
    Autor: Erick Cruz Cedeño

    Registre de canvis:
    29/03/2020 - Creació de la funció- Erick Cruz Cedeño
    ···
    Paràmetres
    ------------
    Retorna:
        Informació

      """
    print("Menú informació:")
    print('1. Informació de funcionament')
    print('2. Mostra Aeroports')
    print('3. Vols directes')
    print('4. Tornar al menú principa')

    opcio = int(input('Escull una opció: '))
    if opcio == 1:
        informacio()

    elif opcio == 2:
        printadic(dicAero)

    elif opcio == 3:
        codi = str(input("Introdueix el codi de l'aeroport: ")).upper()
        ok = check_iata(dicAero,codi)  # EROOR en: 1.origen, 2.desti, 3.O y D
        if ok == 0: #solo hay origen y es correcto
            aero = dicAero.get(codi)
            aero.print_conections(dicAero)

    elif opcio == 4:
        pass #mostaramenu()

    else:
        print('ERROR. Introdueix una opcio entre 1-4.')
        menuinformacio(dicAero) #recursion

def informacio():
    """
    Execució de l'opció 2 per buscar la informació corresponent corresponent i es torna al menu principal
    Autor: Erick Cruz Cedeño

    Registre de canvis:
    30/03/2020 - Creació de la funció- Erick Cruz Cedeño
    ···
    Paràmetres
    ------------
    Retorna:
        Informació

      """

    print("La següent aplicació té com a finalitat cercar el vol més optim entre un origen i una destinació, introduit per l'usuari,\n"
        "dins d'una xarxa d'aeroports. A l'usuari se li mostrarà un menú amb diferents opcions on haurà de decidir que vol fer.\n"
        "Si l'usuari tria l'opció 1, haura de introduir el codi de l'aeroport d'origen i posteriormeent el codi  de l'aeroport de destinació\n" 
        "i amb aixó la aplicació iniciarà  una cerca per trobar la ruta més optima.  ")

def exit():
    """
        Execució de l'opció 3 per sortir de la funció del menú

        Autor: Erick Cruz Cedeño

        Registre de canvis:
        30/03/2020 - Creació de la funció- Erick Cruz Cedeño
        Paràmetres
        ------------
        Retorna:
             Retorna al menu
        """
    print("Sortin del programa")

def main():
    """
        Execució del menu principal

        Autor: Erick Cruz Cedeño

        Registre de canvis:
        01/04/2020 - Creació de la funció- Erick Cruz Cedeño i Erick Cruz Cedeño
        02/04/2020 - modificació - Erick Cruz
        ···
        Paràmetres
        ------------
        Retorna:
             Retorna al menu
        """

    aeropoerts = cargar_dadas('Dades.txt')
    opcio = mostra_menu(aeropoerts)
    while (opcio != 3) :
        runOpcio(opcio,aeropoerts)
        opcio = mostra_menu(aeropoerts)
    exit()

#ejcuta solo main
if __name__ == "__main__":
   main()