import importlib.util

spec = importlib.util.spec_from_file_location(r"calculator_gui_importable", "../Tkinter_calculator")   
foo = importlib.util.module_from_spec(spec)       
spec.loader.exec_module(foo)
foo.GUI()

import HMMM

