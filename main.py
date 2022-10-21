from unicodedata import category
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

def separar_por_categoria(dataset,categorias):
	separated = dict()
	for categoría in categorias:
		separated[categoría] = dataset[dataset["Category"] == categoría]
	return separated

def obtenerCategorias(df):
    categorias = []
    df_categories = df["Category"].drop_duplicates()
    for x in df_categories:
        categorias.append(x)
    return categorias

def media(numeros):
	return sum(numeros) / len(numeros)

def deviaciónEstandar(numeros):
	promedio = media(numeros)
	varianza = sum([x - promedio] for x in numeros) / float(len(numeros) - 1)
	return sqrt(varianza)

nombres = ['URL','Category']


url_Dataset = pd.read_csv("./URL Classification.csv", names = nombres ,na_filter= False)
categorias = obtenerCategorias(url_Dataset)

categorias_separadas = separar_por_categoria(url_Dataset,categorias)
