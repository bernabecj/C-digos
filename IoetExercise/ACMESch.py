''' Ejercicio

La empresa ACME ofrece a sus empleados la flexibilidad de trabajar las horas que deseen. Pero debido a algunas circunstancias externas, necesitan saber qué empleados han estado en la oficina en el mismo período de tiempo.
El objetivo de este ejercicio es generar una tabla que contenga pares de empleados y la frecuencia con la que han coincidido en la oficina.
Entrada: el nombre de un empleado y el horario que trabajó, indicando el tiempo y las horas. Este debe ser un archivo .txt con al menos cinco conjuntos de datos. Puede incluir los datos de nuestros ejemplos a continuación:

Ejemplo 1:
APORTE
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
ASTRID=LU 10:00-12:00, JU 12:00-14:00, DO 20:00-21:00
ANDRÉS=MO10:00-12:00,J12:00-14:00,DO20:00-21:00

PRODUCCIÓN:
ASTRID-RENÉ: 2
ASTRID-ANDRES: 3
RENÉ-ANDRÉS: 2

Ejemplo 2:
APORTE:
RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00
ASTRID=LU 10:00-12:00, JU 12:00-14:00, DO 20:00-21:00

PRODUCCIÓN:
RENÉ-ASTRID: 3 


'''
import pytest

class Schedule:
    def __init__(self):
        self.new_list=[]
        with open('input.txt') as f:
            lines = f.readlines()

        for line in lines:
            if line[-1] == '\n':
                self.new_list.append(line[:-1])
            else:
                self.new_list.append(line)

        self.arr_of_schedule = [None] * len(self.new_list)

        for a, b in enumerate(self.new_list):
            b = b.replace(",", "\n")
            x=b.splitlines()
            i=0
            temp = []
            while i < len(x):
                temp.append(x[i].split("="))
                i += 1
            self.arr_of_schedule[a] = temp
        

    def get_dict_list(self):
        dict_list = []

        for i, li in enumerate(self.arr_of_schedule):
            res = {}
            for a, b in enumerate(li):
                res[b[0]] = Schedule.get_timeslots(list(str(li[a][1]).split("-")))

            dict_list.append(res)
        
        return dict_list


    def get_timeslots(arr):
            i = int(arr[0])
            j = int(arr[1])
            timeslots = set()
            for x in range (i, j):
                timeslots.add((x, x + 1))
            
            return timeslots


    def get_coincidence(self, person1, person2):
        recurrent = []
        count = 0

        for key, value in person1.items():
            try:
                if(person1[key].intersection(person2[key])):
                    recurrent.append((f"Las coincidencias se dan el día: \033[1;32;40m{key}\033[0m, en las horas: \033[1;32;40m{person1[key].intersection(person2[key])}\033[0m."))
                    count += 1
            except:
                pass

        return recurrent, count


def testing():
    schedule = Schedule()
    person = schedule.get_dict_list()

    caso1 = schedule.get_coincidence(person[0], person[1])[1]
    caso2 = schedule.get_coincidence(person[1], person[2])[1]
    caso3 = schedule.get_coincidence(person[0], person[2])[1]

    #Ejemplo de salida, en donde se muestran los días, las horas y cuantas veces coinciden dos personas
    resul = schedule.get_coincidence(person[1], person[2])
    for i in resul[0]:
        print(i)
    print(f"Teniendo un total de: \033[1;32;40m{resul[1]}\033[0m coincidencias.")

    #Pruebas unitarias especificadas en el ejercicio
    assert caso1 == 2, "Failed"
    assert caso2 == 3, "Failed"
    assert caso3 == 2, "Failed"


if __name__ == '__main__':
    testing()