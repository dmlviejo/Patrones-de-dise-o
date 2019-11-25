class persona():
   pass

class Despertar(persona):
   
   @staticmethod
   def despierto():
      return True

   
class Juanito(persona):
   
   def __init__(self):
      self.despertar = Despertar()
      self.trabajar= iraTrabajo()

class iraTrabajo(persona):

   def ire(self):
      self.ir = True
   
   def noire(self):
      self.ir = True

def main():
   juanito = Juanito()
   juanito.iraTrabajo(True)

