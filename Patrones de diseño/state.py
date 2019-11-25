class usuario:
    pass

class Gon_Freecss(usuario):

   name = "state"
   allowed = []

   def switch(self, state):
      """ Switch to new state """
      if state.name in self.allowed:
         print ('Estado:',self,' => cambiando a',state.name)
         self.__class__ = state
      else:
         print ('Estado:',self,' => cambiando a',state.name,'no es posible.')

   def __str__(self):
      return self.name

class Ren(Gon_Freecss):
   name = "ren"
   allowed = ['Hatsu','Zetsu','ren']

class Hatsu(Gon_Freecss):
   name = "hatsu"
   allowed = ['ren','Zetsu','Ten']

class Zetsu(Gon_Freecss):
 
   name = "Zetsu"
   allowed = ['hatsu','ten','ren']

class Ten(Gon_Freecss):

   name = "Ten"
   allowed = ['hatsu','ren','zetsu']

class Nen(usuario):
   """ A class representing a Nen """
   
   def __init__(self, model='HP'):
      self.model = model

      self.state = Hatsu()
   
   def change(self, state):
      """ Change state """
      self.state.switch(state)

if __name__ == "__main__":
   Gon = Nen()
   Gon.change(Zetsu)
   Gon.change(Hatsu)
   Gon.change(Ten)
   Gon.change(Ren)
   
