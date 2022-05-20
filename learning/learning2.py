import pandas as pd
from PIL import Image
import glob

sheet_id = '1WxkdUPn9lUj6T2e14ma27io7MMZvjd08LjYKk35Vf8w'
df = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv')
var1 = df.name.tolist()
print(var1)
# ['Plátano de Canarias', 'Banana', 'Plátano macho', 'Uva blanca sin semillas', 'Uva negra sin semillas', 'Uva roja sin semillas', 'Manzana Golden', 'Manzanas Golden', 'Pera Conferencia', 'Peras Conferencia', 'Pera Ercolina', 'Manzana Granny Smith']


# your_path: str = '/Users/cmmt/Downloads/mercadona\ fruits\ images/fruits'
# image_list = map(Image.open, glob.glob(f"{your_path}/*.jpg"))
# print(image_list)
