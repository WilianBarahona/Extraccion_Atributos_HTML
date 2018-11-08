##from os import listdir
from collections import OrderedDict
import re

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
   
    ##Expresiones regulares
    re_price = re.compile('^<p class="price">')
    re_location = re.compile('^<span class="location_info" itemprop="address">')
    re_size = re.compile('^<li class="dimensions">')
    re_num_bedrooms = re.compile('^<li class="bedrooms">')
    re_num_bathrooms = re.compile('^<li class="bathrooms">')
    re_inner_feats = re.compile('^<h2 class="title">Características interiores</h2>')
    re_outer_feats = re.compile('^<h2 class="title">Caracteristicas exteriores</h2>')
    re_environ_feats = re.compile('^<h2 class="title">Entorno</h2>')

    #Lectura string que contiene el html linea a linea
    lines = self.html.split('\n')

    #Inicio de banderas, necesarias para capturar todas las caracteristicas de las casas
    bool_inner_feats = False
    bool_outer_feats = False
    bool_environ_feats = False

    price = ''
    location = ''
    size = ''
    num_bedrooms = ''
    num_bathrooms = ''
    inner_feats = ''
    outer_feats = ''
    environ_feacts = ''

    for line in lines:
      line = line.lstrip() #lstrip borra spacios en blanco a la izquierda de una cadena
      
      if re_price.match(line): 
        price = line

      if re_location.match(line):
        location = line

      if re_size.match(line):
        size = line

      if re_num_bedrooms.match(line):
        num_bedrooms = line

      if re_num_bathrooms.match(line):
        num_bathrooms = line

      if re_inner_feats.match(line):
        bool_inner_feats = True
        bool_outer_feats = False
        bool_environ_feats = False

      if bool_inner_feats:
        if "tick" in line:
          inner_feats = inner_feats + line + '\n'
      
      if re_outer_feats.match(line):
        bool_inner_feats = False
        bool_outer_feats = True
        bool_environ_feats = False

      if bool_outer_feats:
        if "tick" in line:
          outer_feats = outer_feats + line + '\n'

      if re_environ_feats.match(line):
        bool_inner_feats = False
        bool_outer_feats = False
        bool_environ_feats = True

      if bool_environ_feats:
        if "tick" in line:
          environ_feacts = environ_feacts + line + '\n'
        
        
    ###========TEST Variables De Extraccion=========###   
    # print(price)
    # print(location)
    # print(size)
    # print(num_bedrooms)
    # print(num_bathrooms)
    # print(inner_feats)
    # print(outer_feats)
    # print(environ_feacts)

    # price = price.replace('<p class="price">','')  #Busca '<p class="price">' y todas las apariciones #las reemplaza por -->  ''
    # price = price.rstrip('</p>')   #Elimina la cadena '</p>' al final del str

    ###===========Reeplazo de texto===============###

    #Metodo para remplazar texto 
    def replace_all(text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text

    ###=============Diccionario ordenados: contiene pares de reemplazos===================####
    dic_replace_txt_price = OrderedDict([('L.', ''),('</p>', ''),('<p class="price">',''),(',',''),(' ','')])

    dic_replace_txt_location = OrderedDict([('<span class="location_info" itemprop="address">',''), ('</span>','')])

    dic_replace_txt_size =OrderedDict([('<li class="dimensions">',''), ('</li>',''), ('m2',''),(' ','')])

    dic_replace_txt_num_bedrooms =OrderedDict([('<li class="bedrooms">',''), ('</li>',''), ('Habitaciones',''), (' ','')])

    dic_replace_txt_num_bathrooms =OrderedDict([('<li class="bathrooms">',''), ('</li>',''), ('Baños',''), (' ','')])

    dic_replace_txt_feats =OrderedDict([('<li class="tick">',''), ('</li>','')])


    ###============Reemplazo de varibles==============########
    list_inner = []
    list_outer = []
    list_environ = []

    if price != '':
      price = replace_all(price , dic_replace_txt_price)

    if location != '':
      location = replace_all(location , dic_replace_txt_location)

    if size != '':
      size = replace_all(size , dic_replace_txt_size)

    if num_bathrooms != '':
      num_bedrooms = replace_all(num_bedrooms , dic_replace_txt_num_bedrooms) 

    if num_bathrooms != '':
      num_bathrooms = replace_all(num_bathrooms , dic_replace_txt_num_bathrooms)

    ####===========Insertar caracteristicas en una lista==============##
    ###=======Establecer un conjunto a partir de una lista ---> set_feats = set(lista)===##
    if inner_feats != '':
      inner_feats = replace_all(inner_feats , dic_replace_txt_feats)
      lines = inner_feats.split('\n')
      for line in lines:
        if line != '':
          list_inner.append(line)

    if outer_feats != '':
      outer_feats = replace_all(outer_feats , dic_replace_txt_feats)
      lines = outer_feats.split('\n')
      for line in lines:
        if line != '':
          list_outer.append(line)

    if environ_feacts != '':
      environ_feacts = replace_all(environ_feacts , dic_replace_txt_feats)
      lines = environ_feacts.split('\n')
      for line in lines:
        if line != '':
          list_environ.append(line)


    #### =============Test de variables ==========####
    # print(price)
    # print(location)
    # print(size)
    # print(num_bedrooms)
    # print(num_bathrooms)
    # print(list_inner)
    # print(list_outer)
    # print(list_environ)

    dic = {
    'price': price,
    'location': location,
    'size': size,
    'num_bedrooms': num_bedrooms,
    'num_bathrooms': num_bathrooms,
    'inner_feats': set(list_inner),
    'outer_feats': set(list_outer),
    'environ_feats': set(list_environ)
    }

    return dic

