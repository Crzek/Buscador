"""
        Autor: Sheyla Caya Gilarde

        Registre de canvis:
        30/03/2020 - Creació    - Sheyla Caya Gilarde
        12/04/2020 - implementació metodes - Sheyla Caya Gilarde
"""
""" La funció de la classe aeroport és guardar la informació de cada aeroport de la xarxa de vols del projecte.
       ···
       Atributs
       ------------
       IATA: str
           codi IATA de l'aeroport de la xarxa
       Nom: str
           nom de l'aeroport de la xarxa
       latitud: int
           coordenada angular de latitud
       longitud: int
           coordenada angular de longitud
       Connexions: str
           conjunt de connexions que té l'aeroport junt amb els costos associats

       Mètodes
       ------------
       get_nom ()
           accedeix a l'atribut nom i retorna el valor corresponent
       get_IATA ()
           accedeix a l'atribut codi IATA i retorna el valor corresponent
       get_latitud ()
           accedeix al valor de latitud i retorna el valor corresponent
       get_longitud ()
           accedeix al valor de longitud i retorna el valor corresponent
       get_conections ()
           accedeix al valor de connexions i retorna el valor corresponent
        set_xxx():
            ens permeteix cambiar el valor de latribut
       """


class Aeroport:

    def __init__(self, Iata, Nom, latitud, longitud, conecciones):

        self.IATA = Iata    #str
        self.Nom = Nom       #str
        self.latitud = latitud  #float
        self.longitud = longitud    #float
        self.Conecciones = conecciones  #diccionario

    def __str__(self):
        return str(self.get_IATA())+' - '+str(self.get_nom())  #'  Latitud:'+str(self.get_latitud())+' Longitud:'+str(self.get_longitud())

    def print_conections(self, dicAeroports):

        print('-----------')
        print('Conecciones directas con el Aeropuerto '+self.Nom+ ' ('+self.IATA+')')

        for key in self.Conecciones:
            nom = dicAeroports[key]
            print(nom)
        print('---------')


    def get_nom(self):
        return self.Nom

    def get_IATA(self):
        return self.IATA

    def get_latitud(self):
        return self.latitud

    def get_longitud(self):
        return self.longitud

    def get_conections(self):
        return self.Conecciones

    def set_nom(self, nom):
        self.Nom = nom

    def set_iata(self, iata):
        self.IATA = iata

    def set_latitud(self, latitud):
        self.latitud = latitud

    def set_longitud(self, longitud):
        self.longitud = longitud

    def set_conection(self, conections):
        self.Conecciones = conections

