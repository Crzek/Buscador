from auxiliar import distance, time, hh_to_ss, ss_to_hhmm
from readfile import *
'''
generador tabla heuristica
'''
def printe(heu, iata):
    print(iata, ' ', heu,' seg')

dicAero = cargar_dadas("Dades.txt")
desti= str(input("Intraduce Destino: ")).upper()

if dicAero.get(desti) is not None:
    lt2 = dicAero[desti].get_latitud()
    lg2 = dicAero[desti].get_longitud()


    for iata in dicAero:
        lt1 = dicAero[iata].get_latitud()
        lg1 = dicAero[iata].get_longitud()

        dist = distance(float(lt1),float(lg1),float(lt2),float(lg2))
        heuri = time(dist)
        printe(heuri,iata)