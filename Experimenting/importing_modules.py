import importlib.util
import importlib

#DIDN'T WORK-----------
# calculator_gui_importable=  importlib.import_module(r"C:\Users\viraj\Programming when I shouldn't be Programming\Tkinter_calculator")

#WORKS(Method-1)--------------------
spec = importlib.util.spec_from_file_location(r"calculator_gui_importable", r"C:\Users\viraj\Programming when I shouldn't be Programming\Tkinter_calculator\calculator_gui_importable.py")   
 
# importing the module as foo
foo = importlib.util.module_from_spec(spec)       
spec.loader.exec_module(foo)
 
# calling the hello function of mod.py
foo.GUI()


#WORKS(Method-2)--------------------
import sys
 
sys.path.insert(0,r"C:\Users\viraj\Programming when I shouldn't be Programming\Tkinter_calculator")
from calculator_gui_importable import *
GUI()