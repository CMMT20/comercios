import os

list1 = ['plátano_de_canarias', 'banana', 'plátano_macho', 'uva_blanca_sin_semillas', 'uva_negra_sin_semillas', 'uva_roja_sin_semillas', 'manzana_golden', 'manzanas_golden', 'pera_conferencia', 'peras_conferencia', 'pera_ercolina', 'manzana_granny_smith']
# folder = "/Users/cmmt/StudioProjects/comercio/lib/pages"
folder2 = "/Users/cmmt/Downloads/mercadona_fruits_images/fruits"

list2 = os.listdir(folder2)
print(list2)
l1 = len(os.listdir(folder2))
print(l1)
for i in range(1, l1):
    print(i)
    source = folder2 + '/' + str(i) + '.jpg'
    print(source)

    destination = folder2 + '/' + list1[i-1] + '.jpg'
    print(destination)
    os.rename(source, destination)
