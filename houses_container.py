from house import House

class HousesContainer:
  """Representa un contenedor de casas, específicamente de objetos de tipo House."""

  def __init__(self):
    """En el constructor se leen todos los archivos con extensión html que están en el directorio '/casas'.

    El contenido de cada archivo html se lee en una cadena que se usa para crear un objeto de tipo House. 
    """
    ##Leer archivos html
     #archivo = open("casas/10053.html","r", encoding='utf-8')  ##encoding = 'utf-8' para windows

    archivo = open("casas/10053.html","r", encoding='utf-8')
    html = archivo.read() #leer archivo completo, y almacenarlo en un string(str)
    self.casa = House(html, '...')


  def get_homes(self):
    """Retorna un lista que contiene todo los objetos de tipo House creados en el constructor."""
    pass

contenedor = HousesContainer()
dic = contenedor.casa.get_feats()
print(dic)