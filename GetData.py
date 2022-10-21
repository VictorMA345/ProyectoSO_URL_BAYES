import pandas as pd

#Función para obtener datos de prueba
def getUrls():
    nombres = ['URL','Categoria']
    dataset = pd.read_csv("./URL Classification.csv", names = nombres ,na_filter= False)
    dataset1 = dataset[1:2001]
    dataset2 = dataset[50000:52000]
    dataset3 = dataset[520000:522000]
    dataset4 =dataset[535300:537300]
    dataset5 = dataset[650000:652000]
    dataset6= dataset[710000:712000]
    dataset7=  dataset[764200:766200]
    dataset8=  dataset[793080:795080]
    dataset9=  dataset[839730:841730]
    dataset10=  dataset[850000:852000]
    dataset11=  dataset[955250:957250]
    dataset12=  dataset[1013000:1015000]
    dataset13=  dataset[1143000:1145000]
    dataset14=  dataset[1293000:1295000]
    dataset15=  dataset[1492000:1494000]
    dt=pd.concat([dataset1,dataset2,dataset3,dataset4,dataset5,dataset6,dataset7,dataset8,dataset9,dataset10,dataset11,dataset12,dataset13,dataset14,dataset15], axis=0)
    dataset.drop(dataset.index[1:2000],inplace= True)
    dataset.drop(dataset.index[50000:52000],inplace= True)
    dataset.drop(dataset.index[520000:522000],inplace= True)
    dataset.drop(dataset.index[535300:537300],inplace= True)
    dataset.drop(dataset.index[650000:652000],inplace= True)
    dataset.drop(dataset.index[710000:712000],inplace= True)
    dataset.drop(dataset.index[764200:766200],inplace= True)
    dataset.drop(dataset.index[793080:795080],inplace= True)
    dataset.drop(dataset.index[839730:841730],inplace= True)
    dataset.drop(dataset.index[850000:852000],inplace= True)
    dataset.drop(dataset.index[955250:957250],inplace= True)
    dataset.drop(dataset.index[1013000:1015000],inplace= True)
    dataset.drop(dataset.index[1143000:1145000],inplace= True)
    dataset.drop(dataset.index[1293000:1295000],inplace= True)
    dataset.drop(dataset.index[1492000:1494000],inplace= True)
    dataset.drop(dataset.index[1492000:1494000],inplace= True)
    return dt['URL']

def obtenerCategorias(url_Dataset):
    categorias = []
    url_Dataset_categories = url_Dataset["Category"].drop_duplicates()
    for x in url_Dataset_categories:
        categorias.append(x)
    return categorias