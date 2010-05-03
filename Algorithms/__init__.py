import os
modules = [file[:-3]
           for file in os.listdir(os.path.dirname(__file__))
           if file[-3:] == '.py' and file != '__init__.py']

for module in modules:
    globals()[module] = getattr(__import__(module, globals(), locals(), []), module)