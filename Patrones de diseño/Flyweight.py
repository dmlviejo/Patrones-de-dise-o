class nivel:
   pass

class Piso(nivel):
   def __init__(self):
      pass
   
   def codigo(self, code_code):
      return "Nombre[%s]" % (code_code)
   
class Material(nivel):
   textu = {}
   
   def __new__(cls, name, textu_id):
      try:
         id = cls.textu[textu_id]
      except KeyError:
         id = nivel.__new__(cls)
         cls.textu[textu_id] = id
      return id
   
   def set_textura_info(self, codetic_info):
      cg = Piso()
      self.codetic_info = cg.codigo(codetic_info)
   
   def get_textura_info(self):
      return (self.codetic_info)

def test():
   data = (('a', 1, 'Tierra'), ('a', 2, 'Tierra'), ('b', 1, 'Tierra'))
   textu_nivels = []
   for i in data:
      obj = Material(i[0], i[1])
      obj.set_textura_info(i[2])
      textu_nivels.append(obj)
   
   for i in textu_nivels:
      print ("id = " + str(id(i)))
      print (i.get_textura_info())
   print ("El suelo es de la misma textura")

if __name__ == '__main__':
   test()
