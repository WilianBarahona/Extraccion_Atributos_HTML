from house import House
import os 

class HousesContainer:
  """Representa un contenedor de casas, específicamente de objetos de tipo House."""

  def __init__(self):
    """En el constructor se leen todos los archivos con extensión html que están en el directorio '/casas'.

    El contenido de cada archivo html se lee en una cadena que se usa para crear un objeto de tipo House. 
    """
    ##Leer archivos html
     #archivo = open("casas/10053.html","r", encoding='utf-8')  ##encoding = 'utf-8' para windows
    list_file_html=[]
    files = os.listdir('./casas')
    for file in files:
      if '.html' in file:
        list_file_html.append(file)
    
    self.list_houses = []
    for file_html in list_file_html:
      archivo = open("casas/"+file_html,"r", encoding='utf-8')
      # self.list_houses.append(House(archivo.read(),file_html))
      self.casa = House(archivo.read(), file_html)
 

  def get_homes(self):
    """Retorna un lista que contiene todo los objetos de tipo House creados en el constructor."""
    return self.casa

contenedor = HousesContainer()
c= contenedor.get_homes().get_feats()
print(c)
# dic = contenedor.casa.get_feats()
# print(dic)