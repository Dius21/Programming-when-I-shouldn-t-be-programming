import importlib.util
import HMMM

HMMM

spec = importlib.util.spec_from_file_location("calculator_gui_importable", "C:/Users/viraj/Programming when I shouldn't be Programming/Tkinter_calculator/calculator_gui_importable.py") 
foo = importlib.util.module_from_spec(spec)       
spec.loader.exec_module(foo)
foo.GUI()



