# ProyectoSO_URL_BAYES
# Clasificacion URL con Naive Bayes

Los clasificadores por medio de los métodos de Naive Bayes son algoritmos de aprendizaje automático que aunque su simplicidad es simple en realidad tienen mucho potencial. Se basan en la probabilidad condicional y el teorema de Bayes. En este proyecto se puede observar los resultados tras el uso de estos algoritmos en conjunto de las herramientas de programación en conjunto de respectivas librerías que nos ayudaran a tener como resultado la clasificación de las categorías. 


# Web Scraping

Web scraping se refiere al proceso de extracción de contenido y datos de páginas web mediante software. Por ejemplo, la mayoría de los servicios de comparación de precios utilizan herramientas de web scraping para leer información de precios de diferentes tiendas en línea. Otro ejemplo es Google, que raspa o "rastrea" regularmente la web para indexar páginas web.
La información extraída mediante esta técnica de seguimiento puede ser de cualquier tipo, desde datos de contacto de un sitio web hasta palabras clave o URL, entre otros.
Si bien a primera vista puede parecer que cualquier persona puede obtener información de cualquier sitio web, la verdad es que la minería de datos no siempre es legal.
Las ventajas que ofrece el uso de web scraping


## Ventajas que nos brinda el uso del Web scraping

**Conocer mejor a tus competidores:** gracias a los datos que obtienes, puedes trabajar en mejorar el posicionamiento web de tu sitio
**Extraer datos de cualquier naturaleza:** esto puede resultar de gran utilidad para las páginas que ofrecen un servicio de comparación de ofertas.



# Procesos Multinúcleo

Multinúcleo se refiere a arquitecturas en las que un único procesador físico contiene la lógica central de varios procesadores. Se utiliza un solo circuito integrado para empaquetar o contener estos procesadores. El objetivo es crear un sistema que pueda manejar más tareas simultáneamente, mejorando el rendimiento general del sistema.

El concepto de tecnología multinúcleo se centra principalmente en las posibilidades de computación paralela. La computación paralela puede mejorar en gran medida la velocidad y la eficiencia de las computadoras al combinar dos o más unidades centrales de procesamiento (CPU) en un solo chip.

## ¿Es beneficioso utilizar procesos multinúcleo?

Claramente la cantidad de tiempo y procesamiento que se ahorra es significativo, pero esto es relativo, depende mucho de la cantidad de datos con las que se va a operar, si poseemos un dataset de mucho menor volumen claramente no es recomendable hacer uso de multinúcleo porque al final podría ser contraproducente y no se vería una mejora significativa en los tiempos de ejecución y procesamiento. Pero para este proyecto en cuestión si se presentó un beneficio con el uso y la implementación del multicore.
# Librerias Utilizadas
## Pandas
Pandas es una herramienta de análisis y manipulación de datos de código abierto rápida, potente, flexible y fácil de usar, este fue construido sobre el lenguaje de programación Python.
Las ventajas que nos brinda Pandas son las siguientes:
-   Un objeto **DataFrame** rápido y eficiente para la manipulación de datos con indexación integrada.
    
-   Herramientas para **leer y escribir** datos entre estructuras de datos en memoria y diferentes formatos: CSV y archivos de texto, Microsoft Excel, bases de datos SQL, y el rápido formato HDF5.
    
-   **Alineación** inteligente de datos y manejo integrado de **datos faltantes**: Obtenga alineación automática basada en etiquetas en cálculos y manipule fácilmente datos desordenados en una forma ordenada.
    
-   **Remodelación** flexible y pivote de conjuntos de datos.
    
-   Segmentación inteligente basada en **etiquetas**,  **indexación sofisticada**  y**subconjunto** de grandes conjuntos de datos.
    
-   Las columnas se pueden insertar y eliminar de las estructuras de datos por **tamaño mutabilidad**;
    
-   Agregación o transformación de datos con un potente **grupo por** motor permitir operaciones de división-aplicación-combinación en conjuntos de datos;
    
-   **Fusión y unión** de conjuntos de datos de alto rendimiento;
    
-   **La indexación de ejes jerárquicos** proporciona una forma intuitiva de trabajar con datos de alta dimensión en una estructura de datos de dimensión inferior;
    
-   **Funcionalidad de series temporales**: generación de intervalos de fechas y frecuencia conversión, mover estadísticas de ventanas, cambio de fecha y retraso. Incluso crear compensaciones de tiempo específicas del dominio y tiempo de unión series sin perder datos;
    
-   Altamente **optimizado para el rendimiento**, con rutas de código críticas escritas en Python o C.
    
-   Python con la librería Pandas está en uso en una amplia **variedad de dominios comerciales**, incluyendo Finanzas, Neurociencia, Economía, Estadísticas, publicidad, analítica web y más.
### Instalación
El proceso de Instalación de Pandas es sencillo y es meramente la ejecución de un código en la terminal del entorno de programación, para esto previamente hay que tener instalado Python.

