
def initialization():
    global current_value, previous_value, storage_value, memory_value
    current_value = 0
    memory_value = 0
    previous_value = 0
    storage_value = 0

def display_current_value():
    print(current_value)

def add(to_add):
    global current_value
    global previous_value
    global storage_value
    
    previous_value = current_value
    current_value = current_value + to_add

def subtract(to_subtract):
    global current_value
    global previous_value
    global storage_value

    previous_value = current_value
    current_value = current_value - to_subtract
 

def multiply(to_multiply):
    global current_value
    global previous_value
    global storage_value

    previous_value = current_value
    current_value = current_value * to_multiply

def divide(to_divide):
    global current_value
    global previous_value
    global storage_value

    previous_value = current_value
    if to_divide == 0:
        current_value = "Error"
    else:
        current_value = current_value / to_divide  

def memorize():
    global memory_value, current_value
    
    memory_value = current_value    

def recall():
    global current_value, memory_value
    
    current_value = memory_value
    print(current_value)

def undo():
    global current_value, previous_value

    current_value, previous_value = previous_value, current_value


if __name__ == "__main__":
    
    initialization()
    
    print("Welcome to the calculator program.")
    print("Current Value: ",current_value)
    
    
    display_current_value() # 0
    add(5)
    display_current_value() # 5
    subtract(2) 
    display_current_value() # 3
    undo() 
    display_current_value() # 5
    undo() 
    display_current_value() # 3
    multiply(10)
    display_current_value() # 30
    undo() 
    undo() 
    display_current_value() # 30
    undo() 
    undo() 
    undo() 
    display_current_value() # 3
    memorize()
    add(4)
    multiply(30)
    display_current_value()
    recall()