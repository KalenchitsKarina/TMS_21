import ui_func

try:
    ui_func.result = ui_func.a / ui_func.b
except ZeroDivisionError:
    ui_func.b = 0
    ui_func.result = 0
    print ('error! division by zero')