#imports
from imports import *

""" 
Para el problema se tiene que hay 100 personas, 50 mujeres y 50 hombres
25 de 50 mujeres tienen el pelo largo y las demás tiene pelo corto, y de los hombres
2 tienen el pelo largo y 48 el pelo corto, se aplica inferencia bayesiana para este caso, 
de modo que se quiere inferir que tan probable es seleccionar una persona de cabello largo
"""
# Se definen las 2 categorías en hombres y mujeres
categorias = ['Mujeres con pelo largo','Hombres con pelo largo']

#Probabilidad de obtener un hombre o una mujer respectivamente
probs = [ 1/2 , 1/2]

#Se genera un modelo donde se asignan las posibilidades a cada categoría
previa = pd.Series(probs, categorias)
print(previa)

# Se declaran las probabilidades de que una persona sea de pelo largo en cada una de las categorías
tendencia = [ 1/2 , 1/25 ]

# al multiplicar obtenemos la posibilidad de obtenerlo en cada una de las categorías
posterior_sinNormalizar = tendencia * previa
print(posterior_sinNormalizar)

#Para obtener la probabilidad de obtener una persona de pelo largo se suman las probabilidades
prob_data = posterior_sinNormalizar.sum()
print(prob_data)

#Luego obtenemos un resultado de la inferencia al dividir el modelo por las probabilidades sumadas
posterior = posterior_sinNormalizar / prob_data
print(posterior)


xs = np.linspace(0,1,num = 101)
prob = 1/101
previa = pd.Series(prob,xs)

previa.plot()
plt.xlabel('Fraction of blue balls')
plt.ylabel('Probability')
plt.title('Prior')