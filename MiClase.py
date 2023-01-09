class MiClase:

    variable_clase = 'Valor variable clase2'

    def __init__(self, variable_instancia):
        self.variables_instancia = variable_instancia

        #2 metodos estaticos
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

        #metodos clases

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variables_instancia)

MiClase.metodo_clase()
#context estatico y dinamico
miObjecto1 = MiClase('variable_instancia')
miObjecto1.metodo_clase()
miObjecto1.metodo_estatico()