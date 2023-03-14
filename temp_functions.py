def fahr_to_celsius(temp_fahrenheit):
    """This function converts temperature in degrees Fahrenheit into degrees Celsius
    
    USAGE:
    Input (<float>) the degree F as temp_fahrenheit
    
    Returns degree C as converted_temp (<float>).
    """
    #calculates converted_temp using temp_fahrenheit
    converted_temp = (temp_fahrenheit - 32) / 1.8
    
    #return converted_temp
    return converted_temp


def temp_classifier(temp_celsius):
    """ Classifies temperature(C) as cold, slippery, comfortable and warm using class values.
    
    USAGE
    Input is the float value of celsius temperature as temp_celsius.
    Returns 0 if temperature < -2.0 (cold)
    Returns 1 if -2.0 <= temperature < +2.0 (slippery)
    Returns 2 if +2.0 <= temperature < 15.0 (comfortable)
    Returns 3 if temperature >= 15.0 (warm)
    """  
    
    # cold
    if temp_celsius < -2.0:
        return 0
    
    # slippery
    elif temp_celsius >= -2.0 and temp_celsius <2.0:
        return 1
   
    # comfortable
    elif temp_celsius >=2.0 and temp_celsius < 15:
        return 2
    
    # warm 
    else:
        return 3