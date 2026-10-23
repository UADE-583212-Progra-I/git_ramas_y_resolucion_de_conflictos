import re

def validar_id_usuario(id_usuario:str):
    """
    Valida que id_usuarios sea convertible a int
    Retorna True:False
    """
    patron_id = r"[1-9][0-9]*"
    return bool(re.fullmatch(patron_id, id_usuario))


def validar_nombre(nombre:str):
    """
    Valida que nombre sea no nulo y que solo caracteres"""
    patron_nombre = r"[a-ZA-Z]+"
    return bool(re.fullmatch(patron_nombre, nombre.strip())

def validar_email(email:str):
    """
    Valida que email sea un correo válido
    Retorna True:False
    """
    patron_email = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"
    return isinstance(email, str) and re.fullmatch(patron_email, email) is not None