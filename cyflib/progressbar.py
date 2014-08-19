import sys, time
#barra = "[>..........]"
class progressbar():
    def __init__(self, **kwargs):
        self.char = "/"
        self.char_empty = " "
        self.width = 20
	self.percentage = True
        if "char_full" in kwargs:
            self.char = kwargs["char_full"]
        if "char_empty" in kwargs:
            self.char_empty = kwargs["char_empty"]
        if "width" in kwargs:
            self.width = kwargs["width"]
	if "percentage" in kwargs:
	    self.percentage = kwargs["percentage"]
        self.progress = 0
        self.barra = self.build_start_bar()
        self.bloques = 100/self.width
        self.bloques_rellenos = 0
    def increment(self, incremento):
        self.progress = self.progress + incremento
    def print_progress_bar(self, message):
        if(message==None):
          print self.build_barra(), "\r",
          sys.stdout.flush()
        else:
          print self.build_barra() + " " + message, "\r",
          sys.stdout.flush()
    def return_barra(self):
        return self.build_barra()
    def build_barra(self):
        #Se quitan los [ y ]
        actual_barra = self.barra[1:]
        actual_barra = actual_barra[:-1]
        #Se calcula los bloques a cambiar por el caracter x usando progreso/bloques(2)
        #progreso = xporciento
        #bloques = subir un punto cada X bloques. Ej: Si hay 2 bloque,s subir
        #un punto cada 2porciento
        self.bloques_a_rellenar = self.progress/self.bloques
        #Se copia la barra sin corchetes a otra variable para editar la variable
        bar_antigua = actual_barra
        #Se eliminan los caracteres a sustituir
        actual_barra = actual_barra[self.bloques_a_rellenar:]
        #Se calcula: len(barra_sin_corchetes)-len(barra_sin_caracteres_a_sutituir)
        #Est daria los caracteres que se deben sustituir
        total = len(bar_antigua) - len(actual_barra)
        #total = Caracteres que seran sustiduidos.
        #Aqui se ponen los caracteres*numero_de_caracteres, mas la variable
        #actual_barra que es la barra sin los caracteres a sustituir
        self.barra_final = "%s%s" % (self.char*total, actual_barra)
        #Se anaden los corchetes (primer_char, ultimo_char) y se imprime
	if(self.percentage):
            self.barra_final = "[%s] %s" % (self.barra_final, str(self.progress) + "%")
	else:
	    self.barra_final = "[%s]" % (self.barra_final)
        return self.barra_final
    def build_start_bar(self):
        barra = "["+self.char_empty*self.width+"]"
        return barra
    def reset(self):
        self.progress = 0
    def get_progress(self):
        return self.progress
#print "[===>......]", "\r",
sys.stdout.flush()