**Código:** $pip install pandas
## Numpy
NumPy es el paquete fundamental para la computación científica en Python. Es un Biblioteca de Python que proporciona un objeto de matriz multidimensional, varios derivados objetos (como matrices y matrices enmascaradas) y una variedad de rutinas para operaciones rápidas en matrices, incluida la manipulación matemática, lógica y de formas, ordenar, seleccionar, E/S, transformadas discretas de Fourier, álgebra lineal básica, Operaciones estadísticas básicas, simulación aleatoria y mucho más.
Las utilidades que nos da Numpy son:
**POTENTES MATRICES N-DIMENSIONALES:** Rápidos y versátiles, los conceptos de vectorización, indexación y difusión de NumPy son los estándares de facto de la computación de matriz actual.
**HERRAMIENTAS INFORMÁTICAS NUMÉRICAS:** NumPy ofrece funciones matemáticas completas, generadores de números aleatorios, rutinas de álgebra lineal, transformadas de Fourier y más.
**INTEROPERABLE:** NumPy admite una amplia gama de plataformas informáticas y de hardware, y funciona bien con bibliotecas distribuidas, de GPU y de matrices dispersas.
**EFICAZ:** El núcleo de NumPy es un código C bien optimizado. Disfrute de la flexibilidad de Python con la velocidad del código compilado.
**FÁCIL DE USAR:** La sintaxis de alto nivel de NumPy lo hace accesible y productivo para programadores de cualquier nivel de experiencia o formación.
**CÓDIGO ABIERTO:** Distribuido bajo unalicencia BSD liberal, NumPy es desarrollado y mantenidopúblicamente en GitHubpor unacomunidad vibrante, receptiva y diversa.
### Instalación
El proceso de Instalación de Numpy es sencillo y es meramente la ejecución de un código en la terminal del entorno de programación, para esto previamente hay que tener instalado Python.

**Código de Instalación:** $pip install numpy

## Flask
Flask es un framework web, es un módulo de Python que permite desarrollar aplicaciones web fácilmente. Tiene un núcleo pequeño y fácil de extender: es un microframework que no incluye un ORM (Object Relational Manager) o tales características.
Tiene muchas características interesantes como enrutamiento de url, motor de plantillas. Es un marco de aplicación web WSGI.

Flask es un marco de aplicación web escrito en Python. Fue desarrollado por Armin Ronacher, quien dirigió un equipo de entusiastas internacionales de Python llamado Poocco. Flask se basa en el kit de herramientas Werkzeg WSGI y el motor de plantillas Jinja2. Ambos son proyectos Pocco.

### Herramientas
**WSGI**
La interfaz de puerta de enlace de servidor web (interfaz de puerta de enlace de servidor web, WSGI) se ha utilizado como estándar para el desarrollo de aplicaciones web de Python. WSGI es la especificación de una interfaz común entre servidores web y aplicaciones web.

**Werkzeug**
Werkzeug es un kit de herramientas WSGI que implementa solicitudes, objetos de respuesta y funciones de utilidad. Esto permite construir un marco web sobre él. El marco Flask utiliza Werkzeg como una de sus bases.

**jinja2**
jinja2 es un motor de plantillas popular para Python.Un sistema de plantillas web combina una plantilla con una fuente de datos específica para representar una página web dinámica.
### Instalación
El proceso de Instalación de Flask y todas sus herramientas es sencillo y es meramente la ejecución de un código en la terminal del entorno de programación, para esto previamente hay que tener instalado Python.

**Código de Instalación:**  $ pip install Flask


## Beautiful Soup
Es un Biblioteca de Python para extraer datos de archivos HTML y XML. Funciona con su analizador favorito para proporcionar formas idiomáticas de navegación, buscar y modificar el árbol de análisis.
Para usarlo, es necesario especificar un parser, que es responsable de transformar un documento HTML o XML en un árbol complejo de objetos Python. Esto permite, por ejemplo, que podamos interactuar con los elementos de una página web como si estuviésemos utilizando las herramientas del desarrollador de un navegador.
### Instalación
El proceso de Instalación de Beautiful Soup es sencillo y es meramente la ejecución de un código en la terminal del entorno de programación, para esto previamente hay que tener instalado Python.

**Código de Instalación:** $pip install beautifulsoup4

## Tiempos de Respuesta
Los tiempos de respuesta lanzaron un tiempo aproximado de el Web Scraping dio un tiempo de ejecucion de 476.18723583221436  segundos mientras que el Bayes nos arrojo un tiempo de 0.7699155807495117  Segundos todo esto en una prueba de 300 paginas. Como se menciono anteriormente entre mas paginas mejor.
## Resultados
Para el modelado de los datos que se obtuvieron tanto de las categorias como tambien de las paginas web recolectadas mediante el proceso de la ejecucion de software se hizo uso de la herramienta Flask para modelar la pagina web
que demostrara los datos de manera grafica y interactiva para el usuario, el usuario puede seleccionar la categoria que se desea observar y al darle click se le redireccionara a los datos por pagina que tengan relacion con dicha categoria.


![image](https://user-images.githubusercontent.com/39351969/199588073-2e3631c7-9370-4063-82ac-a88bc2e4e456.png)

![image](https://user-images.githubusercontent.com/39351969/199588134-5e831671-30b5-4381-811d-b33b09e5254d.png)

Las pruebas se realizaron con el Dataset correspondiente y la categorizacion resulto de la siguiente manera.
![image](https://user-images.githubusercontent.com/39351969/199591248-5e2def6c-b8e3-41cf-b8d6-968305e5aeb7.png)
![image](https://user-images.githubusercontent.com/39351969/199591311-3dd4f8c9-c6b1-4cd2-a6bd-4c6e3514b87f.png)


## Referencias
_Beautiful Soup Documentation — Beautiful Soup 4.9.0 documentation_. (s. f.). Recuperado 2 de noviembre de 2022, de https://www.crummy.com/software/BeautifulSoup/bs4/doc/

_NumPy documentation — NumPy v1.23 Manual_. (s. f.). Recuperado 2 de noviembre de 2022, de https://numpy.org/doc/stable/

_pandas - Python Data Analysis Library_. (s. f.). Recuperado 2 de noviembre de 2022, de https://pandas.pydata.org/

_Welcome to Flask — Flask Documentation (2.2.x)_. (s. f.). Recuperado 2 de noviembre de 2022, de https://flask.palletsprojects.com/en/2.2.x/
