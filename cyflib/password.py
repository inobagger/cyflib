#Solo funciona en Windows
import sys
try:
    import msvcrt as visualc
except:
    raise ImportError("Unable to load Microsoft Visual C++ Runtime Library.")

def getpassword(prompt = ""):
   password = ""
   put = sys.stdout.write
   for i in prompt:
       visualc.putch(i)
   while True:
       char = visualc.getch()
       if char == '\n' or char == '\r': #Salto de linea
           break
       if char == '\b': #Retroceso
           put("\x08 \x08")
           password = password[:-1]
       else:
           put('*')
           password = password + char
   visualc.putch('\r')
   visualc.putch('\n')
   return password
#print getpassword()
#raw_input()