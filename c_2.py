import pandas as pd
import a_comercio_app_str0

#---- 1 from gsheet get the list of new products
#---- 1.1 extrac data from gsh
folder = "/Users/cmmt/StudioProjects/comercio/lib/pages/"


sheet_id = '1WxkdUPn9lUj6T2e14ma27io7MMZvjd08LjYKk35Vf8w'
df = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv')
prices0 = df.price.tolist()
# print(prices0)
names0 = df.name.tolist()
# print(names0)
# ['Plátano de Canarias', 'banana', 'Plátano macho', 'Uva blanca sin semillas', 'Uva negra sin semillas', 'Uva roja sin semillas', 'Manzana Golden', 'Manzanas Golden', 'Pera Conferencia', 'Peras Conferencia', 'Pera Ercolina', 'Manzana Granny Smith']

names_file = [i.lower().replace(' ', '_') for i in names0]
# print(names_file)
# ['plátano_de_canarias', 'banana', 'plátano_macho', 'uva_blanca_sin_semillas', 'uva_negra_sin_semillas', 'uva_roja_sin_semillas', 'manzana_golden', 'manzanas_golden', 'pera_conferencia', 'peras_conferencia', 'pera_ercolina', 'manzana_granny_smith']

names_class = [i.title().replace(' ', '') for i in names0]
# print(names_class)
# ['PlátanoDeCanarias', 'Banana', 'PlátanoMacho', 'UvaBlancaSinSemillas', 'UvaNegraSinSemillas', 'UvaRojaSinSemillas', 'ManzanaGolden', 'ManzanasGolden', 'PeraConferencia', 'PerasConferencia', 'PeraErcolina', 'ManzanaGrannySmith']

#---- 2.1 actual routs conf in flutter project      str0
str_routs = "'/': (context) => Screen0(),'/compras': (context) => Compras(),'/citas': (context) => Citas(),"
str_imports = '''
import 'package:flutter/material.dart';
import 'screen0.dart';
import 'compras.dart';
import 'citas.dart';
import 'uvas.dart';\n
'''

#---- 2.2 generate code to the new routs conf to replace the actual     str0
counter = 0
for i in names0:
    str_routs += f"'/{i.lower().replace(' ', '_')}': (context) => {i.title().replace(' ', '')}(),"
    # print(i.capitalize())

    str1 = "import 'package:comercio/compra_page.dart';\nimport 'package:comercio/image_container.dart';\nimport 'package:flutter/material.dart';\n."
    str2 = "\n"

    # / Uvas
    str3 = f"class {i.title().replace(' ', '')} extends StatelessWidget {{\n"
    str4 = "  @override\n"
    str5 = "  Widget build(BuildContext context) {\n"
    str6 = "    return CompraPage(\n"
    # / 'uvas.jpg'    '/'    '/compras'      '2,5'
    str7 = f"        image: 'images/{i.lower().replace(' ', '_')}.jpg', rout1: '/', rout2: '/{i.lower().replace(' ', '_')}', precio: {prices0[counter]});\n"
    str8 = "  }\n"
    str9 = "}\n"

    str_page = ''
    for j in range(9):
        str_page += locals()[f'str{str(j + 1)}']


    #---- 2.3.1 create new files.dart for each new product, for each new page, in the right flutter project dir
    with open(f"{folder}/{i.lower().replace(' ', '_')}.dart", 'w') as f:
        f.write(str_page)

    str_import = f"import './pages/{names_file[counter]}.dart';\n"
    str_imports += str_import

#---- 2.3.2 and write the code for this page/product

    counter += 1

print(str_routs)
print(str_imports)
