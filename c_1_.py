str1 = "import 'package:comercio/compra_page.dart';\nimport 'package:comercio/image_container.dart';\nimport 'package:flutter/material.dart';\n."
str2 = "\n"

str3 = "class Uvas extends StatelessWidget {\n"
str4 = "  @override\n"
str5 = "  Widget build(BuildContext context) {\n"
str6 = "    return CompraPage(\n"
str7 = "        image: 'images/uvas.png', rout1: '/', rout2: '/compras', precio: '2,5');\n"
str8 = "  }\n"
str9 = "}\n"

str0 = ''
for i in range (9):
    str0 += locals()[f'str{str(i+1)}']

print(str0)
