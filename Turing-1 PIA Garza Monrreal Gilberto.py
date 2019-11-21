class tupla_transicion:

    def __init__(self, _estado, _caracter , _direccion):

        self.estado = _estado

        self.caracter = _caracter

        self.direccion = _direccion



class turing_machine:

    def __init__(self, transicion, string_cinta):

        if isinstance(transicion, dict):

            self.tabla_transicion = transicion

        self.cinta = list(string_cinta)

        self.current_state = 's'

        self.current_position = 0

    def strart(self):

        result = False

        if self.current_state == 's':

            while (self.current_state!= 'Alto' and self.current_state!= 'Si' and self.current_state!= 'No' and self.current_state !='Error'):

                car = self.cinta[self.current_position]

                tupla = "('" + self.current_state + "', '" + car + "')"

                if  tupla in self.tabla_transicion:

                    accion = self.tabla_transicion[tupla]

                    if isinstance(accion, tupla_transicion):

                        self.current_state = accion.estado

                        print(self.cinta[self.current_position], accion.caracter, accion.direccion, accion.estado)

                        self.cinta[self.current_position] = accion.caracter

                        if accion.direccion == 'l':

                            self.current_position = self.current_position - 1

                        else:

                            if accion.direccion == 'r':

                                self.current_position = self.current_position + 1

                            else:

                                if accion.direccion != 'o':

                                    #salida si hay error

                                    self.current_state = 'Error'



        if self.current_state!= 'Alto' or self.current_state!= 'Si' or  self.current_state!= 'No':

            result = True

        return result


# a^3^n
#Acepta cadenas de 3^n letras a

MT = dict()

MT["('s', 'a')"] = tupla_transicion('t', 'a', 'r')

MT["('t', 'a')"] = tupla_transicion('u', 'a', 'r')

MT["('u', 'a')"] = tupla_transicion('s', 'a', 'r')

MT["('s', '@')"] = tupla_transicion('Si', '@', 'o')



stri = 'aaaaaaaaa@'

tm = turing_machine(MT,stri)

result = tm.strart()

print(result)

print(tm.current_state, tm.current_position)




 



 

 

 

 