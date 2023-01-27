"""
        Autor: Erick Cruz Cedeño

        Registre de canvis:
        11/04/2020 - Creació    - Erick Cruz Cedeño
        12/04/2020 - modificacó - Erick Cruz Cedeño

        Atributs:
            Route: lista
            Cost_acumulat: enter
            Funtion_f : enter

        Metodes:
            updateWay() : actualiza les dades del cami amb els nous costos

            expandRoute(): expnadeix el ruta del cami

            print_route() : Permet fer una impresió per pantalla de les rutes que te cada cami

            get_XXXX() : permet obternir el que conte el atribut XXXX

            set_XXXX() : permet reaccinar un altre valor a l'atribut XXXX

"""
from auxiliar import distance, hh_to_ss, time , ss_to_hhmm
import copy

class Way:

    def __init__(self,iata_origen):

        self.Route = [iata_origen]  #llista de codis iata que seran la ruta
        self.Cost_acumulat = 0
        self.Funtion_f = 0

    def __str__(self):
        return 'Ruta: '+ str(self.Route) + ' cost acummulat: ' +str(self.Cost_acumulat) +' funcio f: '+ str(self.Funtion_f)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, C):
        return self.Funtion_f < C.Funtion_f

    def updateWay(self, new_iata, cost, heuristica):
        '''
            Es una funcio que actulitza els atributs de la class Way
            Autor: Erick Cruz Cedeño

        Registre de canvis:
        11/04/2020 - Creació - Erick Cruz Cedeño
        12/04/2020 - Modificació - Erick Cruz Cedeño

        Parametres:
            nou codi de l'aeroport, cost que te per el node seguent, heuristica previamente calculada

        '''
        #insetar el new codigo iata en la ruta
        self.Route.append(new_iata)
        #sumar el coste al coste acumulado
        cost = hh_to_ss(cost)   #convertimos los hh:mm en segundos
        self.Cost_acumulat = self.Cost_acumulat + cost
        self.Funtion_f = self.get_costAcumulat() + heuristica

    def expandRoute(self,dicAero, iataDesti):
        '''


            Es una funcio que actulitza els atributs de la class Way
            Autor: Erick Cruz Cedeño

        Registre de canvis:
        11/04/2020 - Creació - Erick Cruz Cedeño
        12/04/2020 - Modificació - Erick Cruz Cedeño

        Parametres:
            Diccionari de l'aeroport y codi de desti de l'aeroport

        retorna una llista de camins expandits

        '''
        last = self.get_last()
        conect = dicAero[last].get_conections() #dicAero.get(key).Conecciones
        l_aux =[]
        lat_desti = dicAero[iataDesti].get_latitud()
        log_desti = dicAero[iataDesti].get_longitud()

        for key in conect:
            new = copy.deepcopy(self)
            # obtenr lat y log de la key de iata origen
            lat = dicAero[key].get_latitud()
            log = dicAero[key].get_longitud()
            dist = distance(float(lat), float(log), float(lat_desti), float(log_desti))
            heuristica = time(dist)
            new.updateWay(key, conect[key], heuristica)
            l_aux.append(new)

        return l_aux

    def check_ways(self):
        '''
            verificamos si algun elemento de la lista se repite, en caso de que se repita devolvemos un 1 y si no se repite se debuelve un 0
            ejemplo:    l= ['BCN','MAD','BCN'] esta lista se repite
                        l=  ['BCN','MAD','LIS',MAD] esta lista se repite

            Autor: Erick Cruz Cedeño i Erick Cruz Cedeño

            Registre de canvis:
                    11/04/2020 - Creació    - Erick Cruz Cedeño
                    12/04/2020 - modificacó - Erick Cruz Cedeño


        '''

        return self.Route[-1] in self.Route[:-1]


    def print_route(self, sol = None ):
        '''
            Ens permeteix mostra per pantalla las rutes que té la clase Way
            Autor: Erick Cruz Cedeño

        Registre de canvis:
        11/04/2020 - Creació - Erick Cruz Cedeño
        12/04/2020 - Modificació - Erick Cruz Cedeño


        '''

        if len(self.Route)>0:
            print('------------')
            print('Ruta OPTIMA:')
            for i in self.Route:
                if self.Route[-1] == i:
                    print(i)
                    cost = self.get_costAcumulat()
                    cost = ss_to_hhmm(cost)
                    print('Tiempo estimado total: ' + cost[:2] + "h " + cost[3:] + "m")
                else:
                    print(i, end='-->')
        else:
            print('Llista buida')
        print('----------')

    def get_costAcumulat(self):
        return self.Cost_acumulat

    def get_route(self):
        return self.Route

    def get_funtionF(self):
        return self.Funtion_f

    def get_last(self):
        return self.Route[-1]

    def set_costAcumulat(self, cost):
        self.Cost_acumulat = cost

    def set_route(self, route):
        self.Route = route

    def set_funtionF(self, funcioF):
        self.Funtion_f = funcioF