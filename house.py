class House:

  def __init__(self, html, filename):
    """
    Recibe una cadena (str) con el contenido de un archivo con extesión ".html". Idealmente utiliza expresiones regulares para leer de esta cadena todas las características que se retornan a través del método get_feats().
    """
    self.html = html
    self.filename = filename
    
    

  def get_feats(self):
    """
    Retorna un dict() que contiene los atributos de la casa leídos desde la cadena con el código html de la página reciba en el constructor. El diccionario contendrá las siguientes cadenas como claves: price (precio), location (localización), size (tamaño), num_bedrooms (número de habitaciones), num_bathrooms (número de baños), inner_feats (características interiores), outer_feats (características exteriores) y environmental_feats (entorno). 
    Es posible que alguna casa no tenga características interiores (inner_feats), exteriores (outer_feats) o ambientales (environ_feats), es decir estas tres últimas son opcionales y en caso de no existir se retorna un conjunto vacío (conjunto NO lista).

    A continuación se muestra un ejemplo:

    {
      "price": "6370597",
      "location": "Colonia Alameda, Tegucigalpa, Francisco Morazán",
      "size": "267",
      "num_bedrooms": "4",
      "num_bathrooms": "3.5",
      "inner_feats": {"cisterna", "comedor", "sistema de alarma"},
      "outer_feats": {"garaje: si", "cuarto de servidumbre", "estudio", "sala"},
      "environ_feats: {"area social"}
    }

    """
    pass

