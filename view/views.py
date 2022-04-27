from controllers import controller
from models.LinkedList import LinkedList

def main ():  

    lista_ligada = LinkedList()

    while True:

        comandos = input().split(" ")

        if comandos[0] == "RPI":
            RPI(comandos[1], lista_ligada)

        elif comandos[0] == "RPF":
            RPF(comandos[1], lista_ligada)

        elif comandos[0] == "RPDE":
            RPDE(comandos[1],comandos[2],lista_ligada)

        elif comandos[0] == "RPAE":
            RPAE(comandos[1],comandos[2],lista_ligada)

        elif comandos[0] == "RPII":
            RPII(comandos[1], int(comandos[2]), lista_ligada)

        elif comandos[0] == "VNE":
            VNE(lista_ligada)

        elif comandos[0] == "VP":
            VP(comandos[1],lista_ligada)

        elif comandos[0] == "EPE":
            EPE(lista_ligada)

        elif comandos[0] == "EUE":
            EUE(lista_ligada)

        elif comandos[0] == "EP":
            EP(comandos[1],lista_ligada)

        else:
            print("Por favor verifique se todas as informações foram introduzidas.")

def RPI(elemento, lista_ligada):

    lista_ligada = controller.registar_at_star(lista_ligada,elemento)
    lista_ligada.traverse_list()

def RPF(elemento, lista_ligada):

    lista_ligada = controller.registar_at_end(lista_ligada,elemento)
    lista_ligada.traverse_list()

def RPDE(elemento_novo,elemento_registado,lista_ligada):

    lista_ligada = controller.registar_after_item(lista_ligada,elemento_novo,elemento_registado)
    lista_ligada.traverse_list()

def RPAE(elemento_novo,elemento_registado,lista_ligada):

    lista_ligada = controller.registar_before_item(lista_ligada,elemento_novo,elemento_registado)
    lista_ligada.traverse_list()

def RPII(elemento,indice,lista_ligada):

    lista_ligada = controller.registar_no_indice(lista_ligada,elemento,indice)
    lista_ligada.traverse_list()

def VNE(lista):

    numero = controller.numero_paises(lista)
    print("O número de elementos são",numero)

def VP(elemento,lista_ligada):

    if controller.verificar(lista_ligada,elemento) == True:
        print("O país",elemento,"encontra-se na lista.")
    else:
        print("O país",elemento,"não se encontra na lista.")

def EPE(lista_ligada):

    primeiro = lista_ligada.start_node.item
    print("O país",primeiro,"foi eliminida da lista.")
    controller.eliminar_primeiro(lista_ligada)

def EUE(lista_ligada):

    ultimo  = lista_ligada.get_last_node()
    print("O país",ultimo,"foi eliminado da lista.")
    controller.eliminar_ultimo(lista_ligada)

def EP(elemento, lista_ligada):

    if controller.verificar(lista_ligada, elemento) == True:
        print("O país",elemento,"foi eliminado da lista.")
        lista_ligada = controller.elimninar_elemento(elemento, lista_ligada)
    else:
        print("O país",elemento,"não se encontrar na lista.")