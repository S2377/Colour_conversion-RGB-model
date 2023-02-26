""" 
Functions for Assignment A3

This file contains the functions for the assignment. You should replace the stubs
with your own implementations.

AUTHOR : SHIVAM KUMAR
DATE   : 23 FEB 2023
"""
import introcs
import math


def complement_rgb(rgb):
    """
    Returns the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    # THIS IS WRONG.  FIX IT
    return introcs.RGB(255-rgb.red,255-rgb.green,255-rgb.blue)


def str5(value):
    """
    Returns value as a string, but expanded or rounded to be exactly 5 characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
    
    Parameter value: the number to convert to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    # Remember that the rounding takes place at a different place depending 
    # on how big value is. Look at the examples in the specification.

    s = str(value)
    print(s)
    find_dec = s.find('.')
    before_dec = s[:find_dec]
    after_dec = s[find_dec+1:]

    if type(value) == float:

        if len(before_dec) == 3 :
            return str(round(value,1))

        elif len(before_dec) == 2 and len(after_dec) == 2:            
            return s

        elif len(before_dec) == 2 :
            #return str(round(value,2)) if int(after_dec[0]) != 9 and int(after_dec[-1]) >= 5 else str(round(value,2)) + '0'
            return str(round(value,2)) if len(str(round(value,2))) ==5 else str(round(value,2)) +'0' 

        elif len(before_dec) == 1:
            if len(str(round(value,3))) == 5:
                return str(round(value,3))
            elif len(str(round(value,3))) == 4:
                return str(round(value,3)) +'0'

            elif len(str(round(value,3))) == 3:
                return str(round(value,3)) +'00'

        elif '.' not in s:
            return str(round(value,1))+'00'
    else:
        if len(s) == 3:
            return s + '.' + '0'
        elif len(s) == 2 :
            return s + '.' + '00'
        else:
            return s + '.' + '000'





def str5_cmyk(cmyk):
    """
    Returns the string representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    return '('+ str5(cmyk.cyan) +', ' + str5(cmyk.magenta) +', ' + str5(cmyk.yellow) + ', ' + str5(cmyk.black) + ')'
    




def str5_hsv(hsv):
    """
    Returns the string representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Example: if str(hsv) is 
    
          '(0.0,0.313725490196,1.0)'
    
    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object.
    """

    return '('+ str5(hsv.hue) +', ' + str5(hsv.saturation) +', ' + str5(hsv.value)  + ')'
    
    


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.
    
    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to the range 0..1 by dividing them by 255.0.
    r1= rgb.red/255.0
    g1= rgb.green/255.0
    b1= rgb.blue/255.0

    k = 1-max(r1,g1,b1)

    if k == 1:
        cmyk_obj1 = introcs.CMYK(0.0,0.0,0.0,100.0)
        return cmyk_obj1   

    else:
        c = ((1-r1-k)/(1-k))*100
        m = ((1-g1-k)/(1-k))*100
        y = ((1-b1-k)/(1-k))*100
        
        cmyk_obj2 = introcs.CMYK(c,m,y,k*100)
        return cmyk_obj2

        

def cmyk_to_rgb(cmyk):
    """
    Returns an RGB object equivalent to cmyk
    
    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # The CMYK numbers are in the range 0.0..100.0. 
    # Deal with them the same way as the RGB numbers in rgb_to_cmyk()

    c = cmyk.cyan/100
    m = cmyk.magenta/100
    y = cmyk.yellow/100
    k = cmyk.black/100

    r = round(((1-c)*(1-k)*255))
    g = round(((1-m)*(1-k)*255))
    b = round(((1-y)*(1-k)*255))


    return introcs.RGB(r,g,b)



def rgb_to_hsv(rgb):
    """
    Return an HSV object equivalent to rgb
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
   
    Parameter hsv: the color to convert to a HSV object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    

    r = rgb.red/255
    g = rgb.green/255
    b = rgb.blue/255

    M = max(r,g,b)
    m = min(r,g,b)

    if M == m :
        h = 0.0

        print('line 220')

    elif M == r and g >= b:
        h = 60.0*(g - b)/(M - m)

        print('line 225')

    elif M == r and g < b:
        h = 60.0 * (g - b)/(M - m) + 360.0

        print('line 230')

    elif M == g :
        h = 60 * (b - r)/(M - m) + 120.0

        print('line 235')

    elif M == b:
        h = 60.0 * (r - g)/(M - m) + 240.0

    if M == 0 :
        s = 0.0

        print('line 243')

    else:
        s = 1 - m/M

        print(' line 248')

    v = M

    hsv_obj = introcs.HSV(h,s,v)


    return hsv_obj


def hsv_to_rgb(hsv):
    """
    Returns an RGB object equivalent to hsv
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
    
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object.
    """


    h = math.floor(hsv.hue/60)

    f = hsv.hue/60 - h
    p = hsv.value*(1 - hsv.saturation)
    q = hsv.value*(1 - f*hsv.saturation)
    t = hsv.value*(1 - (1 - f)*hsv.saturation)

    if h == 0 or h == 5 :
        r = hsv.value

        print('line 269')

    elif h == 1 :
        r = q 

        print('line 274')

    elif h == 2 or h == 3 :
        r = p 

        print('line 279')

    elif h == 4 :
        r = t

        print('line 284')


    if h == 0 :
        g = t 

        print('line 290')

    elif h == 1 or h == 2 :
        g = hsv.value 

        print('line 295')

    elif h == 3 :
        g = q

        print('line 300')

    elif h == 4 or h == 5 :
        g = p

        print('line 305')


    if h == 0 or h == 1:
        b = p

        print('line 311')

    elif h == 2 :
        b = t

        print('line 316')

    elif h == 3 or h == 4 :
        b = hsv.value

        print('line 321')

    elif h == 5 :
        b = q

        print('line 326')

    R = round(r*255)
    G = round(g*255)
    B = round(b*255)


    rgb_obj = introcs.RGB(R,G,B)
    return rgb_obj






    


def contrast_value(value,contrast):
    """
    Returns value adjusted to the "sawtooth curve" for the given contrast
    
    At contrast = 0, the curve is the normal line y = x, so value is unaffected.
    If contrast < 0, values are pulled closer together, with all values collapsing
    to 0.5 when contrast = -1.  If contrast > 0, values are pulled farther apart, 
    with all values becoming 0 or 1 when contrast = 1.
    
    Parameter value: the value to adjust
    Precondition: value is a float in 0..1
    
    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """

    if -1 <= contrast < 1:
        if value < 0.25 + 0.25 * contrast:
            y = ((1-contrast)/(1+contrast))*value
            return y

        elif value > 0.75 - 0.25*contrast:
            y = ((1-contrast)/(1+contrast))*(value -(3-contrast)/4) + (3+contrast)/4
            return y

        else:
            y =  y = ((1+contrast)/(1-contrast))*(value -(1+ contrast)/4) + (1 - contrast)/4
            return y

    elif contrast == 1 :
        if value >= 0.5 :
            return 1
        else:
            return 0




    


def contrast_rgb(rgb,contrast):
    """
    Applies the given contrast to the RGB object rgb
    
    This function is a PROCEDURE.  It modifies rgb and has no return value.  It should
    apply contrast_value to the red, blue, and green values.
    
    Parameter rgb: the color to adjust
    Precondition: rgb is an RGB object
    
    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    r = rgb.red/255
    g = rgb.green/255
    b = rgb.blue/255

    rgb.red = round(contrast_value(r,contrast)*255)
    rgb.green = round(contrast_value(g,contrast)*255)
    rgb.blue = round(contrast_value(b,contrast)*255)






    