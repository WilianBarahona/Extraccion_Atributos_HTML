correct_feats = [
  {'price': '6000000', 'inner_feats': {'Comedor', 'Calentador de agua', 'Baño de visita', 'Sistema de alarma', 'Aire acondicionado: Si', 'Sala y Comedor', 'Linea telefónica', 'Cisterna', 'Clósets', 'Circuito cerrado', 'Desayunador'}, 'outer_feats': {'Baño de servidumbre', 'Seguridad 24 horas', 'Vigilancia', 'Bodega', 'Patio', 'Estudio', 'Walk-in closet', 'Bomba de agua', 'Caseta de vigilancia', 'Garaje: Techado', 'Electricidad', 'Financiamiento disponible', 'Portón eléctrico', 'Sala de juegos', 'Cuarto de servidumbre', 'Tendedero', 'Sala'}, 'num_bedrooms': '4', 'num_bathrooms': '4', 'location': 'Colonia 15 de Septiembre, Tegucigalpa, Francisco Morazán', 'size': '337', 'environ_feats': {'Lavandería: Interna', 'Calle sin salida', 'Cerca de escuela', 'Cerca de zona comercial'}},
  {'price': '6370597', 'inner_feats': {'Comedor', 'Cisterna', 'Sistema de alarma'}, 'outer_feats': {'Estudio', 'Garaje: Si', 'Cuarto de servidumbre', 'Sala'}, 'num_bedrooms': '4', 'num_bathrooms': '3', 'location': 'Colonia Alameda, Tegucigalpa, Francisco Morazán', 'size': '267', 'environ_feats': {'Area social'}},
  {'price': '7692796', 'inner_feats': {'Circuito cerrado', 'Comedor', 'Sala y Comedor'}, 'outer_feats': {'Terreno en esquina', 'Cuarto de servidumbre', 'Sala'}, 'num_bedrooms': '4', 'num_bathrooms': '4', 'location': 'Colonia Loma Linda Norte, Tegucigalpa, Francisco Morazán', 'size': '250', 'environ_feats': set()},
  {'price': '2764599', 'inner_feats': {'Comedor', 'Secadora', 'Baño de visita', 'Sala y Comedor', 'Lavadora'}, 'outer_feats': {'Baño de servidumbre', 'Garaje: Si', 'Bodega', 'Cuarto de servidumbre', 'Sala'}, 'num_bedrooms': '8', 'num_bathrooms': '4.5', 'location': 'Tegucigalpa, Francisco Morazán', 'size': '140', 'environ_feats': {'Lavandería: Si'}},
  {'price': '5048398', 'inner_feats': {'Comedor', 'Baño de visita', 'Aire acondicionado: Si'}, 'outer_feats': {'Estudio', 'Jardín', 'Bodega', 'Cuarto de servidumbre', 'Sala'}, 'num_bedrooms': '4', 'num_bathrooms': '3.5', 'location': 'Colonia Las Lomas del Guijarro, Tegucigalpa, Francisco Morazán', 'size': '290', 'environ_feats': {'Area social', 'Lavandería: Si'}}
]

grade = 0

def end_and_print_grade():
  print('=' * 79)
  if grade == 100:
    print('¡Felicidades no se detectó ningún error!')
  print(('Su nota asignada es: NOTA<<{0}>>').format(grade if grade >= 0 else 0))
  exit()

try:
  from houses_container import HousesContainer as HC
except Exception as e:
  print('No se pudo importar la clase HousesContainer del módulo houses_container')
  print(('El error recibido fue:\n{0}').format(e))
  end_and_print_grade()

try:
  hc = HC()
except Exception as e:
  print('No se pudo crear una instancia de HousesContainer')
  end_and_print_grade()

try:
  homes = hc.get_homes()
except Exception as e:
  print('No se pudo obtener la lista de casas con get_homes()')
  print(('El error recibido fue:\n{0}').format(e))
  end_and_print_grade()

for h in homes:
  try:
    h_feats = h.get_feats()
  except Exception as e:
    print('No se pudo obtener la lista de atributos de una casa.')
    print(('El error recibido fue:\n{0}').format(e))
  else: 
    if h_feats not in correct_feats:
      print('Los siguientes atributos obtenidos no coinciden con la respuesta correcta:')
      print(h_feats)
      print('Revise las respuestas correctas en la lista correct_feats del archivo autograder.py')
      print(('El error recibido fue:\n{0}').format(e))
    else:
      print('Atributos correctos +20%')
      grade += 20

end_and_print_grade()