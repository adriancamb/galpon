subcategorias = [(1, 'Arr', 'pro', 'img', 'Arr', 0, '', 1),
                 (2, 'Beb', 'pro', 'img', 'Est', 0, '', 1),
                 (3, 'Fun', 'pro', 'img', 'Est', 0, 2, 1),
                 (4, 'Fun', 'pro', 'img', 'Est', 0, 2, 1),
                 (5, 'Acc', 'pro', 'img', 'Est.', 0, '', 2)]

def generar_diccionario_subcategorias(subcategorias):
    diccionario_subcategorias = {}
    for subcategoria in subcategorias:
        id_subcategoria, nombre, _, _, _, id_padre, _, _ = subcategoria
        if id_padre == '':
            diccionario_subcategorias[id_subcategoria] = {'nombre': nombre, 'subcategorias': {}}
        else:
            if id_padre not in diccionario_subcategorias:
                diccionario_subcategorias[id_padre] = {'nombre': '', 'subcategorias': {}}
            if id_subcategoria not in diccionario_subcategorias:
                diccionario_subcategorias[id_subcategoria] = {'nombre': nombre, 'subcategorias': {}}
            diccionario_subcategorias[id_padre]['subcategorias'][id_subcategoria] = diccionario_subcategorias[id_subcategoria]
            del diccionario_subcategorias[id_subcategoria]
    
    return diccionario_subcategorias
    

diccionario = generar_diccionario_subcategorias(subcategorias)
print(diccionario)
{0: {'nombre': '', 'subcategorias': {1: {'nombre': 'Arr', 'subcategorias': {}}, 2: {'nombre': 'Beb', 'subcategorias': {}}, 3: {'nombre': 'Fun', 'subcategorias': {}}, 4: {'nombre': 
'Fun', 'subcategorias': {}}, 5: {'nombre': 'Acc', 'subcategorias': {}}}}}