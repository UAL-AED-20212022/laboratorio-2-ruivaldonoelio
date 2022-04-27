from models.LinkedList import LinkedList

def registar_at_star(lista,elemento):
    lista.insert_at_start(elemento)
    return lista

def registar_at_end(lista,elemento):
    lista.insert_at_end(elemento)
    return lista

def registar_before_item(lista,elemento_novo,elemento_registado):
    lista.insert_before_item(elemento_registado,elemento_novo)
    return lista

def registar_after_item(lista,elemento_novo,elemento_registado):
    lista.insert_after_item(elemento_registado,elemento_novo)
    return lista

def registar_no_indice(lista,elemento,indice):
    lista.insert_at_index(indice,elemento)
    return lista

def numero_paises(lista):
    numero = lista.get_count()
    return numero

def verificar(lista,elemento):

    verify = lista.search_item(elemento)
    return verify

def eliminar_primeiro(lista):
    eliminar = lista.delete_at_start()
    return eliminar

def eliminar_ultimo(lista):
    eliminar = lista.delete_at_end()
    return eliminar

def elimninar_elemento(elemento,lista):
    lista.delete_element_by_value(elemento)
    return lista