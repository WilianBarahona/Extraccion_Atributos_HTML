"""
=================DICCIONARIO=====================
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


======================Extraccion de datos===================

=====price=======
"price" extraer de: 
  <p class="price">L. 5,048,398</p>
expresion regular--> ^<p class="price">

=====location=======
"location"
  <span class="location_info" itemprop="address">lorem ipsum</span>
expresion regular--> ^<span class="location_info" itemprop="address">

========size========
"size" extraer de:
  <li class="dimensions">290m2</li>
expresion regular--> ^<li class="dimensions">

=====num_bedrooms=======
"num_bedrooms" extraer de:
  <li class="bedrooms">4 Habitaciones</li>
expresion regular--> ^<li class="bedrooms">

=======num_bathrooms=======
"num_bathrooms" extraer de:
  <li class="bathrooms">3.5 Baños</li>
expresion regular--> ^<li class="bathrooms">

========inner_feats=======
"inner_feats" extraer de:
Inicie con----> <h2 class="title">Características interiores</h2>      ----> finalize en </ul>
expresion regular-->^<h2 class="title">Características interiores</h2> 


========outer_feats========
"outer_feats" extraer de:
Inicie con----> <h2 class="title">Caracteristicas exteriores</h2>      ---> finalize en </ul>
expresion regular-->^<h2 class="title">Caracteristicas exteriores</h2>

==========environ_feats=========
"environ_feats extraer de:
Inicie con----> <h2 class="title">Entorno</h2>    ---> finalize en </ul>
expresion regular-->^<h2 class="title">Entorno</h2>

"""

""" 
=========codigo importante=========

leer archivo linea a linea
archivo=open("casas/8696.html","r")
html=''
for i in archivo:
  html=html+archivo.readline()

print(html)

"""

##from os import listdir
from collections import OrderedDict
from house import House
import re

#archivo = open("casas/10053.html","r", encoding='utf-8')  ##encoding = 'utf-8' para windows
files = '10564.html'
archivo = open("casas/" + files,"r", encoding='utf-8')
html = archivo.read() #leer archivo completo, y almacenarlo en un string(str)

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
lines = html.split('\n')

#Inicio de banderas, necesarias para capturar todas las caracteristicas de las casas
bool_inner_feats = False
bool_outer_feats = False
bool_environ_feats = False
environ_feacts=''

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
    inner_feats = ''
    bool_inner_feats = True
    bool_outer_feats = False
    bool_environ_feats = False

  if bool_inner_feats:
    if "tick" in line:
      inner_feats = inner_feats + line + '\n'
  
  if re_outer_feats.match(line):
    outer_feats = ''
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
list_environ = []
price = replace_all(price , dic_replace_txt_price)
location = replace_all(location , dic_replace_txt_location)
size = replace_all(size , dic_replace_txt_size)
num_bedrooms = replace_all(num_bedrooms , dic_replace_txt_num_bedrooms) 
num_bathrooms = replace_all(num_bathrooms , dic_replace_txt_num_bathrooms)
inner_feats = replace_all(inner_feats , dic_replace_txt_feats)
outer_feats = replace_all(outer_feats , dic_replace_txt_feats)
if environ_feacts != '':
  environ_feacts = replace_all(environ_feacts , dic_replace_txt_feats)
  lines = environ_feacts.split('\n')
  for line in lines:
    if line != '':
      list_environ.append(line)

########=====test=============######
# print(price)
# print(location)
# print(size)
# print(num_bedrooms)
# print(num_bathrooms)
# print(inner_feats)
# print(outer_feats)
# print(environ_feacts)

####===========Insertar caracteristicas en una lista==============##
###=======Establecer un conjunto a partir de una lista ---> set_feats = set(lista)===##
list_inner = []
lines = inner_feats.split('\n')
for line in lines:
  if line != '':
    list_inner.append(line)

list_outer = []
lines = outer_feats.split('\n')
for line in lines:
  if line != '':
    list_outer.append(line)



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
'num_bathrooms': num_bedrooms,
'inner_feats': set(list_inner),
'outer_feats': set(list_outer),
'environ_feats': set(list_environ)
}

print(dic)