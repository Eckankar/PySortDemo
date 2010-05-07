import os
modules = [pyfile[:-3]
           for pyfile in os.listdir(os.path.dirname(__file__))
           if pyfile[-3:] == '.py' and pyfile != '__init__.py']

for module in modules:
    globals()[module] = getattr(__import__(module, globals(), locals(), []), module)
