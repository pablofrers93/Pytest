import logging

# DEBUG =10 = debug
# INFO = 20 = info
# WARNING = 30 = warning 
# ERROR = 40 = error
# CRITICAL = 50 =critical

logging.basicConfig(level = logging.INFO,
                    format = "%(threadName)s - %(levelname)s - %(asctime)s - Message: %(message)s",
                    datefmt = "%Y/%m/%d"
                    )

def suma(numero1 : int, numero2: int) -> int:
    """Permite sumar dos numeros enteros

    Args:
        numero1 (int):
        numero2 (int):

    Returns:
        int:
    """

    logging.debug('Entramos aquì!! ')

    resultado = numero1 + numero2

    logging.debug('Nos encontramos en esta linea')

    return resultado

if __name__ == '__main__':
    logging.debug('antes del llamado a la función')

    resultado = suma (15,20)
    logging.info(resultado)   