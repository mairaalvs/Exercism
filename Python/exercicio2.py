EXPECTED_BAKE_TIME = 40 #tempo de cozimento esperado

def bake_time_remaining(elapsed_bake_time): #tempo restante de cozimento
    """
    Return bake_time_remaining.
    """ 
    return EXPECTED_BAKE_TIME - elapsed_bake_time #retorna o tempo total de cozimento - tempo que ficou no forno

def preparation_time_in_minutes(number_of_layers): #tempo de preparação em minutos
    """
    Return preparation time in minutes.
    """ 
    return number_of_layers * 2 #numero de camadas da lasanha * 2 min por camada

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time): #tempo decorrido em minutos
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """   
    return (number_of_layers*2) + elapsed_bake_time
