# This is decorator function demo which only make entry for plugins 

PLUGIN = dict() 

def plugin_recorder(func) : 
    """ This is function for plugin register """ 
    PLUGIN[func.__name__] = func 
    return func 

@plugin_recorder
def add(num1,num2) : 
    return num1+num2

@plugin_recorder
def sub (num1,num2) : 
    return num1-num2

@plugin_recorder
def mul(num1,num2) : 
    return num1*num2

@plugin_recorder
def div(num1,num2) : 
    return num1//num2


# you do not even need to call plugin , It will get added automatically
for key in PLUGIN : 
    print(key , " : " , PLUGIN[key] )