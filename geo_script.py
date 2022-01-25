import pickle
from visor.models import Colegio

def create_dict():
    colegios = Colegio.objects.all()
    diccio = {}
    for col in colegios:
        dept = col.departamento
        mun = col.municipio
        if not diccio.get(dept):
            diccio[dept] = [mun]
        else:
            if mun not in diccio[dept]:
                diccio[dept].append(mun)
    return diccio

#print(create_dict())

def pickle_dict():
    dicc = create_dict()

    with open('departamentos.pickle', 'wb') as handle:
        pickle.dump(dicc, handle, protocol=pickle.HIGHEST_PROTOCOL)

def check_pickle():
    with open('departamentos.pickle', 'rb') as handle:
        b = pickle.load(handle)
        print(b)

#pickle_dict()
#check_pickle()
