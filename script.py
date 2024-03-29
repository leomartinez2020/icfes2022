import random
import pandas as pd

from visor.models import Colegio

xfile = 'Saber-11-2021-1.xlsx'
#xfile = 'Saber-11-2021-4.xlsx'
df = pd.read_excel(xfile, skiprows=6)

def proc():
    seq = ['CODINST', 'NOMBREINSTITUCION', 'CODIGOMUNICIPIO', 'NOMBREMUNICIPIO', 'DEPARTAMENTO', 'CALENDARIO',
        'NATURALEZA', 'JORNADA', 'EVALUADO', 'PROMLECTURACRITICA', 'PROMMATEMATICA', 'PROMSOCIALESYCIUDADANAS',
        'PROMCIENCIASNATURALES', 'PROMINGLES', 'PERIODO']
    lista2 = ['codinst', 'nombre', 'codigomunicipio', 'municipio', 'departamento', 'calendario', 'naturaleza', 'jornada',
     'evaluados', 'lectura', 'matematicas', 'sociales', 'ciencias', 'ingles', 'periodo']
    diccio = {clave: valor for clave, valor in zip(seq, lista2)}

    df2 = df.filter(items=seq)
    df2 = df2.rename(columns=diccio)
    df2['periodo'] = '2021'
    return df2

def populate_db_dont_use():
    data = proc()
    counter = 0
    while True: #Colegio.objects.count() < 100:
        if counter > 5:
            break
        d = dict(data.loc[counter])
        c = Colegio(**d)
        try:
            #c.save()
            print(counter)
        except ValueError:
            print('error...')
        finally:
                counter += 1
    print('Terminado...')

def populate_db():
    data = proc()
    counter = 0
    while True:
        d = dict(data.loc[counter])
        c = Colegio(**d)
        try:
            c.save()
            if counter % 100 == 0:
                print(counter)
        except ValueError:
            print('error...')
        finally:
            counter += 1
    print('All done')
