# Enterprise - Especificación Funcional - Expresiones y Funciones

## Descripción del Documento

El presente documento describe el funcionamiento y la sintaxis de las expresiones y funciones (de usuario
y de sistema) que se utilizan en FastPrg.

## Definiciones y Acrónimos

```
Término Definición
Expresión Serie de Operandos combinados con Operadores, con el objetivo de producir
un determinado Tipo de Dato al evaluarse en un Contexto
Función Grupo de instrucciones con un objetivo en particular y que se ejecuta al ser
llamada desde otra Función o desde una expresión
Contexto Delimita qué elementos están disponibles para la evaluación de la expresión
Tipo de dato Tipo de atributo del resultado de la evaluación de la expresión
Operandos Elementos que contienen el valor para la evaluación de la expresión
Operador Elementos que realizan una operación
Parámetros Conjunto de elementos que se reciben al momento de invocar a las
funciones
Función interactiva Función con al menos un parámetro interactivo
Parámetro interactivo Parámetro que implica una interacción del usuario que puede asignar o
modificar su valor
```
## 1. Introducción

En primer lugar, a los fines de comprender a qué nos referimos cuando hablamos de **expresiones** ,
debemos recordar que “FastPrg es una plataforma de desarrollo, ejecución y evolución ágil de
aplicaciones de negocios”.
Para lograr esto, uno de los aspectos fundantes de FastPrg consiste en que los desarrollos no requieran
de programadores expertos que modifiquen el código fuente de la plataforma, sino que sea directamente
un usuario conocedor del negocio quien pueda cambiar el comportamiento del sistema.
Es por esto que FastPrg crea un lenguaje de programación propio, de alto nivel, el cual nos permite, de
forma intuitiva, realizar variaciones en el funcionamiento dentro de la plataforma. Este lenguaje está
formado por expresiones.
Éstas nos posibilitan obtener un resultado a partir de la evaluación de una fórmula en un contexto. Esta
fórmula está compuesta por una serie de operandos y operadores, la cual está escrita en un lenguaje
intuitivo y específico de FastPrg, a partir del cual podemos asemejar las expresiones al lenguaje coloquial,
de manera que sea innecesario tener conocimientos en el área del desarrollo de software.
Cabe destacar que cada usuario que escriba una expresión lo hará en su idioma y FastPrg la
internacionalizará, a fin de que, si otro usuario ingresa en una lengua diferente la visualice en esa misma,
con la que accedió.
Por ejemplo:
**Español**

```
En Cliente Buscar Correo electrónico Cuando Teléfono Comienza con ‘341’
```
**Inglés**

```
In Client Search Email When Phone start with ‘341’
```
Las expresiones cambian de idioma en función del Idioma de interfaz de usuario definido en las
preferencias del mismo. Es importante resaltar que los nombres de los operadores y los nombres de las
instrucciones, en todos los idiomas, son palabras clave reservadas. Esto implica que no podrán crearse
Entidades, atributos o acumuladores que contengan en sus nombres alguna palabra clave reservada.

Podremos indicar una expresión en cualquier lugar donde se nos presente el siguiente ícono , y
dependiendo de dónde lo hagamos, tendremos distintos usos. Entre ellos, la asignación de valores a un
atributo, ya sea en un desencadenante, un valor inicial o valor calculado. También, podemos utilizar
expresiones en filtros de instancias o ítems, como así también en la definición de condiciones, tanto de
una regla de negocio como de una transformación, entre otros.


Veamos, ahora, un ejemplo. Tenemos una grilla de productos, pero nos interesa visualizar solo aquellos
que se encuentren disponibles para la venta. Es importante aclarar que existe un atributo lógico llamado
Vendible, el cual nos permite identificar este grupo específico de instancias, dentro de la entidad
Producto. Para esto, nos posicionamos sobre la grilla, desplegamos el panel de propiedades, luego, damos
clic en el símbolo de Expresiones del filtro y escribimos que la categoría sea vendible, es decir:

```
Vendible = verdadero
```
O simplemente

```
Vendible
```
En consecuencia, se filtran los productos y vemos únicamente aquellos que cumplen con lo escrito.
Podemos filtrar, también, por ejemplo, por los productos pertenecientes a un rubro o a una marca
particular:

```
Obtener traducción(Rubro.Rubro;’es’) = ’Aceites y lubricantes’
```
Incluso, podemos filtrar los que sean de cierto rubro y, a su vez, vendibles.

```
Obtener traducción(Rubro.Rubro;’es’) = ’Aceites y lubricantes’ y vendible
```
De esta manera, tenemos la posibilidad de escribir miles de expresiones.

Al hacer clic o tap en el ícono de expresiones, se abre una ventana donde podemos especificar la
expresión. A esa ventana la llamamos **Editor de expresiones**. El objetivo de esta ventana es proveer un
acceso rápido a los distintos elementos del modelo, a las funciones y operadores. Por otro lado, en algunos
formularios el Editor de Expresiones se encuentra embebido en los mismos formularios.
El Editor de Expresiones presenta los siguientes elementos:

- Una caja de texto donde se ingresa la Expresión.
- Un panel inferior donde se tiene acceso a las distintas herramientas que facilitan el armado de la
    expresión. Este panel se encuentra colapsado si el Editor está embebido en el formulario.
El **Área de texto** cuenta con una barra de herramientas para acceder a un conjunto de acciones que
podrán variar en función del tipo de dato que espera el contenedor de la Expresión:
- **Texto Enriquecido** , se muestra un conjunto de herramientas para dar formato al texto, similar al
siguiente:
- **Contenido Multimedia** se presentan íconos asociados a las siguientes funcionalidades:
o **Insertar Imágenes Prediseñadas** : Ventana que permite seleccionar una imagen
prediseñada, la cual será insertada dentro de la expresión.
o **Insertar Contenido Multimedia** : Ventana que permite seleccionar un archivo local que
contiene una imagen, video o audio, el cual será insertado dentro de la expresión.

Nota de arquitectura
Para el caso en que el tipo de dato contenido en la Expresión sea de Texto Enriquecido o de Contenido
Multimedia, no se permitirá ingresar operaciones, funciones u otros elementos del modelo que se evalúan
dinámicamente, sino que sólo se permitirá ingresar contenido estático.

Además, en el área de texto, tenemos las siguientes características para facilitar el uso de las expresiones:

- **Resaltado de Sintaxis** : Permite facilitar la lectura de las Expresiones.
    El texto se visualiza automáticamente con diferentes tipografías y estilos en función de la
    categoría de los términos. Por ejemplo, los Atributos, Operadores, Literales, Funciones, etc.
    tendrán diferentes tipografías y estilos, los cuales serán configurados mediante una
    parametrización del sistema.
    Inicialmente se usarán los siguientes colores:
    - Instrucciones, operadores: Rojo
    - Entidades: Azul
    - Atributos y acumuladores: Azul
    - Literales: Verde
    - Funciones: Fucsia


```
En Cliente Buscar Email Cuando Teléfono COMIENZA CON “5”
```
- **Resaltado de errores.** En el caso de que la Expresión introducida tenga algún error, se resaltará
    el texto que lo haya producido y se indicará con un tooltip el detalle del mismo. En la siguiente
    imagen se muestra (a título informativo) un ejemplo de esta funcionalidad, donde
    adicionalmente al detalle del error se presentan acciones correctivas:
- **Asistencia de contenidos** : Sugiere, en base al contexto, el contenido que le puede ser de utilidad
    al usuario para “autocompletar” el texto que está introduciendo. Esta funcionalidad usa la
    búsqueda incremental (y no predictiva) descripta en el documento de estándares. Algunos casos
    de uso:
       o Si se empieza a escribir una palabra, se van sugiriendo nombres de Entidades,
          Funciones, Operadores, etc. los cuales se pueden utilizar en base al resto de la Expresión
          y los caracteres ya introducidos. Por ejemplo, si se está escribiendo un parámetro de
          una Función que espera una Entidad, solo se muestran Entidades. Si se escribió “En
          Cliente” se sugieren otras instrucciones que se pueden usar a continuación, por
          ejemplo: Buscar, Primer, Cuando, Ordenar, etc.
       o Si se introduce un punto luego del nombre de una Entidad, se mostrará el listado de
          todos sus Atributos y Acumuladores.
       o Si se introduce un punto luego de un Atributo que no sea de categoría simple, se
          mostrará el listado de Atributos subordinados disponibles.
       o En el caso de que luego de un atributo se introduzca un operador lógico o de
          comparación, el sistema ira proponiendo valores de dichos atributos a partir de las
          instancias existentes. Por ejemplo, si el usuario escribe “Ciudad.Nombre =” en el listado
          se mostrará el listado de ciudades existentes en dicha Entidad. En el caso de que la
          operación soporte que se le pase más de un valor, por ejemplo Cliente.Nombre EN
          (.......), se le permitirá al usuario que seleccione más de una instancia y se completará la
          Expresión con todas las instancias seleccionadas separadas por el separador de listas del
          usuario.
El panel inferior cuenta con las siguientes herramientas:
- **Elementos.** Se visualizan todos los atributos y acumuladores que se pueden utilizar en la
Expresión. Este listado se va desplazando dinámicamente en base a lo que se está escribiendo en
el área de texto de la Expresión, por ejemplo, si se ingresó un nombre de una Entidad en el área
de texto, automáticamente el árbol se ubicara en dicha entidad mostrándola expandida de forma
de visualizar sus atributos. Adicionalmente esta solapa mostrará un área de texto donde se
visualizará el detalle del Elemento visualizado, este detalle se obtendrá de la descripción y
documentación del mismo.
- **Funciones**. Se muestran las Funciones disponibles (agrupadas por la categoría a la cual
pertenecen), y la descripción y documentación del uso de la Función. Las Funciones están
clasificadas y se muestran en primer lugar las específicas y luego las genéricas.
o **Funciones genéricas** : Son las que pueden ser utilizadas en cualquier expresión sin
importar en qué elemento del modelo se utilizan. Por ejemplo, funciones aritméticas y
las de cadena de texto.
o **Funciones específicas** : Las mismas son particulares para ciertos elementos del modelo.
Son ejemplos de estos tipos las Funciones de información del sistema como las que se
usan para obtener el valor de la tolerancia o el saldo por diferencia de conversión desde
una regla de cancelación.
- **Operadores**. Se muestran los Operadores disponibles y la descripción y documentación de cada
uno de ellos a modo de ayuda.
- **Contexto inicial**. Muestra el contexto inicial de la expresión
- **Tipo de atributo de retorno**. Tipo de atributo del resultado de la expresión.


Hablemos ahora de las **Funciones**. En FastPrg podemos emplearlas para llevar a cabo diferentes tareas,
por llamarlas de algún modo. Por un lado, nos permiten realizar cálculos dependiendo de otros valores. Y
en las funciones tenemos el plus de que podemos utilizar parámetros. Si bien más adelante entraremos
en detalle, mencionaremos un caso práctico: podríamos usarla para aplicar determinado descuento, solo
si el cliente es de cierto tipo, por ejemplo, mayorista.
Por otro lado, nos posibilitan centralizar una expresión, de manera que podamos estandarizarla. En caso
de que necesitemos la misma expresión en varios lugares distintos, podemos crear una función que la
contenga y solo reutilizarla en esos otros lugares. Es por esto que, si posteriormente queremos cambiar
la expresión, solo bastará con modificarla en la función. Como consecuencia, de modo automático, este
cambio se verá reflejado en cada lugar que la hayamos empleado, otorgando, así, una mejor adaptabilidad
al cambio y quitándonos la responsabilidad de recordar cada lugar en que se utilizó.
Además, las funciones nos permiten solicitar al usuario el ingreso de valores en forma interactiva. Por
ejemplo, podríamos realizar un filtro en un GDI, en el cual el usuario deba seleccionar una fecha de inicio
y una de fin, y a partir de eso, se filtre el contenido del GDI, según el plazo establecido. Asimismo, al
momento de exportar instancias podemos definir que la función nos pida un período contable y que, al
ejecutarla, exporte las instancias correspondientes a ese lapso de tiempo.
Sigamos con más casos prácticos. También, podemos valernos de funciones a través de las cuales
consumir servicios web. Por ejemplo, una que solicite el código CAE a la AFIP y lo inserte en la factura
electrónica; o que consuman dispositivos, como una lectora de códigos, la cual nos devuelva el precio y la
descripción del producto identificado.
Incluso, podemos utilizarlas para obtener información del sistema, tales como las funciones

```
HOY()
```
que nos indica la fecha actual, o

```
USUARIO()
```
la cual nos devuelve el usuario que ha iniciado la sesión.

## 2. Expresiones

### 2.1 Definición y elementos

Veamos ahora los elementos de una expresión y cómo estos influyen en su evaluación. Para esto, vamos
a descomponer una expresión sencilla en partes y las analizaremos.
Como se trata de un lenguaje de expresiones, FastPrg tiene sus propias reglas, y para que una expresión
sea válida debe cumplirlas.
Las expresiones permiten **obtener un resultado a partir de la evaluación de una fórmula**. A través de sus
elementos, intentaremos ampliar un poco esta definición, pero antes de comenzar, necesitamos una
estructura de datos con la que trabajaremos, que será la de una Factura.

Podemos ver que tiene un número identificatorio, una fecha, un cliente a quien pertenece, un total y una
colección de ítems (donde cada uno, a su vez, cuenta con un producto, un precio, una cantidad y un
subtotal).

Supongamos que queremos modelar una expresión simple, que calcule el subtotal de cada ítem de la
factura

```
Precio * Cantidad
```
O el total de la factura en sí.

```
En .Ítems Sumar Subtotal
```
Ahora, desglosaremos la primera, la cual indica que, si compramos, por ejemplo, dos ítems, con un precio
de dos mil quinientos cada uno, el subtotal es cinco mil. Si bien esta expresión es muy sencilla, nos
alcanzará para comprender cada uno de sus elementos.

Tal como señalamos anteriormente, las expresiones permiten obtener un resultado a partir de su
evaluación, el cual, como todo en FastPrg, tiene un tipo de atributo asociado, llamado “ **Retorno** ”. En
nuestro ejemplo de precio por cantidad, el tipo de dato esperado es el subtotal.


Esta expresión se evaluará en cada uno de los ítems de la factura, tomará el precio de cada uno y lo
multiplicará por la cantidad de ítems. A esto, lo llamamos **contexto** , es decir, nos indica qué elementos
tenemos disponibles para la evaluación de la expresión.
Según este último elemento que describimos, la sintaxis será correcta o incorrecta. Si quisiéramos usar
esta misma expresión a nivel de cabecera, FastPrg nos marcaría que los atributos Precio y Cantidad no
existen, ya que sí están en el contexto del ítem, pero no de la entidad. En nuestro ejemplo, el contexto de
evaluación es el ítem de la factura.
Pero para evaluar algo, necesitamos que exista, al menos, un componente que tenga valor. En este caso
que estamos analizando, existen dos: precio y cantidad, y los llamamos **Operandos**. En otras palabras,
estos son los elementos que contienen el valor para la evaluación de la expresión.
Particularmente, nuestros operandos son atributos, pero también podrían ser números, fechas, textos,
entre otros. Todo dependerá de qué queramos obtener con nuestra expresión.
Entonces, ya vimos qué son los operandos, pero ahora necesitamos unirlos, combinarlos, de alguna
manera. Y es aquí donde aparecen los **operadores** ; elementos que realizan una operación (como cálculos,
comparaciones o cualquier otra) entre uno o más operandos. En nuestro sencillo ejemplo de precio por
cantidad, tenemos un único operador y es el de multiplicación, identificado con un asterisco.

Podemos mencionar, ahora, la siguiente definición, más completa: **una Expresión está formada por una
serie de Operandos combinados con Operadores, con el objetivo de producir un determinado Tipo de
Dato al evaluarse en un Contexto.**
Es importante destacar que internamente no será necesario guardar el formato con el que un usuario
escribió los nombres de las Entidades, Atributos, Palabras reservadas, Funciones, etc. La expresión se
visualizará directamente usando el formato original con el que fueron definidos. Por ejemplo, si un usuario
crea la siguiente expresión:

```
fActurA.imporTE > 10
```
Cuando la vuelva a visualizar se verá:

```
Factura.Importe > 10
```
Suponiendo que en el Diccionario de Datos el nombre de la Entidad es “Factura” y el nombre del Atributo
es “Importe”.

### 2.2 Contextos

Como mencionamos, el contexto es una parte fundamental de la expresión, ya que depende de él si la
sintaxis de la misma es correcta o no. El contexto nos permite identificar cuáles son los operandos que
podemos utilizar en nuestra fórmula. Una misma expresión en contextos diferentes, deja de tener sentido
o directamente: muestra mensaje de error.


Para comprender a qué nos referimos, supongamos que estamos posicionados en una factura y queremos
saber el nombre del cliente y si es de tipo mayorista. Como buscamos obtener el nombre del Cliente,
requerimos alguna manera de navegar entre los diferentes contextos. Para solucionar esto, dentro del
lenguaje de Expresiones provisto por FastPrg, existe el operador “.”.

Este operador se utiliza para navegar entre distintos atributos de tipo referencia, colecciones,
compuestos, acumuladores y secuencias. En este sentido, si deseamos acceder al nombre del cliente
desde la factura, simplemente escribimos la expresión

```
Cliente.Nombre
```
Por ejemplo, para escribir un correo electrónico, podemos comenzar con “Hola ” + Cliente.Nombre, donde
el operador de adición (“+”) une el saludo con el nombre.

Entonces, si el **contexto inicial** era la entidad Factura, al escribir “Cliente.” este cambia automáticamente.
El **nuevo contexto** es la entidad Cliente, es decir, el cliente relacionado con la factura que estamos
haciendo. En este caso, recurrimos al nombre, pero también podemos acceder a la ciudad, a sus
direcciones; a cualquier atributo de dicha entidad. De este modo, tenemos toda la entidad a disposición
a través del operador “.”

Volviendo al ejemplo planteado al comienzo de la capacitación, para corroborar si un cliente es mayorista,
escribimos desde la factura, la expresión Cliente.Tipo = “Mayorista”

Ahora, imaginemos que estamos creando una expresión con contexto en la colección Descuentos de los
Ítems de Factura. Entonces, tenemos la entidad Factura con una colección de ítems, y para cada uno de
estos, una colección de descuentos. A esta segunda colección podemos llamarla subordinada o de
segundo nivel. En caso de que, desde la colección de Descuentos, quisiéramos acceder al número del
comprobante, esto sería imposible, ya que no se encuentra en el mismo contexto.

Sin embargo, si escribimos “ **Esta instancia.** ”, haremos referencia a la instancia completa, es decir, a la
Factura actual. Desde aquí, por ejemplo, podemos acceder al Total, al Cliente y a los Ítems, puesto que el
nuevo contexto pasa a ser la entidad Factura. Es decir, las expresiones Esta instancia.Total, Esta
instancia.Ítems y Esta instancia.Cliente serán válidas.

¿Cuál es el significado de “Esta instancia”? Se trata de un atributo de sistema, elaborado por FastPrg, cada
vez que se crea una entidad o colección. Esto quiere decir que dentro de la colección Ítems existe Esta
instancia, como así también se halla en la colección Descuentos, y en la cabecera. ¿Para qué sirve,


particularmente? ¿Qué utilidad tiene? Este atributo de sistema hace referencia a la instancia completa.
**Nos permite movernos a la cabecera de la instancia** cuando estamos posicionados en una colección.

Por ejemplo, si quisiéramos conocer la cantidad de productos pertenecientes al rubro repuestos que se
han vendido, podríamos hacerlo con la siguiente expresión:

```
EN Factura.Ítems CONTAR Producto CUANDO Producto.Rubro = ‘Repuestos’
```
En caso de que además precisemos el número de productos de este rubro, que compró determinado
cliente, deberíamos escribir:

```
EN Factura.Ítems CONTAR Producto CUANDO Producto.Rubro = ‘Repuestos’ y Esta
Instancia.Cliente = ‘Logística Integral’
```
Es muy importante dejar en claro que sin el atributo Esta instancia nunca podríamos acceder al cliente, ya
que nuestro contexto actual son los ítems de la factura y el cliente se encuentra en la cabecera.

Supongamos ahora que seguimos posicionados en la colección de Descuentos de nuestra Factura. Nuestro
contexto es ese. Si escribimos “ **Este ítem.”,** haremos referencia al ítem completo del descuento. En este
caso, el contexto no cambia, aunque veremos más adelante ejemplos de usos donde sí es relevante el
atributo Este ítem.

Si escribimos “ **Ítem padre.** ”, nuestro contexto pasa a ser la colección de Ítems, aunque no completa, solo
el ítem que es padre del ítem actual. Es decir, en nuestro ejemplo, estaríamos accediendo al ítem que
tiene como producto “Carpeta”. Entonces, por ejemplo, la expresión Ítem padre.Subtotal nos retornaría
$658.

Cabe destacar que el operador “.” no modifica el contexto de toda la expresión, **sino el contexto del
operando actual**. Por ejemplo, con la siguiente expresión podemos conocer cuántos repuestos fueron
facturados para los clientes de Argentina:

EN Factura.Ítems CONTAR Producto CUANDO Esta instancia.Cliente.País = “Argentina” y Producto.Rubro
= “Repuestos”

Tal como observamos, nos adentramos en el contexto de cliente. Sin embargo, luego de especificar el país
que es de nuestro interés, tuvimos la posibilidad de escribir Producto.Rubro dado que nuestro contexto
nunca cambió. Conviene recordar que siempre podemos navegar con el operador “.”, ya sea dentro de la
misma instancia con estos atributos de sistema, o entre atributos de tipo referencia, compuestos o
colecciones. La única excepción la constituyen los atributos de un acumulador, en cuyo caso podemos
navegar por sus dimensiones, pero no por sus atributos.

Veamos ahora gráficamente a qué podemos acceder posicionados en cada contexto de una entidad de
ejemplo: Factura venta y cómo hacerlo.


#### 1) DESDE UN ATRIBUTO DE CABECERA

por ejemplo: Número, Fecha, Cliente, Moneda, Total

Puedo hacer referencia a la instancia completa con "Esta instancia".

Puedo hacer referencia al valor de cualquier otro atributo de cabecera simplemente por su nombre.
Por ejemplo "Cliente".

**NO** puedo hacer referencia directa al valor de ningún atributo de ninguna colección (en este ejemplo:
“Items de la factura”, “Descuentos del ítem” ni “Descuentos del comprobante”).

Puedo hacer búsquedas (en... primer, en...sumar, etc) sobre cualquier colección:

en .Items de la factura CONTAR ...

en .Items de la factura.Descuentos del ítem SUMAR ... (recorre todos los descuentos de todos los ítems)

en .Descuentos del comprobante PRIMER ...

#### 2) DESDE UN ATRIBUTO DE UNA COLECCIÓN DE PRIMER NIVEL

Por ejemplo: Producto, Precio, Cantidad, Total de la colección Ítems de la factura

Puedo hacer referencia a la instancia completa con "Esta instancia".


Puedo hacer referencia al valor de cualquier atributo de cabecera con "Esta
instancia.NombreDelAtributo". Por ejemplo “Esta instancia.Cliente”.

Puedo hacer referencia al ítem completo con “Este ítem”.

Puedo hacer referencia al valor de cualquier otro atributo de la misma colección, simplemente por su
nombre. Por ejemplo ”Producto”.

**NO** puedo hacer referencia directa al valor de ningún atributo de la colección contenida (en este
ejemplo, “Descuentos del ítem”).

**NO** puedo hacer referencia directa al valor de ningún atributo de otra colección (en este ejemplo,
“Descuentos del comprobante”).

Puedo hacer búsquedas (en... primer, en...sumar, etc) sobre cualquier colección:

en .Esta instancia.Items de la factura CONTAR ... (recorre todos los ítems de la factura)

en .Esta instancia.Items de la factura.Descuentos del ítem SUMAR ... (recorre todos los descuentos de
todos los ítems)

en .Descuentos del ítem SUMAR ... (recorre los descuentos del ítem actual)

en .Esta instancia.Descuentos del comprobante PRIMER ...

#### 3) DESDE UN ATRIBUTO DE UNA COLECCIÓN DE SEGUNDO NIVEL

por ejemplo: Descripción, Porcentaje, Importe de la colección Descuentos del ítem (aplica el mismo
criterio para otras colecciones de otros niveles)

Puedo hacer referencia a la instancia completa con "Esta instancia".

Puedo hacer referencia al valor de cualquier atributo de cabecera con "Esta
instancia.NombreDelAtributo". Por ejemplo “Esta instancia.Cliente”.

Puedo hacer referencia al ítem completo que la contiene con “ítem padre”.

Puedo hacer referencia al valor de cualquier atributo del ítem que la contiene con “ítem
padre.NombreDelAtributo”. Por ejemplo “ítem padre.Producto”.

Puedo hacer referencia al valor de cualquier otro atributo de la misma colección, simplemente por su
nombre. Por ejemplo “Porcentaje”.

**NO** puedo hacer referencia directa al valor de ningún atributo de otra colección (en este ejemplo,
“Descuentos del comprobante”).

Puedo hacer búsquedas (en... primer, en...sumar, etc) sobre cualquier colección:

en .Esta instancia.Items de la factura CONTAR ...


en .Esta instancia.Items de la factura.Descuentos del ítem SUMAR ... (recorre todos los descuentos de
todos los ítems)

en .ítem padre.Descuentos del ítem SUMAR ... (recorre todos los descuentos del ítem actual)

en .Esta instancia.Descuentos del comprobante PRIMER ...

#### 4) DESDE UN ATRIBUTO DE UNA ENTIDAD ACCEDER A ATRIBUTOS DE OTRAS ENTIDADES REFERENCIADAS

Se van a mostrar ejemplos desde la cabecera, pero aplica el mismo criterio, desde atributos de
colecciones.

En este caso, el atributo “ **Cliente** ” de esta entidad “ **Factura** ” es de tipo referencia. Por lo cual usando
“Cliente.” Podemos acceder a cualquier atributo de la entidad referenciada “ **Cliente** ”

Puedo hacer referencia directa a un atributo de cabecera de una entidad referenciada. Por ejemplo
“Cliente.nombre” o “Cliente.Email”

Puedo hacer referencia directa a un atributo de cabecera de una entidad referenciada a la entidad
referenciada. Por ejemplo “Cliente.Cuenta de Venta.Nombre”. En este caso, el atributo “ **Cuenta de
venta** ” de la entidad “ **Cliente** ” es una referencia a la entidad “ **Cuenta Contable** ”.

Puedo hacer búsquedas (en... primer, en...sumar, etc) sobre cualquier colección de la entidad
referenciada:

En Cliente.Domicilios PRIMER ... (recorre todos los domicilios del cliente de la factura actual)

En Clientes.Contactos.Teléfonos BUSCAR ... (recorre todos los teléfonos de todos los contactos del
cliente de la factura actual)

El mismo criterio se aplica sobre Atributos de tipo referencia a Colección.

### 2.3 Contexto global

Vimos los contextos de acumulador, colección y entidad. Ahora veamos el **contexto global**. Es el contexto
que siempre está presente. ¿Qué significa esto? Que en cualquier elemento donde se pueda ingresar una
Expresión, es posible moverse al contexto global a través de alguna operación de búsqueda, por ejemplo:
EN... BUSCAR o EN... PRIMER.

De esta manera, es posible moverse al contexto de cualquier Entidad, Colección o Acumulador, gracias al
contexto Global donde se encuentran todos ellos.

Este contexto global puede tener alguna relación con el contexto inicial donde nos encontramos o no. Por
ejemplo, en el caso de ir a buscar el nombre del cliente de una factura, empezamos en el contexto de la
factura y pasamos al contexto del cliente de esa factura.

Sin embargo, en otra situación, podríamos desde la factura ir a buscar la cotización del dólar a la entidad
Cotizaciones, y no estar relacionado en nada con la factura que se está emitiendo.

En Cotizaciones ÚLTIMO cotización CUANDO Moneda = “USD”


De esta manera, obtenemos la cotización del dólar sin tener que relacionarlo con nada de la factura.

### 2.4 Contexto anterior, operador SUPER

Imaginemos el siguiente escenario: estamos posicionados en el ítem de una factura y queremos insertar
el precio declarado en la lista de precios. Una opción para modelar esto, y la que utilizaremos ahora,
consiste en tener una entidad Lista de precios donde cada una de sus instancias sea el producto y su
precio. Una operación muy sencilla. Pero como nos situamos en la colección de los ítems de factura,
nuestro contexto es esta colección. Ahora bien, de entre todos los ítems de las listas de precios existentes,
necesitamos obtener el valor cuyo producto sea igual a aquel sobre el cual estamos posicionados en este
momento. Entonces, podemos escribir

```
EN Lista de precios PRIMER Precio CUANDO Producto = ___?
```
En este punto es válido preguntarnos ¿a qué es igual el producto? Sabemos que al producto sobre el cual
estamos posicionados, sin embargo ¿cómo podemos expresar esto? Ya que con la frase EN Lista de precios
nos movimos al contexto de la entidad Lista de precios. En cambio, el dato que necesitamos utilizar en la
condición para la comparación -a saber, el producto de la factura- se encuentra en el contexto anterior,
en los ítems de este tipo de comprobantes. Como una posible respuesta a esta situación, FastPrg cuenta
con el operador **SUPER** , el cual nos permite volver al contexto anterior, o mejor dicho superior, de aquí
su nombre.
Para el ejemplo que planteamos, basta con escribir SUPER.Producto. A través de este operador
regresamos a los ítems de la factura, esto es, el contexto anterior a la lista de precios; dicho de otro modo,
el contexto inicial de la expresión. Allí, obtendremos el producto sobre el cual nos posicionamos al
comenzar a escribirla. La expresión nos queda de la siguiente manera:

```
EN Lista de precios PRIMER Precio CUANDO Producto = SUPER.Producto
```
En lo que sigue, analizaremos el contexto en cada sección de la expresión, a los fines de poder enfatizar
este nuevo concepto, que puede resultar complejo. Antes de empezar a escribir, nuestro contexto era
donde estábamos posicionados, es decir, los _ítems de la factura_.

Al tipear “EN Lista de precios”, tal como hemos visto, nos movimos a ese contexto.


Luego, “PRIMER Precio” no lo altera y “CUANDO Producto =” tampoco, es decir, hasta esta parte, siempre
nuestro contexto es el que elegimos para la expresión, es decir, la lista de precios.

Seguidamente, a través del operador ”SUPER.” nuestro contexto vuelve a ser el de los ítems de la factura.
Aquí podríamos escribir Precio, Subtotal, Cantidad o Producto; cualquiera de los atributos propios de esta
colección. Sin embargo, para este ejemplo nos interesa conocer el producto.

Entonces, esta expresión recorrerá la lista de precios y nos traerá el primer elemento al que esté asociado
el producto igual al del ítem, donde nos posicionamos al escribirla. En otras palabras, nos devolverá, por
ejemplo, el precio de las bujías cuando facturemos bujías, o el de los neumáticos cuando facturemos
neumáticos.

Veamos en detalle otra situación: estamos posicionados en un cliente y queremos saber el importe total
de sus facturas. Para ello, debemos escribir

```
EN Factura SUMAR Total CUANDO Cliente.Nombre = Super.Nombre
```

En este caso, como nos situamos sobre el cliente, podemos acceder al nombre sin problemas. Entonces,
al escribir Super. no tenemos que cambiar de contexto ni hacer nada para obtener el nombre. Otra forma
de escribir esto puede ser

```
EN Factura SUMAR Total CUANDO Cliente = Super.Esta instancia
```
La diferencia aquí radica en que no estamos consultando clientes que tengan el mismo nombre. En el
ejemplo anterior, buscábamos que coincida el nombre del cliente de la factura con el nombre del cliente
donde estábamos calculando la suma. En contraste, en este caso nos interesa que sea el mismo cliente.
Estamos comparando la instancia completa. Si tuviésemos dos clientes con el mismo nombre, en el caso
anterior donde comparábamos justamente sus nombres, estaríamos sumando lo facturado por ambos
clientes. Sería más conveniente, en este caso, utilizar la segunda expresión.
Veamos ahora los contextos: El contexto inicial es la entidad Cliente

Al escribir en la expresión En Factura, nos movemos al contexto de la entidad Factura

Luego, al escribir SUPER. nuestro contexto vuelve a ser la entidad Cliente


Supongamos, ahora, que necesitamos saber desde qué fecha le estamos facturando a un cliente. Para
ello, podemos extraer en estos comprobantes, la fecha que coincida con la primera factura del cliente:

```
EN Factura PRIMER Fecha CUANDO Cliente = Super.Esta instancia
```
Los ejemplos son muy parecidos. Aquí aplica la misma distinción; estamos igualando instancias, no los
nombres de clientes.

También, podemos observar que, si estamos posicionados en Factura, raramente utilicemos EN Cliente
PRIMER, o EN Cliente CONTAR, ya que desde este comprobante podemos acceder al cliente, de manera
directa, con ” Cliente.”.

De todos modos, si queremos obtener, en cada factura, el número de clientes que tienen la misma ciudad
que el cliente de la factura, podemos escribir

```
EN Cliente CONTAR Nombre CUANDO Ciudad = Super.Cliente.Ciudad
```
¿Qué sucede si en lugar de contar los clientes, queremos saber sus nombres? En ese caso solo debemos
cambiar la operación CONTAR por BUSCAR. En efecto, esta expresión nos trae todos los nombres de los
clientes que posean la misma ciudad que el cliente de nuestra factura.

Hasta aquí, hemos indicado cómo obtener datos con nuestras expresiones. Operaciones bastante
complejas, que incluyen búsquedas en instancias de otras entidades, sumas, conteos. Aun así, existe un
caso particular, que especificaremos a continuación.

Para ello, veamos la siguiente situación. Estamos posicionados en el atributo Total de la factura, que -
supongamos un caso muy simple- es la suma de los subtotales de los ítems. A este total queremos
asignarle un valor. Es decir, debemos recorrer los ítems de la factura y sumar sus subtotales. ¿Cómo


podemos efectuar esto? ¿Podemos escribir EN Factura.Ítems SUMAR Subtotal? Nos traería los subtotales
de todos los ítems de cada una de las facturas.
¿Y la siguiente opción es conveniente? EN Factura.Ítems SUMAR Subtotal cuando Esta instancia =
super.Esta instancia
Aquí, estamos recorriendo todas las facturas y sumando los subtotales de la factura actual, utilizando Esta
instancia y el operador super. Sin embargo, esto no es posible ya que las búsquedas se realizan con los
datos persistidos, y la factura no lo está aún, sino que se está creando en este momento. Para este caso
particular, en FastPrg se implementa un uso más del operador “.”, a través del cual no solo podemos
movernos entre contextos, sino también buscar en instancias no confirmadas todavía.

¿Cómo utilizamos este operador? Debe preceder al contexto actual. De esta manera, le indica a FastPrg
que recorreremos una colección en memoria. Por ejemplo, en este caso podríamos escribir

```
EN .Ítems SUMAR Subtotal.
```
Así, estamos recorriendo la colección de ítems actual, la de esta factura que estamos creando.

Supongamos, ahora, que queremos realizar una validación dentro de los ítems de factura para no comprar
productos repetidos. Podemos hacerlo posicionándonos sobre cada artículo y contar cuántos productos
son iguales a estos en la factura: el resultado en cada caso debería ser uno.

Esta expresión, ahora, podemos escribirla, posicionados en el producto:

```
EN. Esta instancia.Ítems CONTAR Producto CUANDO Producto = super.Producto
```
Nos devolverá la cantidad de ítems iguales al producto actual, para cada producto de la factura. Ahora
solo nos resta igualarlo a uno.

```
(EN .Esta instancia.Ítems CONTAR Producto CUANDO Producto = super.Producto) = 1
```
Vale recordar que siempre debemos escribir una colección luego del operador “.” cuando lo utilizamos de
esta manera. En este caso, Ítems o Esta instancia.Ítems son colecciones.

De esta misma manera, es posible utilizar **super** en otros lugares donde usamos expresiones. Veamos
algunos ejemplos:

- En una función, si utilizamos un en...buscar o en...contar, podemos utilizar Super para referenciar
    a los parámetros de la función. Por ejemplo, en una condición de la función utilizamos la siguiente
    expresión:
    esnulo((en Publicación por Comercio electrónico.Variaciones de la publicación primer Este ítem
    cuando Esta instancia = super.Publicación))
    al posicionarnos con En... primer en **Publicación por Comercio electrónico.Variaciones de la**
    **publicación** cuando utilizamos super.Publicación nos referimos al parámetro de entrada de la
    función
- En una RN que asigna una especialidad a las tareas de mantenimiento, para realizar la asignación
    de valor al modificar ítem, se usa la siguiente expresión:
    en Tarea de mantenimiento primer Especialidad de mantenimiento cuando Esta instancia =
    super.Tarea
    De esta manera, super.Tarea refiere a la tarea por la que se activó la Regla de Negocios

Así, podríamos seguir dando ejemplos de Super para Transformaciones, Desencadenantes, Reporte por
bandas, Filtro de modelo, Planificación, etc. Debe tenerse en cuenta que siempre que necesitemos volver
a un contexto anterior debemos utilizar la palabra reservada Super.

### 2.5 Expresiones sin contextos (unbound expression)

En ciertas situaciones, es necesario definir expresiones donde aún no está definido el contexto donde se
va a aplicar. En estos casos, no se realizan las validaciones que aplican al contexto, sí a la sintaxis de la
expresión.


Algunos ejemplos de estas expresiones son:

- **Tipos de Atributo** : Para el caso de las expresiones dentro de un Tipo de Atributo, desde el
    Editor de Tipos de Atributo no se puede determinar el contexto del mismo, ya que el
    contexto recién se definirá cuando se lo utilice dentro de un Atributo de una Entidad. Por lo
    que en estos casos se podrá ingresar dentro de la expresión cualquier entidad o atributo de
    las mismas. Pero cuando desde el Editor de Entidades, se utilice el Tipo de Atributo dentro
    de la definición de un Atributo, se evalúa la expresión dentro del contexto de la Entidad a la
    que pertenece el Atributo y se presentan los errores que correspondan. Por ejemplo, si en
    Valor Inicial del Tipo de Atributo de atributo “IVA” se ingresa la expresión “Cliente.IVA” será
    válida para el Tipo. Pero si luego dentro de la Entidad Factura se define un Atributo cuyo Tipo
    sea “IVA” se deberá validar que desde la Entidad Factura exista un atributo llamado Cliente,
    y en caso contrario se presenta un error en la expresión del valor inicial del Atributo.
    Otro ejemplo es el caso en que se tiene un Tipo de Atributo Enumerado y se establece una
    condición de visibilidad para algún valor del mismo. Luego, en la entidad donde se utiliza el
    enumerado, es posible que no se pueda evaluar esa condición de visibilidad porque no se
    encuentre el atributo, en este caso no muestra error, se considera verdadera la condición.

### 2.6 Operaciones de búsqueda

#### 2.6.1 Estructura

```
Para comenzar a entender la sintaxis de las expresiones, imaginemos un caso particular:
necesitamos conocer todos los nombres de los clientes argentinos de nuestra cartera, ordenados
por su CUIT de menor a mayor. A los fines de cumplir este objetivo, en FastPrg podemos escribir:
```
```
EN Cliente BUSCAR Nombre CUANDO Obtener traducción(País.Nombre;'es') = 'Argentina'
ORDENAR CUIT asc
```
```
En primer lugar, la palabra reservada EN seguida de Cliente. Esta parte es la que nos indica el
nuevo contexto en el que evaluaremos la expresión. Recordemos que ya tenía un contexto y nos
estamos moviendo hacia otro que, en este caso, es la entidad Cliente.
Vemos, luego, la palabra BUSCAR, la cual constituye nuestra operación y señala que nos traerá
todo lo que encuentre, pero ¿qué es lo que buscará exactamente? La respuesta es Nombres.
¿Cuáles? Los del nuevo contexto, es decir, los nombres de los clientes.
Ahora, necesitamos saber si queremos todos los nombres de los clientes o solo algunos en
particular. Como en nuestro ejemplo nos interesan los de clientes argentinos, entonces,
podemos filtrarlo con una condición: Obtener traducción(País.Nombre;'es') es igual a 'Argentina'.
Es importante aclarar que la palabra reservada CUANDO implica un filtro y es opcional. En caso
de no querer usarlo, lo omitiremos. Por ejemplo, podemos establecer
EN Cliente BUSCAR Nombre
y, en efecto, obtendremos todos los nombres de todos los clientes.
A CUANDO le sigue una condición , la cual filtrará todas las instancias que cumplan con ésta y
debe retornar un tipo de dato lógico, ya sea verdadero o falso, cuyo contexto será aquel al que
ya nos dirigimos, es decir, Cliente. Se buscará, por lo tanto, el nombre del País del cliente.
Ya tenemos todos los datos que nos traerá FastPrg, ahora, nos queda ver cómo realizará esta
operación. En la situación planteada, necesitábamos ordenarlos por CUIT, de menor a mayor.
Para ello, podemos escribir, luego de la condición, la palabra reservada ORDENAR seguida del
atributo por el que deseemos efectuar esta disposición. En este caso, es el CUIT y de forma
ascendente.
En conclusión, podemos afirmar que esta expresión ingresará a todos los clientes, buscará los
nombres de los que sean argentinos y los ordenará de manera ascendente, por cuit.
```
```
Es importante aclarar que estas operaciones también pueden escribirse en modo función y, al
confirmar, el analizador de impacto las traduce al formato Operaciones de búsqueda. Por
ejemplo:
```

```
Buscar(Factura; Importe total > 100 Y Cliente.Nombre CONTIENE “Pedro” Y
Cliente.Limite de crédito > 100 )
En Factura Buscar Esta instancia Cuando Importe total > 100 Y Cliente.Nombre
CONTIENE “Pedro” Y Cliente.Limite de crédito > 100
```
#### 2.6.2 Tipos de operaciones

```
La sintaxis de las expresiones es la siguiente:
```
EN <contexto> <operación> <elemento> (CUANDO) <filtro> (ORDENAR) <elemento orden>

```
En el caso planteado, vimos una: BUSCAR , que retorna siempre una colección. Incluso si hay un
solo elemento que cumpla la restricción, la devolverá con ese único. Como buscamos los
nombres de los clientes argentinos, esa expresión nos trae una colección de nombres.
La siguiente operación es PRIMER , a través de la cual podemos obtener un elemento. Así como
BUSCAR siempre retorna una colección, esta operación siempre devuelve un único elemento (o
ninguno, en el caso de que no encuentre).
Por ejemplo, si queremos extraer el nombre del primer cliente, escribiremos “EN Cliente PRIMER
Nombre”. Ahora bien, ¿qué quiere decir esto? Se refiere al primer cliente que se dio de alta en
FastPrg. El orden, por defecto, cuando utilizamos las operaciones PRIMER, ÚLTIMO o BUSCAR
sobre instancias es aquel en que se fueron creando.
En caso de emplearlas sobre colecciones, automáticamente, si no se elige otra opción, FastPrg
seguirá el orden en el cual se visualizan los ítems.
Si quisiéramos obtener el nombre del último cliente expresaríamos “EN Cliente ÚLTIMO
Nombre”, o EN Cliente ÚLTIMO Nombre CUANDO País = “Argentina”, para traer el último cliente
argentino.
También, si requerimos una búsqueda más específica como, por ejemplo, el nombre del cliente
de la última factura creada, podemos obtenerlo mediante la expresión EN Factura ÚLTIMO
Cliente.Nombre. Vale aclarar que con el punto estamos indicando que precisamos el nombre de
ese cliente. En tal sentido, las posibilidades son infinitas.
Para conocer el total facturado en todo el sistema, escribimos EN Factura SUMAR Total. Como
podemos observar, la sintaxis es siempre la misma. Además, podríamos filtrar esta suma por los
clientes argentinos (EN Factura SUMAR Total CUANDO Cliente.País = ‘Argentina’) o sumar el total
facturado con comprobantes cuyo importe sea menor a cierta cantidad, por ejemplo, mil pesos
(EN Factura SUMAR Total CUANDO Total < 1000). Y en caso de querer obtener el total facturado
por clientes argentinos con un monto inferior a mil pesos, juntamos las dos condiciones.
EN Factura SUMAR Total CUANDO Total < 1000 y Cliente.País = ‘Argentina’
```
```
Ahora, podemos preguntarnos ¿cuántas facturas suman este número? Para resolver esto no es
necesario nada más que cambiar la operación SUMAR por CONTAR
EN Factura CONTAR Total CUANDO Total < 1000 y Cliente.País = ‘Argentina’
```
```
Es importante destacar que si no existiese ninguna factura que cumpla con estas condiciones, es
decir, hecha a nombre de clientes argentinos y con un monto menor a mil pesos, por defecto,
ambas operaciones retornan cero. Asimismo, solo operan sobre atributos completos, es decir, si
tenemos trescientas facturas pero hay diez que no poseen monto total, la operación CONTAR
devolverá docientas noventa, ya que estamos contando los totales.
```
```
Además, podemos realizar un promedio, dividiendo la suma por la cantidad.
(EN Factura SUMAR Total CUANDO Total < 1000 y Cliente.País = ‘Argentina’) / (EN Factura
CONTAR Total CUANDO Total < 1000 y Cliente.País = ‘Argentina’)
```
```
De todos modos, FastPrg cuenta con una operación especial para simplificar esto.
EN Factura PROMEDIO Total CUANDO Total < 1000 y Cliente.País = ‘Argentina’
```
```
Si quisiéramos obtener el menor monto facturado, ¿qué deberíamos hacer? Podríamos escribir,
por ejemplo, EN Factura PRIMER Total ORDENAR Total ASC. Esto dispondría de manera
```

```
ascendente los totales de las facturas y nos traería el primero. Sin embargo, FastPrg ofrece un
atajo para este tipo de cálculos: la operación MÍNIMO. Sencillamente, debemos escribir EN
Factura MÍNIMO Total.
Así como existe mínimo, contamos con la operación MÁXIMO que hace lo mismo, pero a la
inversa. Para obtener, entonces, el mayor monto de una factura, formularemos la siguiente
expresión: EN Factura MÁXIMO Total.
```
```
Operaciones disponibles en FastPrg: BUSCAR, PRIMER, ÚLTIMO, SUMAR, CONTAR, PROMEDIO,
MÍNIMO y MÁXIMO.
```
```
Tener en cuenta que, sin dar una instrucción específica, las operaciones se realizan considerando
las instancias persistidas y, además, las instancias que se encuentran en edición dentro de la
conversación actual en la que se encuentra trabajando el usuario. En ningún caso se tienen en
cuenta las que están en edición para otras instancias, excepto que se aclare el almacén
correspondiente. El ordenamiento de ítems de colección (e instancias) en memoria se realiza por
el atributo order que está en las colecciones, que es el que se usa para ordenar en la grilla en
forma predeterminada.
```
#### 2.6.3 Agregar y Eliminar elementos

```
Se podrán adicionar elementos a una colección mediante el operador “+”; de la misma forma, se
podrán eliminar con el operador “–” o con el método eliminar(<índice>). En el caso de la
eliminaciones con el operador “–”, se eliminarán de la colección todas las ocurrencias del
operando que está a la derecha del operador.
Colección1 + Colección2 + [“roca”;1626] ; [“Montevideo”;100]
Colección1 – [“roca”;1626]
```
#### 2.6.4 Ejecutar expresión sobre cada elemento de la lista

```
Dada una operación aritmética cuyos operandos son de categoría simple, si la misma recibe una
colección de elementos, se aplicará la operación sobre cada uno de dichos elementos. Para el
ejemplo presentado a continuación, el resultado será una colección donde cada uno de sus
elementos será un elemento de Colección1 multiplicado por 5.
Colección1.atributo * 5
```
#### 2.6.5 Limitar a

La palabra reservada **"Limitar a"** permite al usuario especificar la cantidad de instancias que el
sistema devuelve en las expresiones que contienen "Buscar" o "Buscar aleatorio".

Sintaxis:
en <Entidad> o <Colección> Buscar/Buscar aleatorio <Atributo> **Limitar a** <Número entero>
Donde:

- "Limitar a" es la palabra reservada que indica que se quiere limitar la cantidad de instancias que
devuelve fastprg.
- <Número entero> es un número entero que indica la cantidad de instancias que se desean
obtener.
Comportamientos:
- En las expresiones que contengan un "Buscar" y no especifiquen el límite de instancias a traer,
fastprg devolverá todas las instancias.
- Al especificar un límite en la expresión, fastprg devuelve la cantidad de instancias especificadas
por el usuario.
- Si el límite especificado es mayor que la cantidad de instancias persistidas en la base de datos,
fastprg devuelve todas las instancias.


- Al utilizar la palabra reservada "Limitar a" siempre se debe indicar la cantidad de instancias a
retornar, en el caso de que el usuario no lo indique, se debe dar un mensaje de error de sintaxis
indicando que debe ingresar la cantidad de instancias.

```
Ejemplos :
En Cliente Buscar aleatorio Teléfono
El sistema mostrara en el panel de mensajes un error de sintaxis en la expresión, ya que
```
```
En Cliente Buscar Teléfono limitar a 5
Devuelve cinco instancias del atributo "Teléfono" de la entidad "Cliente".
```
```
Suponiendo que existen 50 instancias persistidas de la entidad "Cliente":
En Cliente Buscar Teléfono limitar a 51
Como la cantidad de instancias persistidas del atributo "Teléfono" en la entidad "Cliente" es
menor que 51, el sistema devuelve todas las instancias.
```
#### 2.6.6 Buscar aleatorio

El operador de sistema "Buscar aleatorio" permite al usuario buscar instancias aleatorias de un
atributo persistido en la base de datos.

Sintaxis:
en <Entidad>o<Colección> **Buscar aleatorio** <Atributo> **Limitar a** <cantidad de elementos>
Donde:

- Buscar aleatorio es el operador que indica que se quiere buscar instancias aleatorias.
- Limitar a es una palabra reservada que indica que se quiere limitar la cantidad de instancias
aleatorias que se devuelven.
- <cantidad de elementos> es un número entero que indica la cantidad máxima de instancias
aleatorias que se desean obtener.
Comportamientos:
    - Al usar buscar aleatorio, siempre se debe especificar el límite. Si se intenta utilizar sin la
       palabra reservada Limitar a, saltara en el panel de mensajes error de sintaxis en la
       expresión.
    - Si se especifica un límite, el sistema devuelve esa cantidad de instancias aleatorias del
       atributo especificado.
    - Si el límite especificado es mayor que la cantidad de instancias persistidas en la base de
       datos, el sistema devuelve todas las instancias de forma aleatoria.
    - Las instancias devueltas son seleccionadas de manera aleatoria de entre las instancias
       persistidas en la base de datos del atributo especificado.

**Ejemplos** :
En Cliente **Buscar aleatorio** Teléfono
El sistema mostrara en el panel de mensajes un error de sintaxis, ya que la expresión para ser
válida, necesita la palabra reservada **Limitar a**.

En Cliente **Buscar aleatorio** Teléfono **limitar a 5**.
Devuelve cinco instancias aleatorias del atributo "Teléfono" de la entidad "Cliente".

Suponiendo que existen 50 instancias persistidas de la entidad "Cliente":
En **Cliente Buscar** aleatorio Teléfono **limite 51**
Como la cantidad de instancias persistidas del atributo "Teléfono" en la entidad "Cliente" es
menor que 51, el sistema devuelve todas las instancias de forma aleatoria.

#### 2.6.7 Buscar en almacén explícito

En las expresiones utilizadas, opcionalmente podremos indicar el almacén desde el cual
deseamos obtener la información. Los almacenes a los que se permite acceder son:


```
Almacén Contenido
Definitivo Contiene el historial de instancias que ya se encuentran confirmadas
Edición Contiene información acerca de instancias que se encuentran en
edición
Edición Cancelado Contiene información acerca de instancias que se encontraron en
edición pero que luego fueron descartadas.
Consolidado Contiene solo información de la última versión creada de una instancia.
Consolidado
borrado
```
```
Contiene información de aquellas instancias que se encontraban
dentro del almacén consolidado, pero luego fueron borradas.
Consolidado todo Contiene toda la información tanto del almacén consolidado como del
almacén consolidado borrado.
```
```
Dependiendo del tipo de entidad sobre el cual se aplica, se podrá tener acceso a diferentes
almacenes de datos.
```
- **Entidades maestras**. En este tipo de entidades se podrá consultar sobre cualquiera de
    los almacenes mencionados anteriormente. En caso de no indicar el almacén, se aplicará
    por defecto la expresión sobre el almacén ‘Consolidado’.
- **Entidades transaccionales**. En este tipo de entidades se podrá consultar solo a los
    almacenes ‘Definitivo’, ‘Edición’, ‘Edición Cancelado’. En caso de no indicar el almacén,
    se aplicará por defecto la expresión sobre el almacén ‘Definitivo’.

```
Buscar(Cliente; ; teléfono COMIENZA CON “5”; Definitivo )
En Cliente Buscar Cuando teléfono COMIENZA CON “5” Desde almacen
Definitivo
```
Consideraciones al es pecificar un al macén de datos.

```
Al crear una expresión, en caso de ser una entidad de tipo Transaccional sobre la cual se desea
indicar el almacén de datos, deberemos evaluar que no se intenten utilizar los almacenes
‘Consolidado’, ’Consolidado Borrado’, ’Consolidado todo’ (en este caso no es posible utilizar
Desde Consolidado, Consolidado borrado, Consolidado Todo). En caso de intentar utilizarlos, el
sistema deberá informar la situación y solicitando la modificación de la expresión para poder
continuar.
Existe la posibilidad de luego cambiar el tipo de entidad y en este caso el sistema realiza
determinadas validaciones.
```
### 2.7 Operadores y operandos

Como vimos, una expresión tiene distintos tipos de elementos que la componen. Uno de estos elementos
son los **operadores** , que permiten realizar operaciones con uno o más **operandos**. Y es importante
considerar el orden de resolución de los mismos. Veremos en detalle estos temas:

#### 2.7.1 Tipos de operadores

```
Existen distintos tipos de operadores; tenemos los operadores aritméticos (los podemos usar
por ejemplo para asignar un valor inicial a un atributo numérico), tales como:
Operador Significado Ejemplo
+ Suma 5 + 6
```
**-** Resta 4 _–_ 2
***** Multiplicación 2 _*_ 3
**/** División 5 _/_ 2
**%** Porcentaje 21 _%_


```
^ Potenciación 9 ^ 3
```
```
Resaltamos que los operadores +,- podemos utilizarlos para sumar o restar números, fechas y
duraciones. Por ejemplo, podemos sumarle a la fecha de una factura 30 días y así calcular un
vencimiento.
Operador Significado Ejemplo
+ Suma {10/10/2012} + {5 días}
```
**-** Resta {10/10/2012} - {5 días}
    {10/10/2012} - {5/10/2012}

```
También el operador + se puede usar para concatenar textos, combinando varias cadenas en una
sola.
Operador Significado Ejemplo
+ Concatena dos valores de texto para generar un
valor de texto continuo.
```
```
“Neural” + “Soft”
```
```
Otro tipo de operadores son los de comparación (muy utilizados en las validaciones). Entre estos
tenemos <, >, =, >=, <>, <=. Estos operadores utilizan 2 operandos del mismo tipo y retornan un
valor lógico: verdadero o falso. Podemos utilizarlos entre números y fechas. Por ejemplo
Total>100 o Fecha<{25/12/2000}
Operador Significado Ejemplo
= Igual a Remito.Importe = Factura.Importe
> Mayor que Remito.Importe > Factura.Importe
< Menor que Remito.Importe < Factura.Importe
>= Mayor o igual que Remito.Importe >= Factura.Importe
<= Menor o igual que Remito.Importe <= Factura.Importe
<> Distinto de Remito.Importe <> Factura.Importe
```
```
Y, por último, tenemos los operadores lógicos , como O o Y , que toman dos valores lógicos y
retornan otro lógico. Si deseamos aplicar un descuento para las facturas del mes de marzo del
año 2001, por ejemplo, podemos escribir la expresión
```
Fecha>={01/03/2001} y Fecha<={31/03/2001}

```
Operador Significado Ejemplo
Y VERDADERO si ambos Operandos son
VERDADERO
```
VERDADERO Y

VERDADERO

```
O VERDADERO si algún Operando es
VERDADERO
```
VERDADERO O FALSO

```
Retorna verdadero
EN VERDADERO si el Operando es igual a uno
dentro de la colección
```
```
“Neural” EN (“Neural”;
“Soft”)
CONTIENE VERDADERO si el Operando contiene con
una cadena
```
```
“NeuralSoft” CONTIENE
“Neural”
COMIENZA
CON
```
```
VERDADERO si el Operando comienza con
una cadena
```
```
“NeuralSoft” COMIENZA
CON “Neural”
TERMINA
CON
```
```
VERDADERO si el Operando termina con
una cadena
```
```
“NeuralSoft” TERMINA
CON “Soft”
NO Invierte el valor de otro Operando lógico NO FALSO
Retorna: VERDADERO
ENTRE VERDADERO si el Operando está dentro
de un intervalo. Se incluyen los valores
extremos como verdadero. Aplica para
números, textos y fechas.
```
10 ENTRE 1 Y 20

La evaluación de las Expresiones lógicas es mínima. Es decir, solo se evalúa un segundo
argumento en el caso de que el anterior no sea suficiente pare determinar el resultado. Por


ejemplo, en una expresión en la que se deben cumplir dos condiciones separadas por el operador
“Y”, en el caso de que no se cumpla el primero no se evalúa el resto de la operación.

#### 2.7.2 Tipos de operandos

Los operandos son los elementos que tienen valor dentro de una expresión. Pero no todos los
operandos son iguales: dentro de los operandos también podemos distinguir distintos tipos.
Un **literal** es un valor que no se calcula, siempre permanece constante. Dependiendo del tipo de
dato, existen distintos literales.
Por ejemplo, en un tipo de dato lógico tenemos dos posibles literales: verdadero y falso. Ahora,
si el tipo de dato es más complejo, como un numérico, cualquier número que escribamos puede
ser un literal. Un 5 es un literal, un -5, 200, 208, 208.75
Si nuestro tipo de dato es un texto, cualquier palabra o carácter puede ser un literal: “Hola”,
“Sebastian”, “Hola, mi nombre es: Sebastian”, son todos literales de tipo texto. Se podrán
delimitar en forma indistinta con comillas simples o dobles para permitir la inclusión en la cadena
del tipo de comillas que se desee.

```
Cuando el tipo de atributo es enumerado, un literal va a ser un posible valor de ese tipo de
atributo. Por ejemplo, si hablamos del género de una persona, “Femenino” puede ser un literal.
Si hablamos del tipo de cliente, “Mayorista” es un literal, “Minorista” otro. Y dependiendo de
cada tipo de enumerado tendremos distintos literales. Los enumerados tienen un código y una
descripción. Dentro de las expresiones, usamos el código de los mismos y en otras secciones del
sistema, como puede ser un filtro rápido, usamos la descripción. Supongamos que tenemos un
enumerado de tipo de documento donde el código es “DNI” y la descripción es “Documento
nacional de identidad”. Si necesitamos aplicarlo en una expresión, mencionaremos tipo de
documento = “DNI”, en cambio, si lo usamos en un filtro rápido de una grilla, deberemos escribir
“Documento nacional de identidad” para que lo filtre.
Si el tipo de dato es Fecha, un posible literal es {31/12/1999}. Si es un dato de tipo Fecha hora,
puede ser {31/12/1999 23:59}. Para delimitar literales de Fecha Hora, se usarán llaves, y siempre
estarán en el formato medio (definido en la configuración regional para cada idioma). Para
ingresar un literal de fecha/hora con Zona Horaria, se podrá ingresar país y ciudad, ejemplo:
{10/1/2008 10:12:22 Europe/London}, la parte del país y ciudad es un texto internacionalizable
que el usuario lo puede ingresar manualmente en su idioma o desde el editor de E&F mediante
una lista desplegable en donde visualiza el enumerado de zonas horarias el idioma en el que se
encuentra logueado.
Asimismo, existen algunas conversiones automáticas. Por ejemplo, si el usuario ingresa {1/1/10},
esto se traduce inmediatamente a la fecha {01/01/2010} y si el usuario ingresa {1/1/98} se
traduce automáticamente a {01/01/2098}, pudiendo el usuario cambiar dicha fecha.
Cuando estamos hablando de un tipo de dato Duración, valores posibles son {5 días}, {30
minutos}. Al igual que los de fecha y fecha hora se delimitan con llaves.
```
```
Tipo Ejemplo
Booleano VERDADERO
Numérico 12,34
Texto “Hola, mundo”
Enumerado ‘monotributista’
Fechas y Duraciones {31/12/2012 12:34} {5 días} {10 meses}
{2 años} {3 horas} {192 minutos} {11550 segundos}
{10/1/2008 10:12:22 Europe/London}
```
Si nos enfocamos en los **atributos** , podemos dividirlos en Atributos de **sistema** y Atributos de
**usuario**. Para indicar la relación entre Atributos y Entidades se usa el punto (.). Para representar
un atributo que está contenido dentro de un compuesto que a su vez está dentro de una
colección, no se deberá escribir el nombre del compuesto dentro del camino. Por ejemplo, si se
tiene una colección llamada Direcciones que a su vez contiene un atributo compuesto llamado
Dirección que contiene dos simples, Calle y Número. La calle se deberá referenciar simplemente
escribiendo: Direcciones.Calle. Esto no aplica si el compuesto no está dentro de una colección.


Los **atributos de sistema** son los atributos que vienen predefinidos con las entidades, por
ejemplo, la Fecha de creación. Cada vez que se cree una instancia de una entidad, un atributo de
esa instancia es la fecha en la cual se creó la misma. Otro atributo de sistema es el Usuario
creador. De estos atributos de sistema, algunos nos sirven de auditoría como Fecha de creación
y Usuario creador, pero también hay otros como Esta instancia (que hace referencia a la instancia
completa), Este ítem (que se utiliza en colecciones y hace referencia al ítem completo), Ítem
padre (que se utiliza cuando tenemos colecciones anidadas), que nos ayudan a armar las
expresiones y a obtener los datos que necesitamos.
Los **atributos de usuario** no son más que los creados por el usuario modelador, y varían según
cada entidad. Por ejemplo, en nuestro prototipo de Cliente podemos ver que nuestros atributos
de usuario son Nombre, Ciudad, Direcciones, etc.
Tenemos un detalle de los atributos que podemos utilizar en Anexo II: Atributos.
Es posible también invocar una **función** y utilizar su resultado dentro de una expresión. Las
funciones dentro de FastPRG, así como los atributos, pueden dividirse en: **funciones de usuario**
y **funciones de sistema** (para verlas en detalle tenemos la sección Funciones y además, todas las
funciones disponibles en el sistema se encuentran en la sección de funciones, agrupadas por su
clasificación. Las mismas serán de sólo lectura y el usuario podrá moverlas a una carpeta
diferente. En el caso de que se seleccione una _Función del Sistema_ para su edición, se presentará
el mismo contenido que tienen las _Funciones de Usuario_ pero sin permitir la edición de la misma.
En el área donde van las instrucciones, se presentará un resumen con la funcionalidad provista.
Adicionalmente, los nombres de las _Funciones del Sistema_ deberán ser visualizados con una
tipografía diferente a las de las _Funciones de Usuario_.

Por ejemplo, si quisiésemos calcular el vencimiento a 30 días de un cheque de hoy, podríamos
utilizar la expresión

```
HOY() + {30 días}
```
```
Nota de arquitectura
Si en una expresión se repiten 2 o más veces la misma función o la misma operación que involucra
datos externos al contexto de la misma, la primera vez que se evalúa, se guarda el resultado en
memoria y las demás veces, se obtiene del valor guardado en memoria.
Esto puede ocurrir dentro de la misma expresión o en distintas expresiones evaluadas en la
misma instancia.
Por ejemplo, si en la entidad Factura se tienen los siguientes valores iniciales:
Vendedor de la factura = Usuario().Nombre + Usuario().Apellido
Usuario que generó instancia = Usuario().Nombre
Luego de que evalúe el primer valor inicial, siempre se devolverá el mismo nombre, aunque en
el medio de las 2 evaluaciones cambie el nombre del usuario actual.
```
```
Esto se realiza dentro de una operación de Core.
```
#### 2.7.3 Orden de resolución / Prioridad

```
El orden de resolución de las expresiones es el definido matemáticamente, esto es, de izquierda
a derecha y siguiendo el siguiente orden:
```
1. Término entre paréntesis
2. Potenciación y raíz
3. Multiplicación y división
4. Suma y resta
5. Comparación
6. Operadores lógicos
Si se combinan varios operadores en una única Expresión, se ejecutan las operaciones en el orden
indicado. Si una Expresión contiene operadores con la misma prioridad (por ejemplo, si una
Expresión contiene un operador de multiplicación y otro de división), se evalúan los operadores
de izquierda a derecha.


```
Esto significa que, si tengo escrita la siguiente expresión: 5 + 3 * 2
Se resuelve como cinco, más tres por dos, es decir, 5 + 6, ya que se resuelve antes la multiplicación
que la suma.
Si tengo la expresión 5 + (8 – 5) * 2, se resuelve primero 8-5 = 3 por estar entre paréntesis,
quedándonos
5 + 3 * 2, y ahora tenemos el mismo caso que antes.
```
```
Supongamos la expresión:
45 * 2 – 8 > 25 Y Raíz cuadrada(25) * Potencia(4;2) < 200
45*2 – 8 > 25 Y 5 * 16 < 200
90 – 8 > 25 Y 80 < 200
82 > 25 Y 80 < 200
Verdadero Y Verdadero
Verdadero
```
```
Veamos ahora cómo queda la misma expresión si modificamos agregando los paréntesis:
45 * (2 – 8) > 25 Y Raíz cuadrada(25) * Potencia(4;2) < 200
45 * (-6) > 25 Y Raíz cuadrada(25) * Potencia(4;2) < 200
45 * (-6) > 25 Y 5 * 16 < 200
(-270) > 25 Y 80 < 200
Falso y Verdadero
Falso
```
```
El simple hecho de agregar los paréntesis hizo que cambiara el resultado completamente, por eso
es sumamente importante tener en cuenta este orden de Prioridad.
```
```
Otro ejemplo a considerar es cuando tenemos varias operaciones de Y con paréntesis. Veamos el
siguiente caso: Necesito visualizar todos los clientes que sean del país Argentina y que el monto
Total de sus facturas en los últimos 6 meses sea mayor a $100mil. Para esto, podría usar un filtro
en un Gestor dinámico de información con la siguiente estructura:
```
```
Obtener traducción(Domicilio facturación.País.Nombre;’es’) = ‘Argentina’ y (en Factura sumar
Importe cuando Cliente = super.Esta instancia y Fecha > Hoy() – {6 meses}) > 100000
```
```
En este caso, en primer lugar se resuelve el paréntesis que corresponde al EN SUMAR
```
### 2.8 Uso de expresiones en diferentes elementos

```
Las expresiones pueden ser booleanas o devolver valor, entonces, ¿dónde usamos expresiones y
de qué tipo son en cada caso?
Valores iniciales devuelven valor
Valores calculados devuelven valor
Validaciones booleanas
Condiciones
o de visibilidad
o de edición
o en formatos condicionales
o de ejecución (Regla de Negocios, Desencadenantes,
Transformaciones, etc.)
o otras condiciones en configuraciones (de Acumuladores,
Secuenciadores, etc.)
```
```
booleanas
```
```
Asignación de valores en
o Transformaciones
o Desencadenantes
```
```
devuelven valor
```

```
o Reglas de negocios
o Tareas de Integración
Funciones
o Condición booleanas
o Expresión devuelven valor
Filtros
o de modelo
o en Panel de Propiedades
o en Imputaciones
o en Tareas de Integración
o otros filtros...
```
```
booleanas
```
Comenzaremos con el siguiente ejemplo: hagamos de cuenta que necesitamos impedir la emisión
de facturas cuyo monto sea menor a diez mil pesos, para clientes mayoristas. Podemos resolver
esta situación con una **validación** en el atributo “Total” de la entidad “Factura”. Para esto, nos
posicionamos sobre el total de la factura y desplegamos la solapa de validación. Luego,
completamos los atributos “nombre” y “mensaje”, y escribimos la expresión a validar.

En este caso, el contexto de la expresión es el mismo que el del atributo. Indicamos, entonces, lo
que nos interesa asegurar, es decir, que el cliente sea minorista (lo expresamos a través de No
cliente.mayorista) o, que, si es mayorista, el total de la factura no sea inferior al número
determinado, y confirmamos la entidad.

No cliente.mayorista o importe total > 10000


Podemos probarlo intentando cargar una factura con un importe menor a diez mil para un cliente
mayorista y observar que se nos impide confirmar.

En este caso vimos cómo configurar **una validación con contexto entidad**. El ejemplo que recién
analizamos consituye el caso más usual de una expresión, vale decir, aquel cuyo **contexto es el
mismo que el del atributo**.

Supongamos que necesitamos filtrar los productos de una factura; solo queremos tener la
posibilidad de seleccionar aquellos que sean Vendibles. Para realizar esta configuración, debemos
seguir estos pasos:

Comenzamos activando el atributo “Vendible” en algún artículo de la entidad “Producto”.

Ahora, nos dirigimos a la entidad “Factura”. Como podemos notar, existe, para el atributo
producto dentro de la colección de ítems, un filtro de modelo; el cual tiene, en este caso, contexto
“Producto” y permite restringir los artículos que podremos seleccionar en la factura. Siempre el
contexto es la entidad o colección a la que hacen referencia.

Escribimos, entonces, una expresión para filtrar aquellos artículos que están disponibles para la
venta:


y confirmamos la entidad. Ahora, para probarlo, intentamos cargar una factura y solo podemos
elegir aquellos ya marcados como vendibles.

En este caso, vimos cómo **configurar un filtro de modelo**.

En el caso de que necesitemos emitir un remito a partir de una factura, podemos generar una
transformación. Veamos qué valores tendrá este comprobante. Ingresamos a la entidad
“Factura” y desde la solapa de Transformaciones, agregamos una, indicando el Nombre y la
Descripción.

El paso siguiente consiste en indicar el contexto “Entidad”, que configura el contexto de la
transformación, como así también de la condición y de la definición de valores.


Luego, completamos el resto de los campos requeridos y nos posicionamos sobre la definición de
valores. Establecemos la fecha del remito, que es la actual (Hoy()), el cliente que es el mismo y,
para cada ítem, tanto el producto, como el precio y la cantidad son los mismos. Es importante
que el tipo de dato obtenido por la expresión sea el esperado, en este caso, una colección de
productos, precios e ítems. El subtotal lo podemos dejar en blanco, ya que será calculado
directamente en el remito.

En este caso vimos cómo **crear una transformación con contexto entidad**.

Ahora, utilizaremos más expresiones, pero en este caso, para la definición de valores de un
desencadenante con otro contexto. Imaginemos el siguiente escenario: tenemos las entidades
“Remito” y “Movimiento de stock” y queremos generar un desencadenante desde “Remito”, para
que cada uno de sus ítems se transforme en una instancia de “Movimiento de stock”.

Posteriormente, podremos añadir un acumulador en “Movimiento de stock”, con el fin de tener
consolidada la información. Entonces, cada compra aumenta el stock y cada remito lo disminuye.

Al momento de crear el desencadenante desde “Remito”, establecemos a la colección de ítems
de la entidad como contexto.

De esta manera, estamos eligiendo el contexto de la Condición y de la definición de valores.
Luego, procedemos a completar los valores. Recordemos que la cantidad debe estar en negativo
ya que estamos restando stock, entonces la expresión en cantidad la indicamos:

- 1 * Cantidad


En este punto, ya podemos crear un remito y observar cómo se añaden instancias en
“Movimiento de Stock” desde la vista previa correspondiente.

Acá vimos cómo es posible definir un **desencadenante con contexto de colección.**

Ahora, especificaremos algunos casos a través de los cuales empleamos ciertas **funciones** que
permiten pasar entre textos que sean internacionalizables y aquellos que no lo sean. Tomando
como ejemplo la entidad “Producto”, encontramos dos atributos de texto: el “nombre”, que no
es internacionalizable; y la “descripción”, que sí lo es. Aquí nos interesa que, como valor inicial
de la descripción, se escriba el nombre.

Esto sería imposible, dado que ambos tienen distintos tipos de datos. Ahora bien, si usamos la
función “ **Traducir texto a idiomas** ” con sus parámetros, lo podremos conseguir.

Para ello, nos posicionamos sobre el atributo al cual queremos asignarle un valor, es decir, la
descripción. Especificamos la función junto con sus parámetros, de los cuales el primero es el
texto a traducir, en este caso, el nombre del producto. Mientras que el segundo parámetro es el
idioma al que lo estamos convirtiendo, en este caso, el español.

Traducir texto a idiomas(nombre;’es’)

Si en este momento intentamos cargar un producto, podremos notar cómo, al ingresar el
nombre, se autocompleta la descripción. De todas maneras, al ser un valor inicial, tenemos la
posibilidad de redefinirlo.

Así, logramos convertir un texto no internacionalizable, como lo es el nombre, en uno que sí
contenga esta característica. A continuación, realizaremos el proceso inverso.


Supongamos que de una grilla de productos solo queremos visualizar aquellos pertenecientes al
rubro “Repuestos”. Este atributo, esto es, el rubro de los artículos, es internacionalizable. En
efecto, no podemos utilizar directamente la expresión Rubro = ‘Transporte’, sino que debemos
incorporar, en la misma la función **Obtener traducción** , para tener la traducción en español:

Obtener traducción(Rubro.Rubro;”es”) = ”Transporte”

Para hacer **filtros con expresiones con fechas** , supongamos, que necesitamos filtrar todas las
facturas de la última semana. Podemos lograrlo a través de la función HOY. Entonces, nos
posicionamos sobre el filtro e indicamos que la fecha sea mayor a siete días. Es importante saber
que siempre que escribamos una fecha, debemos hacerlo entre llaves.

Fecha > Hoy() – {7 días}


Otro ejemplo, si quisiésemos asignar un valor mediante una expresión en un reemplazo global,
podemos hacerlo. En este caso, le asignamos la fecha al cierre de ciclo, por ejemplo, con la
siguiente expresión:

{31/12/2023}

Ahora, hagamos de cuenta que queremos filtrar en la factura los descuentos asociados al cliente,
es decir, contamos con una colección que los contenga.

Para lograr esto, nos posicionamos sobre el atributo “descuento” de Factura y en el filtro de
modelo, escribimos la expresión.

Esta instancia EN (en .super.esta instancia.cliente.descuentos generales buscar descuento)


Al estar posicionados en el filtro de modelo, “Esta instancia” hace referencia a aquella de
descuento. La palabra reservada **EN** , aquí, está actuando como un “ **contiene** ”. Recordemos que
A EN B retorna verdadero si A es un ítem de B. Y por último, tenemos la expresión .super.esta
instancia.cliente.descuentos generales que retorna la colección de descuentos asociados al
cliente de la cabecera. “Super”, en este caso, está indicando que queremos salir del contexto de
la entidad del descuento, para ir al contexto de la colección de descuentos de la factura. Luego,
nos movemos en la cabecera, al cliente y a su colección de descuentos asociados. Por su parte, el
“.”, en este caso, nos indica que nos referimos a una colección.

```
Muchas veces nos encontramos con la situación de que, al momento de crear una expresión,
Fastprg nos muestra un mensaje de error. Se debe tener en cuenta que Fastprg no asume nunca
un redondeo, entonces si el resultado de una expresión tiene más decimales que el tipo de dato
esperado, entonces Fastprg muestra un error.
Supongamos que se tienen definidos en el atributo de Subtotal 2 decimales y que precio y
cantidad tienen 4 decimales. Al intentar realizar Precio * Cantidad para calcular el Subtotal,
FastPrg detecta que el resultado tendrá mayor cantidad de decimales y, por lo tanto, no puede
asignarlo al Subtotal que tiene 2 y nos muestra un mensaje que indica Tipos de datos no son
compatibles.
```
```
En este caso, se podría aplicar la función
```
Redondear((Precio*Cantidad); 2)

```
para poder llevarlo a la cantidad de decimales que se esperan en el Subtotal.
```

```
Esta es una opción, sin embargo, también se podría usar la función Truncar() o se podría
redondear el precio antes de multiplicar. Podemos ver las funciones disponibles en el Anexo I:
Funciones del sistema, en la sección de Funciones Matemáticas.
Otra situación muy común es que Fastprg nos muestre el mensaje: Símbolo no encontrado. Esto
en general se debe a que nos encontramos en otro contexto o bien que hay un error de tipeo al
indicar, por ejemplo, un atributo. Entonces, si estamos posicionados en la colección de ítems e
intentamos hacer referencia a un atributo de cabecera, al no estar en el mismo contexto, Fastprg
no lo encuentra. Como vimos, para solucionar esta situación es necesario movernos a otro
contexto, por ejemplo con esta instancia, este ítem, etc.
```
### 2.9 Conversiones de Tipos de datos

```
En el caso en que en una Operación se utilicen Operandos incompatibles (es decir, Operandos
a los que no sea posible aplicarles la Operación debido a su tipo), el sistema sugiere las
acciones correctivas más usuales para dicha Operación.
En los siguientes ejemplos se muestra la edición de una expresión para el valor inicial de un
atributo basado en un tipo Texto. En este caso el sistema resalta los errores, y al posicionarse
```

sobre un error, se muestra un tooltip indicando el detalle del error y se ofrece aplicar las
acciones correctivas más comunes.

```
Imagen 1 : El cursor está posicionado sobre el operando Factura.Fecha y se presenta el tooltip.
```
```
Imagen 2 : El cursor está posicionado sobre el operando 10 y se presenta el tooltip.
```
```
Imagen 3 : El cursor está posicionado sobre la expresión y se presenta el tooltip anteriormente
descripto, ya que en este caso la incompatibilidad se presenta entre el tipo de dato del resultado de
la expresión y el tipo de dato del contenedor.
```
A continuación se muestra una tabla con las posibles combinaciones que pueden presentarse
al utilizar operandos de diferentes tipos.

Dentro de dicha tabla, asociado a cada par de tipos de datos involucrados en la operación, se
presenta un número que indica el comportamiento que deberá tener el sistema ante dicha
operación. El contenedor indica el tipo de dato en capa base que se espera del resultado de la
expresión. Para el los distintos tipos para representar una Fecha (Instante, Fecha y Hora, Solo
Fecha, Solo Hora) se agrupan en las columnas y filas “Fechas”, y luego más adelante en el
documento se detalla el comportamiento entre los mismos.

Respecto al Tipo de Dato contenedor “Texto Enriquecido” aplican las mismas
combinaciones que el tipo de dato “Texto”. Si se deseara realizar una operación con un tipo
de dato “Texto Enriquecido” sobre un contenedor diferente de su tipo, deberá aplicarse sobre
el mismo una función de sistema de conversión a tipo de dato a “Texto”, la cual extraerá del
texto enriquecido el texto sin formato, a partir de ahí aplicarán las mismas restricciones que
el tipo de dato “Texto”.

La descripción del comportamiento asociado a cada número se detalla a continuación
de la tabla.


**Contenedor: Numérico**

**Tipo de dato Numérico Texto Booleano Fechas Duración**

Numérico 2 3 3 7 7

Texto 3 3 3 3

Booleano 3 3 3

**Fechas** 7 7

Duración 7

**Contenedor: Texto o Texto Enriquecido**

**Tipo de dato Numérico Texto Booleano Fechas Duración**

Numérico 2 y 5 4 4 6 y 5 6 y 5

Texto 8 4 4 4

Booleano 5 4 4

**Fechas** 5 5

Duración 5

**Contenedor: Booleano**

**Tipo de dato Numérico Texto Booleano Fechas Duración**

Numérico 3 3 3 3 3

Texto 3 3 3 3

Booleano 1 3 3

**Fechas** 3 3

Duración 3

**Contenedor: Fechas**

**Tipo de dato Numérico Texto Booleano Fechas Duración**

Numérico 3 3 3 6 3

Texto 7 3 7 7

Booleano 3 3 3

**Fechas** 3 1

Duración 3

**Contenedor: Duración**

**Tipo de dato Numérico Texto Booleano Fechas Duración**

Numérico 6 3 3 3 6

Texto 7 3 3 7

Booleano 3 3 3

**Fechas** (^)
1 para la resta
3 para la suma 3
Duración 1
✓ _Comportamiento 1_ : Se realiza la operación sin efectuar conversiones.
✓ _Comportamiento 2_ : En el caso de que la operación implique un resultado que
puede tener una mayor precisión decimal que la que soporta el contenedor (por


```
ejemplo, una división o multiplicación entre números con decimales), se marca
con error la operación y se sugiere un listado de funciones de redondeo.
Adicionalmente, en caso de que la operación no sea una suma, se deberá evaluar
si el contenedor soporta la cantidad de dígitos a la izquierda de la coma. Para ello
se deberá suponer el peor escenario y marcar un error que obligue al usuario a
utilizar un contenedor que soporte una mayor escala. Para el cálculo del peor
escenario se deberá asumir que en las Entidades hay 10000 millones de
instancias, y en las colecciones será obligatorio que se indique la cantidad
máxima de elementos. En cambio, en los acumuladores o en el gdi, inferir un tipo
con la capacidad necesaria.
En caso contrario se realiza la operación sin realizar conversiones.
```
```
✓ Comportamiento 3 : En el caso de que la incompatibilidad sea con el contenedor
se marca con error toda la operación, y en el caso de que la incompatibilidad sea
entre los operandos se marca con error cada operando, indicando que hay una
incompatibilidad de tipos de dato. De ser posible, se sugerirán las funciones de
conversión apropiadas, para el primer caso la función estará aplicada a toda la
operación, y para el segundo caso se presentarán dos sugerencias una para cada
operando.
```
```
✓ Comportamiento 4 : Se marca con error el operando incompatible, y se sugiere
un listado con las funciones existentes de conversión desde el tipo incompatible
a texto. Luego de que el usuario lo convierte a Texto se debe validar el
comportamiento 8.
```
```
✓ Comportamiento 5 : Se marca con error toda la operación, y se sugiere un
listado con las funciones existentes de conversión desde el tipo incompatible a
texto. Luego de que el usuario lo convierte a Texto se debe validar el
comportamiento 8.
```
```
✓ Comportamiento 6 : Se marca con error el operando incompatible, y se sugiere
un listado para indicar la unidad que expresa el Número. Por ejemplo, días,
meses, años, horas, minutos, segundos, etc.
```
```
✓ Comportamiento 7 : Se marca con error la operación y se sugiere un listado de
funciones para convertir el valor en el tipo de dato del contenedor.
```
```
✓ Comportamiento 8 : Se debe validar si el resultado de la operación puede ser
almacenada dentro del contenedor. Para ello se plantea el peor escenario en
cuanto a la cantidad de caracteres que puede dar como resultado la operación y
se valida si entra en el contenedor. En el caso de que el resultado pueda ser de
un número mayor de caracteres que los que entran en el contenedor se deberá
marcar con error la operación y sugerir una función para truncar el resultado a la
cantidad de caracteres del contenedor.
```
El listado anterior sólo tiene en cuenta los casos que pueden producirse por
incompatibilidad por operaciones entre distintos tipos de datos; por lo tanto, no están
incluidos los casos de incompatibilidad de operaciones entre operandos con el mismo tipo de
dato. Por ejemplo, para la operación de división entre dos operandos de tipo texto, no se
detalla esta incompatibilidad en el listado anterior pero deberá producir un error.
Consideraciones en cuanto a los contenedores
Para los casos en los que el contenedor es de tipo Texto y el resultado de una
expresión es un número, al notificar la incompatibilidad de tipos, además de las funciones de
conversión existentes se presentará la función de conversión de números a letras ("literal").


```
Para los casos en los que el contenedor es de tipo Texto y el resultado
particularmente es un número de punto flotante, al notificar la incompatibilidad de tipos se
presenta un diálogo donde se sugiere funciones que permitirán especificar el formato de
conversión de dicho número a texto (redondeo, decimales, etc.).
```
```
En el caso de que la incompatibilidad se deba a que el contenedor espera un valor de
categoría simple y el resultado es una colección se deberá sugerir que en la expresión indique
una función de agregación.
```
#### Consideraciones para atributos basados en tipo fecha

```
En particular para las operaciones entre los diferentes tipos de Fecha (Solo Fecha,
Solo Hora, Fecha y Hora, Instante, Duración) para la suma:
```
```
^
Instante Fecha Y
Hora
```
```
Solo
Fecha
```
```
Solo Hora Duración
```
```
Instante No
permitido
```
```
No
permitido
```
```
No
permitido
```
```
No
permitido
```
OK

```
Fecha Y
Hora
```
```
No
permitido
```
```
No
permitido
```
```
No
permitido
```
OK

```
Solo
Fecha
```
```
No
permitido
```
```
No
Permitido
```
OK

```
Solo Hora
No
Permitido
```
```
No
Permitido
Duración
OK
```
```
Para el caso de la resta se tendrán las siguientes operaciones permitidas:^
Instante Fecha Y
Hora
```
```
Solo Fecha Solo Hora Duración
```
```
Instante OK
(duración)
```
OK

```
(duración)
```
OK

```
(duración)
```
```
No
permitido
```
OK

```
(instante)
Fecha Y
Hora
```
OK

```
(duración)
```
OK

```
(duración)
```
OK

```
(duración)
```
```
No
permitido
```
```
OK (fecha y
hora)
Solo
Fecha
```
OK

```
(duración)
```
OK

```
(duración)
```
OK

```
(duración)
```
```
No
Permitido
```
```
OK (sólo
fecha)
Solo Hora No
Permitido
```
```
No
Permitido
```
```
No
Permitido
```
```
No
Permitido
```
```
No
Permitido
Duración No
Permitido
```
```
No
Permitido
```
```
No
Permitido
```
```
No
Permitido
```
OK

```
(duración)
De las tablas anteriores se deberá tener en cuenta las siguientes consideraciones:
✓ Para el caso de la suma o resta de Instante, Fecha y Hora, Solo Fecha con una
Duración se deberá validar que la Duración tenga una unidad compatible con
la operación. Es decir la Duración deberá tener una unidad mayor que el tipo
con el que se hace la operación (Entendiendo que la unidad mayor es el año
y la unidad menor es el nanosegundo). Por ejemplo, a un Instante se le
puede sumar o restar una Duración con cualquier unidad, pero a un Fecha y
Hora no se le podrá sumar o restar una Duración que está en milisegundos,
o a un Solo Fecha no se le podrá sumar o restar una Duración que está en
Horas.
✓ Para el caso de operaciones de suma o resta entre Duraciones, las mismas
podrán no tener la misma unidad de medida, siempre que ambas duraciones
```

```
se encuentren en uno de los siguientes grupos y el resultado es siempre la
unidad de medida menor:
o Grupo 1: Semana o inferior: las unidad de tiempo posibles son
semana, día, horas, minutos o segundos. Ejemplo válido: { 2 días} -
{4 horas} devuelve { 44 horas}. Ejemplo inválido: {4 meses} + {2 días}
no se puede realizar porque no se sabe cuántos días tiene cada mes.
Lo mismo ocurre con la cantidad de días de un año.
o Grupo 2: Mes o superior: las unidad de tiempo posibles son mes o
año. Ejemplo válido: {1 año} + {4 meses} devuelve {16 meses}.
Ejemplo inválido: { 2 años} – {14 minutos} no se puede realizar por
el mismo motivo (la cantidad de días varía de mes a mes y de año a
año).
✓ Para el caso de la resta entre Instantes, Fecha y Hora, Solo Fecha:
o En los casos de que la operación sea entre diferentes tipos se
supondrá que la información faltante en el tipo de menor precisión
es cero. Por ejemplo, si resto a un Instante un Solo Fecha, se
supondrá que para el Solo Fecha el valor de la Hora, Minutos,
Segundos, Milisegundos, Nanosegundos es cero. Y luego se supone
que la operación se hace entre dos operandos del tipo de mayor
precisión.
✓ El resultado entre la resta de dos Solo Fecha será en días. Adicionalmente,
se podrá utilizar una función para indicar en qué unidad se desea el
resultado, siendo válidas unidades menores a días (horas, minutos,
segundos, milisegundos o nanosegundos). Por ejemplo, {10/10/2013} –
{01/07/2013} devuelve {101 días}. En el caso de querer calcular la cantidad
de horas entre las dos fechas se deberá especificar la unidad del resultado:
horas ({10/10/2013} – {01/07/2013}).
✓ El resultado entre la resta de dos Fecha y Hora será en segundos.
Adicionalmente, se podrá utilizar una función para indicar en qué unidad se
desea el resultado, siendo válidas unidades menores a segundos
(milisegundos o nanosegundos).
✓ El resultado entre la resta de dos Instantes será en nanosegundos.
```
En cuanto a la compatibilidad de los resultados de las operaciones entre Fecha con el
contenedor se deberá evaluar si el tipo del resultado es compatible y en caso de que no lo sea
sugerir funciones de conversión. Por ejemplo, si sumo un “Solo Fecha” con una duración en
días, y el contenedor es un “Fecha y Hora”, se deberá sugerir funciones de conversión de “Solo
Fecha” a “Fecha y Hora” para toda la expresión.

Para el caso de que el contenedor sea una duración, se devolverá el valor en la unidad
de medida del contenedor, siempre y cuando el contenedor y el resultado de la expresión
pertenezcan ambos a uno de los grupos detallados anteriormente ( _Grupo 1: Semana o inferior_
y _Grupo 2: Mes o superior_ )..

Para el caso de las operaciones de comparación (<, >, >=, <>, etc) estarán permitidas
para los siguientes casos:

✓ Entre dos Duraciones las mismas tendrán que tener la misma
unidad, o unidades inferiores a la semana, o una unidad en años y
otra en meses. En caso contrario se deberá sugerir funciones de
conversión.
✓ Entre Instante, Solo Fecha, y Fecha y Hora en cualquier combinación
de ellos. Para los casos que se usan tipos diferentes se supondrá
que la información faltante en el tipo de menor precisión es cero.
✓ Entre dos Solo Hora.
Si la unidad de medida es “fecha y hora”, las operaciones de comparación permitidas
son:
```
Literal de
fecha/hora sin ZH
Ejemplo:
{3/1/2015 18:30}
```
```
Literal de
fecha/hora
con ZH
Ejemplo:
{5/1/2015
12:00 GMT
```
**- 3}**

```
Atributo de
tipo
fecha/hora sin
considerar ZH
Ejemplo:
FechaCompra
```
```
Atributo de tipo
fecha/hora
considerando su
ZH
Ejemplos:
ConsiderarZona
Horaria(FechaCo
mpra)
ConvertirZonaH
oraria(FechaCo
mpra, “GMT-3”)
```
**Literal de fecha/hora
sin ZH**

**Ejemplo: {1/1/2015
15:00}**

```
OK sin ZH) No
Permitido
```
```
OK (sin ZH) No Permitido
```
**Literal de fecha/hora
con ZH**

**Ejemplo: {10/1/2015
10:12:22
Europe/London}**

```
No Permitido OK (con ZH) No Permitido OK (con ZH)
```
**Atributo de tipo
fecha/hora sin
considerar ZH**

**Ejemplo:
FechaVencimiento**

```
OK (sin ZH) No
Permitido
```
```
OK (sin ZH) No Permitido
```
**Atributo de tipo
fecha/hora
considerando su ZH**

**Ejemplos:
ConsiderarZonaHorar
ia(Fecha
Vencimiento)**

**ConvertirZonaHoraria
(FechaVencimiento,
“GMT-3”)**

```
No Permitido OK (con ZH) No Permitido OK (con ZH)
```
```
Para los casos de conversión de Fecha a Texto, las funciones de conversión tendrán
dos parámetros:
1 - El primer parámetro permitirá indicar un formato de fecha con el cual realizar la
conversión: Corta, Media, Larga, o Completa. Estos formatos podrán definirse en
la configuración regional de cada usuario, y adicionalmente deberán definirse a
nivel de todo el sistema y se podrá especificar un formato particular para cada
empresa o sucursal, así como para otros elementos, como por ejemplo
formularios.
```
```
2 - El segundo parámetro indica si se tomará el formato de la fecha definida para el
usuario, o la definida para el sistema. En este último caso, la búsqueda del
formato deberá efectuarse de lo particular a lo general. Por ejemplo, primero en
el formulario, luego en la configuración general, etc. En caso de no estar definido
```

```
en alguno de los elementos, se deberá utilizar la configuración definida en el
elemento jerárquicamente superior.
Conversión de tipos de atributos
```
```
Destino
```
**Origen**

```
Simple Compuesto Referencia Referencia a
colección
```
```
Colección Enumerado Secuencia
```
**Simple** No Si Si Si Si Si No

**Compuesto** No Si Si Si Si Si No

**Referencia** Si Si Si Si Si Si No

**Referencia a
Colección**

```
Si Si Si Si Si Si No
```
**Colección** Si No No No No Si No

**Enumerado** Si Si Si Si Si Si No

**Secuencia** No No No No No No No

```
Detalle de funciones:
```
```
Función Descripción Ansi- 92
Convertir Referencia a
Simple (tipo de
atributo)
```
```
Convierte un tipo de atributo de categoría
Referencia a un tipo atributo de categoría
Simple. Si se aplica a un atributo que
contiene un valor, se copia el atributo
descriptor de la referencia en el atributo
simple.
```
```
Ejemplo: Convertir
Referencia a Simple
(Cliente; Nombre de
cliente)
```
```
Convertir Referencia a
Colección a Simple
(tipo de atributo)
```
```
Convierte un tipo de atributo de categoría
Referencia a Colección a un tipo atributo de
categoría Simple. Si se aplica a un atributo
que contiene un valor, se copia el atributo
descriptor de la colección referenciada en el
atributo simple.
```
```
Ejemplo: Convertir
Referencia a Simple
(Direcciones de
Cliente; Dirección del
Cliente)
```
```
Convertir Colección a
Simple (tipo de
atributo)
```
```
Convierte un tipo de atributo de categoría
Colección a un tipo atributo de categoría
Simple. Si en un atributo del tipo que
cambia, la colección contiene más de un
elemento, los mismos se concatenan
separados con el “separador de lista”
definido en la configuración regional del
Modelo.
```
```
Ejemplo: Colección a
Texto Enriquecido()
```
```
Colección a Texto
Internacionalizable()
```
```
Convertir Enumerado
a Simple (tipo de
atributo)
```
```
Convierte un tipo de atributo de categoría
Enumerado a un tipo atributo de categoría
Simple. Si se aplica a un atributo que
contiene un valor, se copia la descripción del
valor del enumerado en el atributo simple.
```
```
Ejemplo: Convertir
Referencia a Simple
(Direcciones de
Cliente; Dirección del
Cliente)
Convertir X a
Compuesto (tipo de
atributo,
expresión/es)
```
```
Convierte un tipo de atributo de categoría X
a un tipo atributo de categoría Compuesto.
Se debe definir una expresión para indicar
cómo se distribuye el primer tipo en un
compuesto. Se debe especificar una
expresión por cada tipo que contenga el
compuesto.
```
```
Ejemplo: Convertir
Simple a Compuesto
(Domicilio; izquierda
(domicilio; 10);
derecha( domicilio;3))
```

```
Convertir X a
Referencia (tipo de
atributo, entidad
referenciada)
```
```
Convierte un tipo de atributo de categoría X
a un tipo atributo de categoría Referencia.
Se debe definir la entidad que referencia.
```
```
Ejemplo: Convertir
Simple a Referencia
(nombre de cliente;
Cliente)
Convertir X a
Referencia a Colección
(tipo de atributo,
colección
referenciada)
```
```
Convierte un tipo de atributo de categoría X
a un tipo atributo de categoría Referencia a
Colección. Se debe definir la colección que
referencia.
```
```
Ejemplo: Convertir
Simple a Referencia a
Colección (dirección de
cliente;
Cliente.Direcciones)
Convertir X a
Colección (tipo de
atributo, colección
referenciada)
```
```
Convierte un tipo de atributo de categoría X
a un tipo atributo de categoría Colección de
X (por ejemplo, si el atributo es simple, se
convierte a un atributo colección de
simples). Si se aplica a un atributo que tiene
un solo valor, la colección resultante tendrá
un solo ítem.
```
```
Ejemplo: Convertir
Simple a Colección
(dirección de cliente;
Direcciones)
```
```
Convertir X a
Enumerado (tipo de
atributo)
```
```
Convierte un tipo de atributo de categoría X
a un tipo atributo de categoría Enumerado.
Si se aplica a un atributo que tiene un solo
valor, el enumerado resultante tendrá un
solo ítem.
```
```
Ejemplo: Convertir
Simple a Enumerado
(Forma de Pago; Forma
de Pago)
```
### 2.10 Manejo de nulos

```
Es importante destacar que el comportamiento es diferente cuando una expresión es nula (es
decir que no se configuró la misma) y cuando el resultado de la evaluación es nulo.
Por ejemplo, cuando una Regla de negocios se ejecute y una condición no se pueda evaluar
porque alguno de los atributos a evaluar dentro de la expresión es nulo (no posee valor), las
acciones dentro de esta condición no se ejecutarán.
De todas maneras, en las condiciones se puede especificar que se evalúe si el atributo no es
nulo, por ejemplo: si se desea ejecutar una acción si “mes(fecha) = 12” y en algunas instancias
la fecha es nula, se puede cambiar la condición a “no Esnulo(fecha) y mes(fecha) = 12”.
En todas las operaciones sobre colecciones, si alguno de los elementos que aplican a la
operación es nulo, se ignora. Por ejemplo, si monto suma todos los subtotales de los ítems de
factura, si existe un ítem cuyo subtotal está vacío, se ignora para la sumatoria. Esto no se
deberá confundir con los valores 0.
Supongamos el siguiente ejemplo: Se tiene una colección de valores enteros y se obtiene:
Suma y Cuenta de los mismos. Veamos 2 ejemplos que a simple vista parecen similares, pero
varían en sus resultados.
Colección 1:
Valor entero
20
40
(nulo)
60
Suma: 120
Cuenta: 3
```
```
Colección 2:
Valor entero
20
40
0
60
Suma: 120
Cuenta: 4
```
```
En la suma, ambos valores son iguales y para la cuenta de ítems, en el caso de la colección 1,
el valor nulo se omite y en el caso de la colección 2 el valor 0 se tiene en cuenta.
```

```
Otro caso a considerar es en los atributos de tipo booleano, si no tienen valor inicial toman
valor nulo, sin embargo, al visualizarlos se ven de la misma manera que el falso, por lo tanto
es sumamente importante validar que no sea nulo antes de utilizarlo, o darle un valor inicial y
de esta manera evitar que tome el valor nulo.
Las siguientes son las reglas al momento que comparar valores nulos. Es importante
considerarlas ya que podrían resolverse algunas expresiones y puede que no necesariamente
el modelador tenga que siempre completar cada uno de los atributos.
```
```
Y Verdadero Nulo Falso
Verdadero Verdadero Nulo Falso
Nulo Nulo Nulo Falso
Falso Falso Falso Falso
```
```
O Verdadero Nulo Falso
Verdadero Verdadero Verdadero Verdadero
Nulo Verdadero Nulo Nulo
Falso Verdadero Nulo Falso
```
NO

```
Verdadero Falso
Nulo Nulo
Falso Verdadero
```
```
Esnulo()
Verdadero Falso
Nulo Verdadero
Falso Falso
```
```
No Esnulo()
Verdadero Verdadero
Nulo Falso
Falso Verdadero
```
### 2.11 Memoria de cálculo

Con el objetivo de que un usuario pueda comprender el motivo por el cual a una instancia en Fastprg se
le asignó un valor, Fastprg proporciona una funcionalidad que almacena la memoria de cálculo con cada
uno de los elementos que asignaron un valor al mismo, como lo puede ser un valor inicial, valor calculado,
regla de negocio, etc.
Para acceder a esta funcionalidad, el usuario debe posicionarse sobre el dato del cual se desea obtener la
información, por ejemplo, en el ABM Factura, en la columna “importe”, en el número de importe en el
que se quiera obtener la información, y allí se presenta una ayuda emergente en la que existe un ícono
para poder acceder a la mencionada funcionalidad.

El comportamiento de esta funcionalidad, varía en función del tipo de ambiente en el que se encuentre
trabajando el usuario:

- En el caso de ser ambiente de desarrollo, se presentará en forma predeterminada la
    memoria de cálculo en cada una de las instancias en edición, pero una vez confirmada la
    instancia, esta información no se persiste, y además se presentará un botón en la toolbar
    que permite activar o desactivar la memoria de cálculo, que por defecto siempre estará
    desactivado.
- En el caso de ser otro tipo de ambiente, solo se presenta esta información cuando el atributo
    tiene activa la memoria de cálculo.


Para más información sobre como activar esta funcionalidad, ver documento funcional de tipos de
atributo.

Dependiendo del origen del dato al cual se quiere obtener información, varia la estructura JSON dentro
de la funcionalidad:

- Si el origen del dato proviene de un **desencadenante** , transformación, valor inicial o valor
calculado, la estructura JSON es la siguiente:

**Ejemplo:**
{"Origen": "",
"Valor": "",
"Expresión": "",
"Detalle": []
}

- Si el origen del dato proviene de una **regla de negocio** , la estructura JSON es la siguiente:

**Ejemplo:**
{"Origen": "",
"Nombre": "",
"Acción condicional": "",
"Condición": "",
"Acción": "",
"Valor":,
"Expresión": "",
"Detalle": []
}

La estructura JSON dentro del detalle es igual siempre sin importar de donde proviene el dato, sin
embargo, existen 2 estructuras distintas:

- La primera es la estructura por defecto, en la que se visualizan los ítems de la expresión y sus
valores.
Ejemplo:
"Detalle": [
{"Ítem": "",
"Valor": },
{"Ítem": "",
"Valor": },
{"Ítem":,
"Valor": } ]
- La segunda estructura se da en los casos que, dentro del detalle, existe un ítem que proviene de
otra expresión, en ese caso, además del ítem y del valor, también se visualizara la expresión de donde
proviene ese ítem y el detalle desglosando la nueva expresión:
Ejemplo:
{"Ítem": "",
"Valor": ,
"Expresión": "",
"Detalle": [{
"Ítem": "",
"Valor": },
{"Ítem": "",
"Valor": } ]


### 2.12 Seguridad

Existen 2 momentos en cualquier expresión, un primer momento donde se define la misma y otro donde
se ejecuta obteniendo un resultado. Ese primer momento lo llamamos **_definición_** **de una expresión** y
aplica tanto a la definición inicial como a la modificación de una expresión. La seguridad que se evalúa en
este momento es la siguiente:

- Por cada atributo, se evalúa si tiene permiso de consultar atributos en la entidad [seguridad de
    modelado] O si tiene permiso de consulta en el atributo en algún ambiente [seguridad de
    atributo]. En el caso de los pathfields, se valida la seguridad en cada atributo del camino.
- Por cada entidad, se evalúa si el usuario tiene permiso de consultar [seguridad de entidad].
- Por cada función, se evalúa si el usuario tiene permiso de consulta en algún ambiente.
- Por cada acumulador, se evalúa si el usuario tiene permiso de consulta de acumulador en
    cualquier dimensión [seguridad de instancias en el acumulador] o permiso de consulta de
    acumuladores en seguridad de la entidad [seguridad de entidad].

Si el usuario **NO** tiene permiso en algún elemento dentro de la expresión, **NO** puede ver la expresión ni
editarla.

Por otro lado, los permisos que se validan en la **_ejecución_** **de las expresiones** varían dependiendo de
dónde se encuentren.

_Expresiones sujetas a seguridad_ :

- Tootilps
- Campo calculado/Columna calculada
- Campo de atributo o cualquier componente visual dentro de un formulario/gdi

_Expresiones NO sujetas a seguridad_ :

- Formato condicional
- Condición de visualización y edición
- Filtros (en vistas, en un componente, etc)
- Expresión de agrupamiento de las instancias dentro de la banda de detalle.
- Expresión para mandar a imprimir a una impresora
- Expresión para obtener idioma
- Todas las expresiones definidas en los editores (Entidades, TA, Actividades): valor inicial,
    validaciones, expresión para agrupar transformaciones, condiciones de formularios.

_Expresiones mixtas_ :

- Cuando el mensaje de error muestra un atributo en el cual el usuario no tiene permiso de
    lectura, se deberá ofuscar el valor del atributo con el mismo formato que las contraseñas:
    o ***. Por ejemplo: El límite de crédito debe ser menor a 1000 y actualmente es ”. Ver si
    esto no es costoso en la implementación.


Por otro lado, con respecto a entidades de sistema, cuando se usa un atributo de una entidad de sistema
en una expresión, por ejemplo: en una condición de la RN se pone: Actividad.Nombre = Facturación, se
debe tener en cuenta el permiso “consultar actividades” en el Modelo (es decir permiso de consulta en
todas las actividades, no en cada una). Es decir, en este caso, no se controla la seguridad por atributo (ya
que no existe).

## 3. Funciones

### 3.1 Definición y uso.

Una Función es un grupo de instrucciones con un objetivo en particular y que se ejecuta al ser llamada
desde otra Función o desde una expresión. Pueden recibir datos a través de parámetros y deben retornar
un resultado. Tienen un nombre único, un Tipo de dato de resultado, una lista de parámetros de entrada
y sus instrucciones.

### 3.2 Tipos de funciones

#### 3.2.1 De usuario

```
Existen distintos tipos de funciones, iniciamos con las más simples: las funciones estándares de
usuario.
En un caso hipotético, necesitamos aplicar un descuento del 15% en una factura si el cliente es
mayorista. De lo contrario, no se efectúa el descuento. Si nos dirigimos a la entidad Factura,
podemos lograr esto con una función, la cual recibe un parámetro: el cliente.
A la función la llamamos Descuento por cliente, tiene también una descripción y una
documentación, al igual que cualquier elemento de FastPrg. Además, cuenta con una categoría
que nos facilita agrupar las funciones y un tipo de dato de retorno, esto es, lo que devolverá la
función.
Una función recibe una colección de parámetros que podrá utilizar para evaluar y calcular su
retorno, los cuales pueden ser interactivos o no. También, disponemos de las condiciones, por
las que definimos el cálculo que realizará la función para obtener nuestro valor de retorno.
En el caso del ejemplo, tenemos el parámetro Cliente. Dado que recibimos una referencia,
podemos navegarla. La primera condición consiste en que sea mayorista (Cliente.Mayorista =
verdadero) y escribimos, entonces, su retorno: 0.85.
Como segunda condición, establecemos que el cliente no sea mayorista
(esnulo(Cliente.Mayorista) o Cliente.Mayorista=Falso) y determinamos su retorno: 1. Una vez que
hayamos finalizado estos pasos, tenemos modelada nuestra función.
Se debe tener en cuenta que:
```
- El contexto para las condiciones y las expresiones es el de los parámetros.
- Las condiciones se evalúan desde arriba hacia abajo, es decir, primero se chequeará que
el cliente sea mayorista y luego que no lo sea.
- El retorno de las expresiones debe ser compatible con el definido en la función.
- Si ninguna condición se cumple, la función retornará nulo. Entonces, una buena práctica
consiste en definir una última condición que sea siempre verdadera y un valor por defecto.
- Los parámetros de entrada pueden ser de cualquier tipo excepto una colección.

#### 3.2.2 De sistema

```
FastPrg provee ciertas funciones que asistirán al usuario cuando quiera obtener o generar datos,
cambiarles el idioma, o convertir distintos tipos de atributos. Estas funciones son de solo lectura,
no pueden ser modificadas por el usuario.
La lista es muy extensa, y podemos encontrarlas con su documentación y ejemplos de uso dentro
del acordeón y en el Anexo I: Funciones del sistema.
```

### 3.3 Categoría de las funciones

Las funciones se agrupan en categorías de manera de encontrarlas en cada grupo. Estas categorías por
defecto vendrán ya creadas en base a las de las Funciones del Sistema. Algunas categorías son: Texto,
Fecha hora, Matemática, etc. En el acordeón, encontramos las funciones dentro de cada categoría.

### 3.4 Tipo de dato de retorno

Las funciones siempre devuelven un resultado, ese resultado debe ser de un único tipo que se indica al
modelar la función o está definido en las funciones de sistema.

### 3.5 Retorna colección

Esta opción indica que, en lugar de devolver un valor del tipo de retorno, el resultado de la función será
una colección de ese tipo. Tendrá un ítem por cada expresión cuya condición sea verdadera.

Supongamos que, según la cantidad de productos de una compra, les daremos un regalo a nuestros
clientes. Entonces, determinamos las siguientes condiciones:

- Si tiene más de cinco productos, se lleva una lapicera.
- Si supera los diez, obtiene, además, una agenda.
- En caso de comprar más de veinte productos, aparte de la lapicera y la agenda, le regalamos una
mochila.
Para esta situación, podríamos modelar la función que calcula los obsequios de esta manera, con la
propiedad activada, y como consecuencia, se sumarán aquellos regalos cuya condición se cumpla. Esta
función devuelve una colección de obsequios.

### 3.6 Parámetros

Los parámetros son un conjunto de elementos que se reciben al momento de invocar a la función. Son los
que definen el contexto de las expresiones utilizadas en Condición y en Expresión.
Al invocar la función, los argumentos se separan con el Separador de lista definido en la configuración
regional del dominio para el idioma del usuario. Además, los parámetros que se pasan, pueden ser
cualquier elemento que contiene valor (Atributos, Acumuladores, literales, valores devueltos de
Funciones y Expresiones). El tipo de datos del parámetro debe coincidir exactamente con el tipo de
atributo definido en la función, para ese parámetro.

Por cada parámetro se podrá especificar:

✓ **Nombre** : es el nombre del _Parámetro_. Deberá ser único para una misma _Función_ y debe ser
internacionalizable.
✓ **Tipo** : Es el _Tipo de dato_ del _Parámetro_. Los parámetros pueden ser de cualquier tipo simple, no
pueden ser colección.
✓ **Descripción** : permitirá indicar una breve descripción del _Parámetro_. La misma es internacionalizable.

El orden de los parámetros para la función se obtiene del orden en la grilla (el primer parámetro en la
grilla, el de más arriba, es el primer parámetro de la función).

Si se recibe como parámetro, un dato tipo referencia, es posible acceder a los atributos de cabecera de la
instancia referenciada pero NO recorrer sus colecciones.

### 3.7 Condiciones y orden de ejecución

Es donde se define qué retorna la función. Se tienen un conjunto de condiciones y el valor de retorno para
cada una de ellas. Cada condición se evalúa en el orden en que están ingresadas, hasta que de verdadero.

✓ **Condición** : Permite introducir una _Expresión_ que en caso de evaluarse como verdadera se ejecutará
la _Expresión_ indicada en el siguiente campo.
✓ **Expresión** : Indica la _Expresión_ que deberá ser ejecutada.
✓ **Documentación:** Indica en forma coloquial, cuál es la condición que se debe cumplir para devolver el
resultado de la expresión, y cuál es el valor que devuelve esa expresión. La idea es que el usuario lo
entienda rápidamente sin tener que interpretar las expresiones.

En el caso de que se indique que retorno es _multivalor_ la función deberá devolver una colección con el
resultado de todas las expresiones que fueron ejecutadas. En caso contrario, solo se ejecutará la primera
expresión cuya condición sea evaluada como verdadera. Si no se cumple ninguna condición, la función
devuelve nulo.


Como se mencionó, el orden de ejecución es secuencial según el orden establecido en las condiciones. Es
por esto que se debe prestar suma importancia al orden en que se escriban las mismas.
Por ejemplo, supongamos la siguiente situación:
Se aplica un descuento al cliente según el monto del total de la factura, que se recibe como parámetro.
El descuento es de 10% hasta $ 50.000; 15% hasta $200.000 y 20% en adelante

Entonces, si escribimos las condiciones de la siguiente manera:
Total factura > 0 10%
Total factura > 50.000 15%
Total factura > 200.000 20%

Al cumplirse la primera condición, no se evaluarán las siguientes, por lo tanto, esta función siempre
devuelve un descuento del 10%.

En cambio, si las escribimos de la siguiente manera:
Total factura > 200.000 20%
Total factura > 50.000 15%
Total factura > 0 10%

En este caso, va a devolver el descuento correspondiente según el monto. Porque al no cumplirse una
condición, seguirá evaluando las condiciones restantes, hasta que se cumpla alguna.

### 3.8 Contexto de ejecución

El Contexto siempre es el de los parámetros, sean interactivos o no.

### 3.9 Sin almacenar resultado

En el modelo editores, adicionalmente se presenta la propiedad “Sin almacenar resultado”. En caso de
estar activa, indica que el valor del resultado de la evaluación de la función no será “cacheable”, es decir,
no se almacenará en cache.
Inicialmente, solo se utilizará en las funciones:

- Valor de tolerancia de imputación.
- Valor residual de conversión de imputación.

### 3.10 Funciones interactivas.

Denominamos **Función interactiva** a aquella **Función de usuario** que tiene configurado al menos un
**parámetro interactivo**.

A continuación, indicaremos cómo utilizar los parámetros interactivos. Recreemos el siguiente ejemplo:
tenemos un GDI con las facturas de los clientes y queremos ver, en forma dinámica, las facturas hechas
en un rango particular y para un cliente particular.

Si nos dirigimos al filtro del GDI, observamos que esto se logra con una función, la cual recibe tres
parámetros interactivos. Estos son el cliente, la fecha desde y la fecha hasta del rango.


Puesto que los filtros esperan un valor lógico, esa es la respuesta de la función. Como notamos, a los
parámetros interactivos podemos definirles un valor inicial para cuando el usuario no desee cambiarlo, es
decir, se utilizará ese mismo cuando se haga uso de la función sin intervención del usuario. Por ejemplo,
al ejecutarse una tarea programada con una de integración.

Dejando de lado a qué nos referimos con parámetros interactivos, el resto de la función es la misma.
Debemos determinar las condiciones y escribir las expresiones que retornan. En este caso, verifica que el
cliente de la factura sea el pasado por parámetro y que la fecha esté en el rango.

Desde el GDI ya creado, vemos cómo FastPrg nos pide directamente que le asignemos valores a los tres
parámetros, aunque nos indica, por defecto, que el rango de las fechas es de dos meses, siendo hoy la
fecha límite. En caso de desearlo, podemos cambiarlo.

Ahora sí, vale hacer una aclaración: se llaman parámetros interactivos, ya que a medida que los
cambiamos, se modifica el filtro.

Si en el mismo GDI tuviésemos otra grilla con el mismo filtro, el valor que seleccionamos será utilizado en
ambas grillas. Nos pedirá solo una vez cada parámetro interactivo.

En el caso contrario, es decir, si tenemos distintas funciones interactivas, se solicitará una vez por cada
una de ellas, incluso aunque pidan el mismo dato y con el mismo nombre.

Es importante señalar que a los parámetros interactivos podemos utilizarlos en las grillas, en las
planificaciones o en las tareas de integración. Si quisiésemos, por ejemplo, hacer una exportación del libro
de IVA, solo basta con usar un parámetro que indique el período, sin necesidad de modificar la tarea de
integración asociada, constantemente.

En el **editor de funciones** está la solapa para configurar parámetros interactivos. Estos parámetros
cumplen la función de **variables** dentro de una función al igual que los parámetros de entrada. No se
pasan por valor al momento de invocar la función, sino que el sistema los pregunta mediante un panel de
ingreso de valores antes de evaluar la misma.

**Por cada parámetro interactivo se debe especificar:**


✓ **Nombre** : _Atributo requerido_. Es el nombre del Parámetro. Es un texto internacionalizable y debe ser

único para una misma Función. No puede haber ni otro parámetro interactivo con el mismo nombre
ni otro parámetro de entrada con el mismo nombre. Este mismo nombre es el que se muestra como
etiqueta, en el panel de ingreso de valores por parte del usuario.
✓ **Tipo de atributo** : _Atributo requerido_. Es el Tipo de dato del Parámetro. Es referencia a tipo de
atributo. No se podrán seleccionar tipos de atributos compuestos ni colecciones. A partir de este tipo
de dato se infiere el widget a mostrar en el panel de ingreso de valores.
✓ **Valor inicial** : Es el valor por defecto que tomará ese parámetro. Es una expresión. Se muestra este
valor en el widget correspondiente en el panel de ingreso de valores. Se toma como valor
predeterminado cuando no existe interacción. Este valor inicial puede establecerse con una expresión
obtenida del contexto global o también pueden utilizarse los parámetros de entrada de la función.
✓ **Descripción** : Permite indicar una breve descripción del parámetro. Es un texto internacionalizable y
tiene la característica de verse como ayuda emergente en el panel de ingreso de valores.
✓ **Documentación** : Permite ingresar una explicación del parámetro en el caso de ser necesaria. Es un
texto multimedia internacionalizable y tiene la característica de verse como documentación asociada
a la ayuda emergente en el panel de ingreso de valores.

```
Nota de arquitectura
Field condition para los atributos:
Nombre : Field condition = “INTERACTIVE_PARAMATER_NAME”
Tipo de atributo : Field condition = “INTERACTIVE_PARAMATER_TYPE”
Valor inicial : Field condition = “INTERACTIVE_PARAMATER_VALUE”
El contexto de la expresión del Valor inicial será GLOBAL (sin incluir parámetros de entrada)
```
Para el filtro del ejemplo anterior, podríamos armar una **función** con las siguientes características:

- **Parámetros interactivos**
    o Ingresar fecha: dato tipo fecha y con valor inicial = hoy()
- **Condición:**


```
Los parámetros interactivos no se pasan al ser invocada la función, sino que el sistema pide su
ingreso por pantalla.
El orden que tienen los parámetros en la grilla es el orden en que aparecen, la etiqueta y widget
correspondientes, en el panel de ingreso de valores.
Si se elimina un parámetro interactivo, el sistema valida que el mismo no esté siendo usado en
una expresión de la solapa de Condiciones.
Si en las expresiones de la solapa de condiciones, se usan funciones interactivas, estas serán
evaluadas estrictamente con sus valores predeterminados, no se pedirán por pantalla.
En cuanto a su Invocación :
```
- En caso de existir una **interfaz visual** , se solicitan los valores para los parámetros interactivos.
    En otros casos, se hará la ejecución con el valor predeterminado que se le dé a cada
    parámetro de la función.
- Cuando haya una interfaz visual, se define genéricamente, que la invocación de parámetros
    interactivos se hará en el **panel de mensajes**. Es un subpanel dentro del panel de mensajes.
    Puede haber, por ejemplo, invocación de una función interactiva en:
       o **Vista de información** : En las expresiones de filtros definidos para cada componente
          de la vista. Al invocarse desde una vista de información, cuando se ejecuta la misma,
          se intentará utilizar los valores predeterminados cargados en la función para cada
          parámetro, en caso de no tener valor alguno de ellos, se deberá solicitar el valor a
          los usuarios en el panel de mensajes antes de mostrar el resultado.

```
o Tarea de integración : En la expresión de filtro de instancias definido para una tarea
de exportación de datos. Se abrirá el panel pidiendo los valores para los filtros y
mostrando los valores por defecto. A diferencia de la invocación desde un GDI,
cuando se invoca desde una tarea de integración, se piden siempre los parámetros
interactivos, aunque todos tengan configurados valores por defecto, antes de
ejecutar la actividad. Es posible utilizar los parámetros interactivos en la expresión
que da nombre al archivo que surge de la tarea de integración. Por ejempo, si se va
a exportar información a un archivo para hacer una presentación a un organismo,
se ingresa la fecha del período que se está exportando y esta fecha puede formar
parte del nombre del archivo obtenido, para cumplir con el formato requerido por
el organismo.
```
- El panel de ingreso de valores para parámetros interactivos tiene un botón “Confirmar” para
    disparar la evaluación de las expresiones involucradas.
       o En el caso de un GDI, al ingresar o modificar valores de los parámetros interactivos
          y presionar botón de confirmación, el sistema evalúa las expresiones y calcula o
          recalcula el conjunto resultado para cada componente involucrado.
       o En el caso de una tarea de integración, al ingresar valores de los parámetros
          interactivos y presionar botón de confirmación, el sistema evalúa la expresión de
          filtro, calcula el conjunto resultado para exportar y dejar en read only los valores de
          los mismos porque ya no se podrán modificar.

Como no es obligatorio que se configuren los valores por defecto de los parámetros interactivos, se
definen en forma genérica los siguientes comportamientos:

- Se muestra siempre expandido el Panel de mensajes (Excepto que no haya interacción del
    usuario: GDI automático por tarea programada, Tarea de integración por tarea programada).
- Al ingresar se evalúan las expresiones y se muestran los resultados filtrados. Si quedan
    parámetros sin valor, la expresión se evalúa igualmente.
- El usuario puede modificarlos y, al confirmar, se reevalúan las expresiones, pero en las Tareas de
    Integración, al confirmar quedan de solo lectura.


- En los casos en los que no hay interacción del usuario, si se pudieron resolver las expresiones sin
    error entonces se ejecuta la tarea. Si no se pudo resolver alguna expresión de filtro, no se ejecuta
    la tarea quedando registro del error.

En el documento de **Estándares de interfaz de usuario** , se detallan las características y comportamiento
del panel de ingreso de valores para los parámetros interactivos.

Respecto del **procesamiento** :

- Si una función interactiva se invoca en una expresión de filtro, los parámetros se piden **una sola**
    **vez** y **no para cada registro a evaluar**.
- Si en una misma expresión se invoca más de una vez a **la misma función interactiva** , se pregunta
    por pantalla **solo una vez**.
- Si en una **misma actividad** se evalúan varias expresiones, y en esas expresiones se invoca más de
    una vez **la misma función** interactiva, se pregunta por pantalla **solo una vez**. Por ejemplo, en una
    vista de información con varias grillas con filtro.
- Si en una **misma actividad** se evalúan varias expresiones, y en esas expresiones se invocan varias
    **funciones** interactivas, se van a preguntar por pantalla todos los parámetros interactivos al
    mismo tiempo. Por ejemplo, en una vista de información con varias grillas con diferentes filtros.

### 3.11 Funciones de consumo de servicios sincrónicos

Las funciones que consumen dispositivos o servicios web realizan el consumo de forma sincrónica. Esto
implica que, a diferencia de los consumos que tienen como origen la acción de una Regla de negocio, el
mismo se efectúa **por cada unidad de cambio**.

Una vez completados los datos básicos correspondientes al tipo de consumo, el sistema brinda la opción
de completar cada uno de los parámetros de entrada/invocación con los que luego se realizará el
consumo.

Dichos parámetros se obtienen de los siguientes lugares:

#### 3.11.1 Consumo de operación de Servicio web

```
Se obtienen los parámetros de entrada de la operación seleccionada y el sistema, además, debe
crearlos con los valores predeterminados que fueron definidos en la misma. Se permite
seleccionar si desea que la función retorne un único valor (en cuyo caso se permitirá seleccionar
el atributo correspondiente) o si se desea que la función realice el retorno de la instancia
completa.
```
- **Mediante agente** : Permite que el consumo del servicio web se realice a través del agente
    para que pueda comunicarse con el dispositivo físico final. Al activar esta opción, el sistema
    adicionalmente presenta las siguientes opciones, las cuales se detalla su funcionamiento en
    el siguiente ítem _Consumo de dispositivo_ :
       o **Tipo de dispositivo**. Tener en cuenta que solo se presentarán los tipos de
          dispositivos los cuales tengan activa la propiedad Consumo por web service.
             ✓ **Origen de dispositivo.**
                - **Dispositivo fijo.**
                   o Dispositivo
                - **Dispositivo Predeterminado**
                   o Predeterminado del usuario autenticado
                   o Predeterminado del Sitio
                   o Predeterminado del dominio
                - **Dispositivo mediante Expresión**
                   o Expresión
Para más información acerca del consumo de web service mediante dispositivos, ver
especificación funcional de dispositivos.
Supongamos, ahora, que debemos cargar una factura a un cliente y para ello necesitamos el
código que nos provee AFIP. Existen distintas formas de conseguir este valor, pero nosotros lo
haremos mediante una función que consuma un web service. Es importante mencionar que este
debe estar previamente creado.


Si activamos la propiedad **Consumo de servicio web** , se nos oculta la solapa de condiciones pero
se habilitan dos más para poder definir el webservice a consumir, junto con sus valores.
En la primera, podemos establecer el grupo de web service, el web service en sí y la operación
que, efectivamente, consumirá la función.

En la segunda, visualizamos los parámetros de invocación del servicio web, los cuales tienen
como valores iniciales aquellos definidos en la operación del servicio, que pueden redefinirse, sin
problemas.
Cada valor es una expresión y su contexto, el de los parámetros de la función; dicho de otro
modo, desde la solapa de parámetros o parámetros interactivos podemos pasarle uno de estos
a la función, y luego, utilizarlo como parámetro de invocación del web service. En este caso, le
indicamos la factura en edición.

Con este atributo podemos determinar si esperamos la respuesta de una instancia completa del
web service, o si solo nos interesa un atributo, en cuyo caso deberíamos especificar cuál. La
respuesta de la función será la respuesta del web service.

Por último, solo veremos estos dos atributos cuando el servicio esté configurado para obtener
token y nos permitan definir la manera de obtenerlo y su tiempo de expiración.


#### 3.11.2 Consumo de Dispositivo

```
Los parámetros de invocación a presentar por cada comando, se obtienen de los controladores
que el usuario haya seleccionado en la Función. Los valores de los Parámetros de invocación que
se hayan definido en el Controlador se presentarán al usuario, quién podrá modificarlos, en caso
de ser necesario.
Propiedades a completar cuando la función sea de tipo Consumo de dispositivo:
✓ Tipo de dispositivo. Indica el Tipo de dispositivo para el cual aplicará la función.
✓ Origen de dispositivo : Define cómo obtener el dispositivo que se va a consumir cuando se
invoque la función. Las opciones disponibles son:
o Dispositivo fijo. Cuando se invoque la función, se consumirá el dispositivo
seleccionado en el atributo “Dispositivo”.
▪ Dispositivo. Define el dispositivo a consumir.
```
```
o Dispositivo predeterminado. Determina que cuando se invoque la función, se debe
consumir un Dispositivo predeterminado, de acuerdo a la configuración establecida
en el atributo Tipo de dispositivo predeterminado , el cual a su vez permite
seleccionar una de las siguientes opciones:
```
- Predeterminado del Usuario autenticado
- Predeterminado del Sitio
- Predeterminado del Dominio

```
o Expresión. Cuando se invoque la función, se evaluará la expresión ingresada en el
atributo “Expresión de dispositivo” para obtener el dispositivo a consumir.
▪ Expresión de dispositivo : Expresión a evaluar para obtener el dispositivo a
consumir.
✓ Controladores
El usuario puede seleccionar un conjunto de controladores, entre todos los existentes para
el Tipo de dispositivo seleccionado en la Función. Si el Origen de dispositivo es “Dispositivo
fijo”, se valida que el usuario haya seleccionado un único Controlador.
Por cada Controlador seleccionado se debe configurar:
```
- **Comando.** Indica el Comando que se va a ejecutar cuando se invoque la función.
- **Parámetros de invocación del comando.** El sistema presenta los Bloques de tipo “Carga
    útil” que estén definidos en el Controlador y el conjunto de Atributos que lo conforman.
    Si en el Controlador se definió una expresión sin contexto (unbound) en el atributo
    Valor, la misma es presentada al usuario, quien si lo desea puede modificarla.:
       o **Parámetro.** Referencia a la carga útil del Parámetro de invocación del
          comando del controlador. Este valor no se puede editar.
       o **Tipo de atributo.** Referencia al tipo de atributo utilizado en cada ítem de la
          carga útil de comando. Este valor no se puede editar.
       o **Requerido.** Indica si el ítem es requerido en la carga útil del comando. Este
          valor no se puede editar.
       o **Valor.** Valor que se enviará en la carga útil del comando cuando se consuma el
          dispositivo.
       o **Condición.**

### 3.12 Definición de Seguridad

La solapa **Seguridad** funciona de acuerdo a lo explicado en el documento de Estándares de Interfaz de
Usuario, en la sección “Características de seguridad”.

Las opciones de seguridad para el _Editor de funciones_ se detallan a continuación:

✓ **Crear función:** Indica los usuarios o grupos de usuarios que pueden crear _Funciones._ Solo se está
disponible para configurar en el dominio o modelo, no en cada función.
✓ **Consulta función:** Indica los usuarios o grupos de usuarios que pueden consultar una _Función._
✓ **Modificar Función** : Indica los usuarios o grupos de usuarios que pueden modificar cualquier parte de
la definición de la _Función_.


✓ **Eliminar Función** : Indica los usuarios o grupos de usuarios que pueden eliminar la _Función_.
✓ **Restaurar función:** Indica los usuarios o grupos de usuarios que pueden restaurar una _Función_
eliminada.
✓ **Traducir función:** Indica los usuarios o grupos de usuarios que pueden traducir las propiedades
internacionalizables de una _Función_.
✓ **Administrar permisos de la función:** Indica los usuarios o grupos de usuarios que pueden administrar
permisos ( **consultar** o **modificar** ) de una _Función_.

En forma predeterminada estarán otorgados todos los permisos para todos los usuarios.

## Anexo I: Funciones del sistema

Se puede consultar la ayuda de todas las funciones del sistema, mirando la descripción y
documentación de la misma, abriendo el elemento desde el acordeón.

### Texto

#### Longitud(Texto)

Devuelve el número entero de caracteres de una cadena de texto.

**Ejemplos:**
Longitud (‘Argentina ́) retorna 9 // LENGTH('CANDIDE') retorna 7.

#### Encontrar(Texto1, Texto2, Posición inicial)

Busca el texto Texto 2 dentro de Texto1. Opcionalmente, se puede definir un número de posiciones desde
el cual comenzar a buscar. Si es negativo, indica desde cuál posición comenzar a buscar contando desde
el final de la cadena. El valor de retorno corresponde a la posición donde se encuentra la sub-cadena (no
a la cantidad de ocurrencias). Equivalente a LOCATE(str1, str2,[number]). El valor de retorno corresponde
siempre a la posición relativa al comienzo de la cadena, no relativa al tercer parámetro. La primera
posición del texto es 1. Retorna 0 si no encuentra Texto2.

**Ejemplos:**

Encontrar('Neuralsoft Neuralsoft Neuralsoft';'soft';1) retorna 7

Encontrar('Neuralsoft Neuralsoft Neuralsoft';'soft'; 10 ) retorna 18, corresponde a la posición de la 2da vez
que está escrito soft.


Encontrar('Neuralsoft Neuralsoft Neuralsoft';'soft'; 20 ) retorna 29, corresponde a la posición de la 3era
vez que está escrito soft.

#### Sustituir(Texto, Texto Buscado, Texto Nuevo)

Sustituye texto nuevo por texto antiguo en una cadena de texto. Sustituye todas las ocurrencias que
encuentra del texto antiguo, por el texto nuevo. Equivalente a REPLACE(original-string, search-string,
replace-string) = STR_REPLACE(originalstr, searchstr, replacestr).

**Ejemplos:**

Sustituir("cdefghi";"def";"yyy") retorna “cyyyghi”.

Sustituir('AIRBUS 150';'AIRBUS';'AB') retorna “AB 150”

#### Reemplazar(Texto, Número inicial, Número de caracteres, Texto nuevo)

Elimina un número de caracteres enteros dados de una cadena que comienzan en una posición específica
y los sustituye con otra cadena. Equivalente a STUFF(string1, start, length, string2).

**Ejemplos:**

Reemplazar('chocolate cake'; 11 ; 4 ; 'pie') retorna 'chocolate pie'

#### Repetir(Texto, Número)

Repite el texto un número entero determinado de veces. Equivalente a REPEAT(string, number) =
REPLICATE(string, number).

**Ejemplos:**
Repetir('Neural';3) Retorna “NeuralNeuralNeural”

#### Minúscula(Texto)

Pone el texto en minúsculas. Equivalente a LOWER(str) = LCASE(str).

**Ejemplos:**
Minúscula("NeuralSoft") retorna neuralsoft
Minúscula('NEURALSOFT') retorna neuralsoft
Minúscula('neuralsoft') retorna neuralsoft

#### Mayúscula(Texto)

Pone el texto en mayúsculas. Equivalente a UPPER(s) = UCASE(str)
**Ejemplos:**
Mayúscula("NeuralSoft") retorna NEURALSOFT

#### Nombre propio(Texto)

Pone en mayúscula la primera letra de cada palabra de un valor de texto.

**Ejemplos:**
Nombre propio(“neuralsoft mirando hacia el futuro”) retorna “Neuralsoft Mirando Hacia El Futuro”

#### Primeros(Texto, Número de caracteres)

Devuelve los primeros caracteres de un texto. Equivalente a LEFT(str, number).

**Ejemplos:**
Primeros(“Neuralsoft”;6) retorna “Neural”

#### Últimos(Texto, Número De Caracteres)

Devuelve los últimos caracteres de un texto. Equivalente a RIGHT(str, number)

**Ejemplos:**
Últimos(‘Neuralsoft’;4) retorna “soft”


#### Extraer(Texto, Posición, Número de caracteres)

Devuelve un número específico de caracteres de una cadena de texto que comienza en la posición que se
especifique. Equivalente a SUBSTRING (cadena, posición, [longitud]).

**Ejemplos:**
Extraer(‘Neuralsoft’;6;5) Retorna “lsoft”

#### Similar(Texto1,Texto2)

Compara dos cadenas, evalúa la similitud entre ellas, y devuelve un valor entero de 0 a 100. Cuanto más
se parecen, mayor es el número.

**Ejemplos:**
SIMILAR('toast', 'coast') retorna 75.

#### Quitar espacios(Texto)

Elimina espacios en blanco iniciales, finales y en medio de un texto. Equivalente a TRIM(str)

**Ejemplos:**
Quitar espacios (“ Neuralsoft. Mirando hacia el futuro ”) retorna “Neuralsoft.Mirandohaciaelfuturo”

#### Quitar espacios iniciales(Texto)

Elimina todos los espacios en blanco del comienzo del texto. Equivalente a LTRIM(str).

**Ejemplos:**
Quitar espacios iniciales(“ Neuralsoft. Mirando hacia el futuro ”) retorna “Neuralsoft. Mirando hacia
el futuro ”

#### Quitar espacios finales(Texto)

Elimina todos los espacios en blanco del final del texto. Equivalente a RTRIM(str).

**Ejemplos:**
Quitar espacios finales(“ Neuralsoft. Mirando hacia el futuro ”) retorna “ Neuralsoft. Mirando
hacia el futuro”

#### Comparar JSON(JSON origen, JSON a comparar)

Realiza la comparación entre dos JSON, retornando la diferencia entre ellos.

- La comparación se realiza mediante la utilización de una clave para cada nivel del JSON. Esto permite
identificar unívocamente donde estuvo la diferencia al momento de realizar la comparación.
Para la definición de claves, se utiliza a nivel entidad aquello que el usuario haya definido como valores
únicos en la colección de valores únicos de la entidad, en caso de haber definido más de una, se asume la
primera de ellas. A nivel colección se utiliza el identificador de ítem generado automáticamente en Fastprg
para cada uno de ellos.

#### Existe carácter especial (Texto)

Realiza la búsqueda de caracteres especiales dentro del texto recibido por parámetro y retorna un valor
booleano.
En el caso que exista carácter especial, la función retorna verdadero, caso contrario retorna falso.
Se entiende como carácter especial a cualquier letra que no se encuentre en el rango [a-z], [A-Z] o [0-9].
Entre dichos caracteres se incluyen: ñ,á,é,í,ó y ú.

**Ejemplos:**
Existe carácter especial('123abcd é') retorna Verdadero
Existe carácter especial('123abcd ') retorna Falso


#### Palabra sin caracteres especiales(Texto)

Busca caracteres especiales dentro de una cadena y en el caso que la cadena contenga uno o más
caracteres retorna una cadena vacía, de lo contrario retorna la misma cadena que fue recibida por
parámetro.
Se entiende como carácter especial a cualquier letra que no se encuentre en el rango [a-z], [A-Z] o [0-9].
Entre dichos caracteres se incluyen: ñ,á,é,í,ó y ú, espacio en blanco, entre otros.

**Ejemplos:**
Palabra sin caracteres especiales('123abcd') retorna '123abcd'
Palabra sin caracteres especiales('123abcd é') retorna ''

#### Obtener Traducción (Texto internacionalizable, Idioma)

Devuelve un texto en un idioma específico a partir de un texto con características de
internacionalización. El texto recibido podrá ser plano, enriquecido o internacionalizable. El valor del
parámetro Idioma sólo aceptará literales de los idiomas configurados en el dominio.

**Ejemplos:**

Suponiendo que tenemos un atributo de tipo texto internacionalizable llamado _texto a traducir_ que
contiene el valor hola.

Obtener traducción(texto a traducir;'es') retorna hola

Obtener traducción(texto a traducir;'en') retorna hello

#### Obtener Traducción de texto enriquecido (Texto enriquecido internacionalizable, Idioma)

Devuelve un texto enriquecido en un idioma específico a partir de un texto enriquecido con
características de internacionalización. El valor del parámetro Idioma sólo aceptará literales de los
idiomas configurados en el dominio.

**Ejemplos:**

Suponiendo que tenemos un atributo de tipo texto enriquecido internacionalizable llamado _texto a
traducir_ que contiene el valor **hola**.

Obtener traducción(texto a traducir;'es') retorna **hola**

Obtener traducción(texto a traducir;'en') retorna **hello**

#### Obtener Traducción de texto multimedia (Texto multimedia internacionalizable, Idioma)

Devuelve un texto multimedia en un idioma específico a partir de un texto multimedia con
características de internacionalización. El valor del parámetro Idioma sólo aceptará literales de los
idiomas configurados en el dominio.

**Ejemplos:**

Suponiendo que tenemos un atributo de tipo texto multimedia internacionalizable llamado _texto a
traducir_ que contiene el valor hola ֎ꙮꚙ.

Obtener traducción(texto a traducir;'es') retorna hola ֎ꙮꚙ

Obtener traducción(texto a traducir;'en') retorna hello ֎ꙮꚙ

#### Traducir Texto a Idiomas(Texto, Idioma de origen)

Dado un texto en un idioma, devuelve las traducciones a todos los idiomas de la aplicación (retorna
texto i18n). El texto recibido podrá ser plano, enriquecido o internacionalizable.

**Ejemplos:**


Suponiendo que tenemos un texto en un idioma y queremos asignarlo en un atributo de tipo texto
internacionalizable, es necesario usar esta función. Por ej: Traducir texto a idiomas(“hola”;”es”)
mostraría un texto con el valor hola, y en el diccionario de traducciones, para inglés queda “hello”. Si
en el dominio hubiese otros idiomas, también se obtendrían las traducciones de los mismos.

#### Traducciones pendientes (texto internacionalizable)

Al recibir un atributo de tipo internacionalizable, indica si el mismo tiene pendiente de aprobar alguna
traducción.
Esto permite a un traductor ingresar a un GDI para poder visualizar si existen traducciones pendientes
para ajustarlas. Por el momento la definición es que se puedan volcar a un GDI las entidades a revisar y
en base a esto se muestren los pendiente, no está en el alcance del requerimiento actual tener un lugar
centralizado que indique todas las traducciones pendientes del sistema

#### Sin traducir(Texto)

Dado un texto sin características de internacionalización, la función devuelve un texto con características
de internacionalización, considerando que el texto ingresado no se traduce y se agrega como traducción
en todos los idiomas disponibles.

**Ejemplos:**
Sin traducir(“URL”) retorna URL con ese valor para todos los idiomas.

### Fecha hora

#### Ahora()

Devuelve la fecha y hora actuales.

**Ejemplos:**
Ahora() retorna 16/08/2023 10:46

#### Hoy()

Devuelve la fecha actual (sin hora).

**Ejemplos:**
Hoy() retorna 16/08/2023

#### Día(Fecha)

Devuelve el día del mes para una fecha dada. Retorna número entre 1 y 31. Se le puede enviar un dato
tipo fecha, fecha/hora o instante.

**Ejemplos:**
Día({16/08/2023 11:00}) retorna 16

#### Día de semana(Fecha)

Devuelve el día de la semana para una fecha dada. No contempla la configuración regional, para Domingo
retorna siempre 1, para Lunes retorna 2, etcétera. Se le puede enviar un dato tipo fecha, fecha/hora o
instante.

**Ejemplos:**
Día de semana({16/08/2023 11:00}) retorna 4

#### Ultimo día del mes(Fecha)

Devuelve la fecha correspondiente al último día del mes para una fecha dada.

**Ejemplos:**


Ultimo día del mes(Hoy()) retorna 3 0 /0 9 /2023

#### Hora(Fecha)

Devuelve la hora de una fecha dada, en el rango de 0 a 23. Se le puede enviar un dato tipo fecha,
fecha/hora o instante.

**Ejemplos:**
Hora({16/08/2023 11:40}) retorna 11

#### Minutos(Fecha)

Devuelve los minutos de una fecha/hora dada, en el rango de 0 a 59. Se le puede enviar un dato tipo
fecha, fecha/hora o instante.

**Ejemplos:**
Minutos({16/08/2023 11:40}) retorna 40

#### Segundos(Fecha)

Devuelve los segundos de una fecha/hora, en el rango de 0 a 59. Se le puede enviar un dato tipo fecha,
fecha/hora o instante.

**Ejemplos:**
Segundos({16/08/2023 11:40 }) retorna 0

#### Mes(Fecha)

Devuelve el mes para una fecha dada. Retorna número entre 1 y 12. Se le puede enviar un dato tipo fecha,
fecha/hora o instante.

**Ejemplos:**
Mes({16/08/2023 11:40 }) retorna 8

#### Año(Fecha)

Devuelve el año para una fecha dada. Se le puede enviar un dato tipo fecha, fecha/hora o instante.

**Ejemplos:**
Año({16/08/2023 11:40 }) retorna 2023

#### Semestre(Fecha)

Devuelve el semestre del año para la fecha, en el rango de 1 a 2. Se le puede enviar un dato tipo fecha,
fecha/hora o instante.

**Ejemplos:**
Semestre({16/08/2023 11:40 }) retorna 2

#### Cuatrimestre(Fecha)

Devuelve el trimestre del año para la fecha, en el rango de 1 a 3. Se le puede enviar un dato tipo fecha,
fecha/hora o instante.

**Ejemplos:**
Cuatrimestre({16/08/2023 11:40 }) retorna 2

#### Trimestre(Fecha)

Devuelve el trimestre del año para la fecha, en el rango de 1 a 4. Se le puede enviar un dato tipo fecha,
fecha/hora o instante.

**Ejemplos:**
Trimestre({16/08/2023 11:40 }) retorna 3


#### Bimestre(Fecha)

Devuelve el trimestre del año para la fecha, en el rango de 1 a 6. Se le puede enviar un dato tipo fecha,
fecha/hora o instante.

**Ejemplos:**
Bimestre({16/08/2023 11:40 }) retorna 4

#### Quincena(Fecha)

Devuelve la quincena del año para la fecha, en el rango de 1 a 24. Se le puede enviar un dato tipo fecha,
fecha/hora o instante.

**Ejemplos:**
Quincena({16/08/2023 11:40 }) retorna 16

#### Semana(Fecha)

Devuelve la semana del año aplicando el standard ISO 8601, en el rango de 1 a 53, contando al Lunes
como primer día de la semana. Se le puede enviar un dato tipo fecha, fecha/hora o instante.

**Ejemplos:**
Semana({28/12/2025 11:40 }) retorna 52
Semana({ 29 /12/2025 11:40 }) retorna 1
Semana({04/01/2026 11:40 }) retorna 1
Semana({ 05 /01/2026 11:40 }) retorna 2

#### Año de la semana (Fecha)

Dada una Fecha o Fecha hora devuelva el Año al cual pertenece su Semana. El resultado no siempre
será igual al Año de la Fecha o Fecha hora que se pasa como parámetro.
**Ejemplos:**

#### Convertir Zona Horaria(Fecha hora, Zona Horaria)

Convierte una fecha-hora en una zona horaria a otra zona horaria determinada.

**Ejemplos:**
Convertir zona horaria(Ahora();"Europe/Madrid")

#### Considerar Zona Horaria (Fecha hora)

Fuerza a considerar la zona horaria de una fecha.
Si Fecha Venta = {06/06/2016 15:45 GMT -3}, al utilizar el atributo Fecha Venta en cualquier expresión se
tendrá en cuenta la siguiente fecha: {06/06/2016 15:45} (sin zona horaria) Pero la siguiente función:
Considerar Zona Horaria (Fecha Vencimiento) devuelve {06/06/2016 15:45 GMT -3} (con zona horaria).

**Ejemplos:**
Considerar Zona Horaria (Ahora()) Retorna {16/08/2023 11:28 GMT -3}

#### Calcular feriados(Fecha inicio, Fecha fin, Calendario de trabajo)

Devuelve la cantidad de feriados entre dos fechas estipuladas. Valor de retorno: Cantidad de feriados.

**Ejemplos:**
Calcular feriados({09/03/2023};{ 14 /03/2023};(en Calendario de trabajo primer Esta instancia cuando
Obtener traducción(Nombre;'es') = 'Calendario estándar')) Retorna: 0

Calcular feriados({09/03/2023};{31/03/2023};(en Calendario de trabajo primer Esta instancia cuando
Obtener traducción(Nombre;'es') = 'Calendario estándar')) Retorna: 1


#### Calcular Fecha(Fecha, Cantidad de días hábiles, Calendario)

Suma una determinada cantidad de días hábiles a una fecha, teniendo en cuenta un calendario dado.
Nota: Se tienen en cuenta las horas disponibles y la cantidad de días se multiplica por 24.

**Ejemplos:**

Se tiene un calendario de media jornada con horario de 4 horas diarias de lunes a viernes.

A partir de una fecha dada, se calcula la fecha para 1 día (equivalente a 24hs). Entonces, se consideran
6 días hábiles (lunes a viernes, excluyendo feriados) y se obtiene la fecha calculada.

Ahora bien, la misma cantidad de días, en una fecha donde hay feriados, queda de la siguiente manera:


#### Calcular Fecha Hora (Fecha Hora, Cantidad de días hábiles, Calendario)

Suma una determinada cantidad de días hábiles a una fecha hora, teniendo en cuenta un calendario
dado. Equivalente a Calcular fecha pero considerando las horas.

**Ejemplos:**

Siguiendo los ejemplos vistos en la función anterior.

#### Disponibilidad fecha(Fecha inicio, Fecha fin, Calendario de trabajo)

Esta función devuelve la duración calculada sumando dos fechas.

**Ejemplos:**
Siguiendo con los mismos ejemplos de las funciones anteriores, tenemos:

#### Disponibilidad fecha hora(Fecha inicio, Fecha fin, Calendario de trabajo)

Esta función devuelve la duración calculada sumando dos fecha hora.

**Ejemplos:**
Siguiendo con los mismos ejemplos de las funciones anteriores, tenemos:


#### Nueva fecha(Año, Mes, Día)

Esta función construye una fecha, a partir de un año, mes y día que recibe como parámetros.

**Ejemplos:**

#### Nueva hora(Colección, Atributo, Condición)

Esta función construye un dato tipo hora, a partir de los parámetros recibidos correspondientes a la
hora, los minutos y los segundos.

**Ejemplos:**

### Colección

#### Contar(Colección, Atributo, Condición)

Devuelve la cantidad de elementos de la colección. Si no hay elementos en la colección, devuelve null.

**Ejemplos:**
Contar(Factura.Items de comprobante;Total; Total > 500)
Se traduce automáticamente en:
en Factura.Items de comprobante contar Total cuando Total > 500

#### Buscar(Colección o Entidad, [Atributos], [Condición], [Ordenar], [Desde almacén])

Devuelve una colección que contiene solo los elementos que cumplen con la condición. Si no hay
elementos en la colección, devuelve null.

**Ejemplos:**


Buscar(Factura; Importe total > 100 Y Cliente.Nombre CONTIENE “Pedro” Y Cliente.Limite de crédito >
100)

Al ingresar dicha función, se traduce a:
En Factura Buscar Esta instancia Cuando Importe total > 100 Y Cliente.Nombre CONTIENE “Pedro” Y
Cliente.Limite de crédito > 100

Buscar(Factura.Items de comprobante;Total; Total > 500)

#### Sumar(Colección, Atributo, Condición)

Devuelve la suma de los elementos de la colección. Si no hay elementos en la colección, devuelve null.

**Ejemplos:**
Sumar(Factura.Items de comprobante;Total; Total > 500)
Se traduce automáticamente en:
en Factura.Items de comprobante sumar Total cuando Total > 500

#### Mínimo(Colección, Atributo, Condición)

Devuelve el menor elemento de la colección. Si no hay elementos en la colección, devuelve null.

**Ejemplos:**
Mínimo(Factura.Items de comprobante;Total; Total > 500)
Se traduce automáticamente en:
en Factura.Items de comprobante mínimo Total cuando Total > 500

#### Máximo(Colección, Atributo, Condición)

Devuelve el mayor elemento de la colección. Si no hay elementos en la colección, devuelve null.

**Ejemplos:**
Máximo(Factura.Items de comprobante;Total; Total > 500)
Se traduce automáticamente en:
en Factura.Items de comprobante máximo Total cuando Total > 500

#### Promedio(Colección, Atributo, Condición)

Devuelve el promedio de los elementos de la colección. Si no hay elementos en la colección, devuelve
null.

**Ejemplos:**
Promedio(Factura.Items de comprobante;Total; Total > 500)
Se traduce automáticamente en:
en Factura.Items de comprobante promedio Total cuando Total > 500

#### Desviación Estándar(Colección, Atributo, Condición)

Devuelve el desvío estándar de los elementos de la colección.

**Ejemplos:**
Desviación estándar(Factura.Items de comprobante;Total; Total > 500)
Se traduce automáticamente en:
en Factura.Items de comprobante desvío estándar Total cuando Total > 500

#### Varianza(Colección, Atributo, Condición)

Devuelve la varianza de un conjunto de números.

**Ejemplos:**
Varianza(Factura.Items de comprobante;Total; Total > 500)


Se traduce automáticamente en:
en Factura.Items de comprobante varianza Total cuando Total > 500

#### Ordenar(Colección, Atributo1 ASC Atributo2 DESC)

Ordena los elementos de la colección según el orden (ASC o DESC) y los atributos indicados.

**Ejemplos:**
Ordenar (Factura.Items de comprobante;Total ASC)

#### Distintos(Colección.Atributo)

Devuelve una colección en la cual no hay elementos duplicados

**Ejemplos:**
Distintos (Factura.Items de comprobante;Producto)

#### Primer(Entidad/Colección, Atributo, [Condición], [Ordenar], [Desde almacén])

Devuelve el primer elemento de una colección.

**Ejemplos:**
Primer(Factura.Items de comprobante;Total; Total > 500;Total DESC)
Se traduce automáticamente en:
en Factura.Items de comprobante primer Total cuando Total > 500 Ordenar Total DESC

#### Último(Entidad/Colección, Atributo, [Condición], [Ordenar], [Desde almacén])

Devuelve el último elemento de una colección.

**Ejemplos:**
Último(Factura.Items de comprobante;Total; Total > 500;Total DESC)
Se traduce automáticamente en:
en Factura.Items de comprobante Último Total cuando Total > 500 Ordenar Total DESC

#### Consultar(Entidad, Atributo, Colección)

Permite indicar implícitamente al algoritmo que no deber realizar producto cartesiano, sino que intenta
completar el atributo de la instancia en curso.
Hay que pasar una entidad, un atributo de esa entidad, y una colección. Los ítems de esa colección tienen
que tener el mismo tipo (o compatible) que el atributo. Retorna una colección de referencias a la entidad.
**Ejemplo:**
Se desea completar con una colección que proviene de un WS con la siguiente estructura:
Listas de precios
Código
Versión
Nombre
Código moneda
La entidad Fast que tiene la siguiente estructura (y del lado derecho se indica como deberá completarse
la definición de valores

```
Definición de valores Fast Expresiones con resultado de WS
Código (Entero) Lista de precios.Código
Versión (Entero) Lista de precios.Versión
```

```
Nombre (Texto) Lista de precios.Nombre
Moneda (Referencia a entidad Moneda) CONSULTAR(Moneda,código,Lista de precios.Código moneda)
```
Donde moneda es otra entidad Fast que posee un atributo código.
Al realizar la función/ operador consultar, el sistema deberá conservar el id de la instancia que se está
intentando completar y de esta manera el algoritmo no debería realizar el producto cartesiano, sino que
solo debería completar el atributo referencia a moneda.

#### Obtener rangos de logro( Json)

Esta función recibe un texto en formato JSON y devuelve una colección de rangos de logro. Su objetivo
es poder decodificar los rangos de logro almacenados en los acumuladores en formato Json y devolver
una colección de rangos de logro que será utilizada por "Interfaz de usuario" como parte de la
información necesaria para mostrar los gráficos con el desempeño de los objetivos.

### Matemática

#### Valor absoluto(Número)

Devuelve el valor absoluto de un número.

**Ejemplos:**
Valor absoluto(123,4 5 ) retorna 123,45
Valor absoluto(-123,4 5 ) retorna 123,45

#### Redondear(Número, Dígitos)

Redondea un número al número de dígitos especificado. El número de dígitos especificado puede ser
positivo (después de la coma o punto decimal) o negativo (antes de la coma o punto decimal).

**Ejemplos:**
Redondear(123,45;1) retorna 123,40
Redondear((- 123,45);1) retorna -123,40
Redondear(123; -2) = 100
Redondear(182; -2) = 200

#### Piso(Número)

Devuelve el primer número entero igual o menor que el número real enviado por parámetro. O sea
devuelve el entero más próximo por defecto. (Ej: Piso(-2,4) devuelve el valor -3; Piso(1,5) devuelve al valor
1).

**Ejemplos:**
Piso(123,45) retorna 123.
Piso(- 123 ,45) retorna -124.

#### Techo(Número)

Devuelve el primer número entero mayor o igual que el número real enviado por parámetro. O sea
devuelve el entero más próximo por exceso. (Ej: Techo(-2,4) devuelve valor -2; Techo(1,5) devuelve el
valor 2).

**Ejemplos:**
TECHO(123,45) retorna 124.
TECHO (- 123 ,45) retorna -123.


#### Truncar(Número, Dígitos)

Trunca un número a la cantidad de dígitos especificada. El número de dígitos especificado puede ser
positivo (después de la coma o punto decimal) o negativo (antes de la coma o punto decimal).

**Ejemplos:**
TRUNCAR(655; - 2) retorna 600.
TRUNCAR(655, 348 ; 2) retorna 655,340.

#### Factorial(Número)

Devuelve el factorial de un número.

**Ejemplos:**
Factorial(5) retorna 120

#### Doble factorial(Número)

Devuelve el doble factorial de un número. EL producto de todos los enteros desde el 1 hasta un entero
no-negativo n que tiene la misma paridad (pares o impares) que n.

**Ejemplos:**
Doble Factorial(5) retorna 15 (5*3*1)
Doble Factorial(6) retorna 48 (6*4*2)

#### Logaritmo natural(Número)

Devuelve el logaritmo natural (neperiano) de un número.

**Ejemplos:**
Logaritmo natural(123) retorna 4,8158362157...
Logaritmo natural(1) retorna 0

#### Logaritmo decimal(Número)

Devuelve el logaritmo en base 10 de un número.

**Ejemplos:**
Logaritmo decimal(100) retorna 2
Logaritmo decimal(1) retorna 0

#### Número Pi()

Devuelve el valor de pi.

**Ejemplos:**
Número Pi() retorna 3,1415926...

#### Potencia(Número, Potencia)

Devuelve el resultado de elevar un número a una potencia.

**Ejemplos:**
Potencia(9;2) retorna 81
Potencia( 3 ; 3 ) retorna 27
Potencia(5;4) retorna 625

#### Aleatorio()

Devuelve un número aleatorio entre 0 y 1.

**Ejemplos:**
Aleatorio() retorna una vez: 0,633892747... luego 0,780470475... luego 0,554040673...


#### Aleatorio con límite(Límite inferior, Límite superior )

Devuelve un número decimal aleatorio entre el Limite inferior y el Límite superior.

**Ejemplos:**
Aleatorio con límite(0;100) retorna 55; luego 48; luego 37

#### Raíz cuadrada(Número)

Devuelve la raíz cuadrada positiva de un número.

**Ejemplos:**
Raíz cuadrada (9) retorna 3.
Raíz cuadrada (144,240100) retorna 12,01.

#### Raíz(Número; Índice)

Devuelve la raíz del índice de un número.

**Ejemplos:**
Raíz(27;3) retorna 3

### Trigonométrica

#### Arcocoseno(Número)

Devuelve el arcocoseno de un número.

**Ejemplos:**
Arcocoseno( 0 ) retorna 1,57079632
Arcocoseno( 1 ) retorna 0

#### Arcoseno(Número)

Devuelve el arcoseno de un número.

**Ejemplos:**
Arcoseno( 0 ) retorna 0
Arcoseno( 1 ) retorna 1,57079632

#### Arcotangente(Número)

Devuelve la arcotangente de un número.

**Ejemplos:**
Arcotangente ( 0 ) retorna 0
Arcotangente ( 1 ) retorna 0,78539816

#### Arcotangente coordenadas( X, Y )

Devuelve la arcotangente de las coordenadas "x" e "y".

**Ejemplos:**
Arcotangente coordenadas (0;5) retorna 0
Arcotangente coordenadas (1;4) retorna 0,24497866

#### Coseno(Número)

Devuelve el coseno de un número.

**Ejemplos:**
Coseno ( 0 ) retorna 1
Coseno ( 1 ) retorna 0,54030230


#### Cotangente(Número)

Devuelve la cotangente expresada en radianes de un ángulo, también expresado en radianes.

**Ejemplos:**
Cotangente ( 1 ) retorna 0,64209261
Cotangente ( 100 )retorna -1,70295691

#### Grados(Número)

Convierte radianes en grados.

**Ejemplos:**
Grados(0) retorna 0
Grados(1) retorna 57,29577951

#### Radianes(Número)

Convierte grados en radianes.

**Ejemplos:**
Radianes (0) retorna 0
Radianes (1) retorna 0,01745329
Radianes(57,2958) retorna 1

#### Seno(Número)

Devuelve el seno (en radianes) de un ángulo determinado (en radianes).

**Ejemplos:**
Seno (0) retorna 0
Seno (1) retorna 0,84147098

#### Tangente(Número)

Devuelve la tangente de un número.

**Ejemplos:**
Tangente (0) retorna 0
Tangente (1) retorna 1,55740772

### Conversión

#### Es Fecha (Texto, Máscara)

Comprueba si un texto se puede convertir a una fecha, considerando la máscara (se debe utilizar
formato mediano). Si la conversión es posible, la función devuelve verdadero; si no, falso. Si el
argumento es nulo, devuelve falso.

**Ejemplos:**

Es fecha(‘25/10/2022’;’dd/MM/yyyy’) retorna verdadero

Es fecha(‘25/10/22’;’dd/MM/yyyy’) retorna falso

Es fecha(‘35/10/2022’;’dd/MM/yyyy’) retorna falso

Es fecha(‘25/40/2022’;’dd/MM/yyyy’) retorna falso

#### Es Numérico (Texto, Idioma)

Comprueba si un texto se puede convertir a un número, considerando el idioma y la configuración
regional para el separador decimal. El valor del parámetro Idioma sólo aceptará literales. Si la
conversión es posible, la función devuelve verdadero; si no, falso. Si el argumento es nulo, devuelve
falso.

**Ejemplos:**


Es número(“123”;”es”) retorna verdadero

#### Texto a Número (Texto)

Convierte y devuelve en formato numérico el texto enviado como parámetro. Esta función sólo acepta
un texto con un solo separador o ninguno, y este separador es el que se toma como separador decimal.

**Ejemplos:**

Texto a Número (“101,104) devuelve el número 101.104

Texto a Número (“123456.123”) devuelve el número 123456.123

Texto a Número (“102;102222”) da error

Texto a Número (“102.102.222”) da error.

#### Número a Texto (Número)

Convierte el número enviado como parámetro en formato texto.

**Ejemplos:**

Número a texto(325,222) retorna ‘325.222’

#### Número a palabra (Número)

Conversión de número a texto escrito internacionalizable. Devuelve texto internacionalizable, es decir,
el texto en todos los idiomas de los datos de la aplicación. Tener presente que, en caso de enviar un
valor negativo, se debe agregar la palabra “Menos” (en cada idioma correspondiente) indicando que el
valor es negativo. En caso de no desear este valor, un modelador debe utilizar la función valor absoluto,
enviando un valor positivo a la función y así no retorna esta palabra “Menos”

**Ejemplos:**

Número a palabra (101) devuelve “ciento uno”, “one hundred and one”, “centouno”, etc.

Número a palabra (12547,24) devuelve “Doce mil quinientos cuarenta y siete con veinticuatro
centavos”, “Twelve thousand five hundred forty seven with twenty four cents”

Número a palabra (-58651,22) devuelve “Menos cincuenta y ocho mil seiscientos cincuenta y uno con
veintidos centavos”, “Negative fifty eight thousand six hundred fifty one with twenty two cents”

#### Fecha a Texto (Fecha, Máscara)

Convierte una fecha en un texto en base a una máscara.

**Ejemplos:**

Fecha a texto ({25/10/2020};"dd/MM/yyyy") retorna "25/10/2020"

Fecha a texto ({ 01 /1 1 / 1977 };"dd/MM/yy") retorna " 01 /1 1 / 77 "

Fecha a texto ({01/11/1977};"MM/dd/yy") retorna "11/01/77"

#### Fecha hora a Texto (Fecha hora, Máscara)

Convierte una fecha hora en un texto en base a una máscara.

**Ejemplos:**

Fecha hora a texto ({25/10/2020 23:5 1 };"dd/MM/yyyy HH:mm:ss") retorna "25/10/2020 23:5 1 : 00 "

Fecha hora a texto ({08/09/2023 10:04};"dd/MM/yyyy HH:mm") retorna "08/09/2023 10:04"

Fecha hora a texto (Ahora();"dd/MM/yyyy HH:mm:ss") retorna "08/09/2023 10:04:26"

#### Texto a Fecha hora (Texto, Máscara)

Convierte un texto en una fecha y hora escrita en base a una máscara.

**Ejemplos:**


Texto a fecha hora ("29/12/2020 23:59:58","dd/MM/yyyy HH:mm:ss") retorna {29/12/2020 23:59:58}

Texto a fecha hora ("01/11/20 20:02”; “dd/MM/yy HH:mm”) retorna {01/11/2020 20:02}

#### Texto a Fecha (Texto, Máscara)

Convierte un texto en una fecha escrita en base a una máscara.

**Ejemplos:**

Texto a fecha ("29/12/2020","dd/MM/yyyy") retorna {29/12/2020}

Texto a fecha ("13/09/23","dd/MM/yy") retorna {13/09/2023}

#### Fecha a Fecha hora

Convierte una fecha en una fecha y hora escrita.

**Ejemplos:**

Fecha a Fecha hora({25/10/2019}) retorna {25/10/2019 00:00:00}

Fecha a Fecha hora(Hoy()) retorna { 08 / 09 /20 23 00:00:00}

#### Fecha hora a Fecha (Fecha hora, Máscara)

Esta función recibe un dato fecha y hora y lo convierte a solo fecha. Puede recibir por parámetro un
dato tipo fecha/hora o instante de forma indistinta.

**Ejemplos:**

Fecha hora a fecha ({25/10/2020 23:51}) retorna "25/10/2020"

#### Duración a milisegundos (Duración)

Convierte una duración a un número (sin la unidad). El tipo de dato duración, indica un lapso de tiempo
en una medida determinada.

La medida puede ser: semanas, días, horas, minutos, segundos o milisegundos. Esta función retorna la
cantidad de milisegundos que hay en esa duración.

**Ejemplos:**

Duración a milisegundos ({6 minutos}) devuelve 360000.

Duración a milisegundos ({5 horas}) devuelve 18000000.

Duración a milisegundos ({ 1 día}) devuelve 86400000.

#### Duración a segundos (Duración)

Convierte una duración a un número (sin la unidad). El tipo de dato duración, indica un lapso de tiempo
en una medida determinada. La medida puede ser: semanas, días, horas, minutos, segundos. Esta
función retorna la cantidad de segundos que hay en esa duración.

**Ejemplos:**

Duración a segundos({6 minutos}) devuelve 360

Duración a segundos({2 horas}) devuelve 7200

Duración a segundos({1 día}) devuelve 86400

#### Duración a Minutos (Duración)

Convierte una duración a un número entero (este número es la cantidad de minutos). Solo funciona
para atributos duración que tienen minutos, horas, días y/o semanas.

**Ejemplos:**

Duración a minutos ({1 minuto}) devuelve 1.

Duración a minutos ({6 horas}) devuelve 360.


Duración a minutos ({5 días}) devuelve 7200.

Duración a minutos ({1 semanas}) devuelve 10080.

#### Duración a horas (Duración)

Convierte una duración a un número (sin la unidad). El tipo de dato duración, indica un lapso de tiempo
en una medida determinada. La medida puede ser: semanas, días, horas, minutos, segundos o
milisegundos. Esta función retorna la cantidad de horas que hay en esa duración.

**Ejemplos:**

Duración a horas({15 minutos}) devuelve 0.25

Duración a horas({2 días}) devuelve 48.

Duración a horas({3 semanas}) devuelve 504.

#### Duración a días (Duración)

Convierte una duración a un número (sin la unidad). El tipo de dato duración, indica un lapso de tiempo
en una medida determinada. La medida puede ser: semanas, días, horas, minutos, segundos o
milisegundos. Esta función retorna la cantidad de días que hay en esa duración.

**Ejemplos:**

Duración a días({15 minutos}) devuelve 0,0104

Duración a días ({2 días}) devuelve 2.

Duración a días ({3 semanas}) devuelve 21.

#### Duración a semanas (Duración)

Convierte una duración a un número (sin la unidad). El tipo de dato duración, indica un lapso de tiempo
en una medida determinada. La medida puede ser: semanas, días, horas, minutos, segundos o
milisegundos. Esta función retorna la cantidad de semanas que hay en esa duración.

**Ejemplos:**

Duración a semanas ({5 días}) devuelve 0.714286

Duración a semanas ({9 días}) devuelve 1.2857

#### Duración a meses (Duración)

Convierte una duración a un número (sin la unidad). El tipo de dato duración, indica un lapso de tiempo
en una medida determinada. La medida puede ser: meses o años. Esta función retorna la cantidad de
meses que hay en esa duración.

**Ejemplos:**

Duración a meses ({2 años}) devuelve 24

#### Duración a años (Duración)

Convierte una duración a un número (sin la unidad). El tipo de dato duración, indica un lapso de tiempo
en una medida determinada. La medida puede ser: meses o años. Esta función retorna la cantidad de
años que hay en esa duración.

**Ejemplos:**

Duración a años ({50 meses}) devuelve 4.16667

Duración a años ({5 meses}) devuelve 0.4167

#### Duración a Texto (Duración)

Convierte una duración al formato texto internacionalizable, es decir, el texto en todos los idiomas de
los datos de la aplicación.


**Ejemplos:**

Duración a Texto ({1 minuto}) devuelve “1 minuto” en español, “1 minute” en inglés, etc.

#### Texto enriquecido a Texto(Texto enriquecido)

Devuelve el texto plano sin formato de un texto enriquecido

**Ejemplos:**

Texto enriquecido a Texto(“Este es un texto con formato.
**Negrita.**
_Cursiva_**.**
**_Negrita y cursiva.”)_** retorna **_“_** Este es un texto con formato.Negrita.Cursiva.Negrita y cursiva.”

#### Hipervínculo(Atributo referencia a instancia o atributo ítem de colección)

Genera un link con el nombre de la entidad + los descriptivos de la instancia separados por “,” en todos
los idiomas existentes; por lo tanto se debe utilizar un atributo del tipo Texto internacionalizable para
poder utilizar la función. Es muy importante revisar los descriptivos de la entidad o colección a la que
se hace referencia, para que se muestre el hipervínculo con el valor adecuado. En caso de no estar
definido el descriptivo correctamente, se muestra con un ID.

**Ejemplos:**

Hipervínculo(nombre del atributo que tiene la referencia) retorna el link a la instancia o ítem que
contiene la referencia.

#### Texto a Base64(Texto)

Dada una cadena de texto ilimitada, retorna el mismo tipo de atributo (cadena ilimitada) en base 64.
Base64 es un sistema numérico que se utiliza para transformar cualquier tipo de datos en una larga
cadena de texto plano, para enviar información a través de internet sin poner en riesgo su integridad.
El sistema numérico Base64 utiliza cadenas de seis bits para representar diferentes símbolos.

**Ejemplos:**

Texto a Base64 (“Bienvenidos”) retorna “QmllbnZlbmlkb3M=”


Texto a Base64 (“Neuralsoft”) retorna “TmV1cmFsc29mdA==”

#### Convertir de base64 a blob(Texto)

Dado un tipo de dato base64, retorna un atributo de tipo blob. Invocación:

**Ejemplos:**

Convertir de base64 a blob(“QmllbnZlbmlkb3M=”) genera un archivo de tipo Texto con la metadata:
Bienvenidos

#### Convertir de base64 a archivo(Nombre de archivo, Texto)

Dado un tipo de dato base64, retorna un atributo de tipo blob, permitiendo definir un nombre de
archivo.

**Ejemplos:**

Convertir de base64 a archivo(‘prueba.pdf’; “QmllbnZlbmlkb3M=”) genera un archivo de tipo Texto con
la metadata: Bienvenidos y el nombre del archivo es prueba.pdf

#### Convertir texto o número en duración

Convertir un texto o número en duración.

**Ejemplos:**

#### Colección a texto enriquecido (Colección)

```
Permite convertir un conjunto de ítems de una colección en una lista de elementos de tipo Texto
Enriquecido Internacionalizable.
En esta función podemos utilizar como parámetro de entrada tanto un atributo de tipo Colección
como una expresión de búsqueda “En <Colección> Buscar <Atributo>”, siempre y cuando luego de la
instrucción “En” se indique una Colección, por ejemplo, si se desea obtener la lista de direcciones de
un cliente, éstas pueden obtenerse del siguiente modo En .Domicilios Buscar Dirección.
Adicionalmente, la función admite que se pueda solicitar más de un elemento en la expresión de
búsqueda, para esto, al momento de escribir la expresión se deberán indicar los elementos de la
colección que se desean convertir separándolos con ‘;’, por ejemplo; En .Domicilios Buscar Dirección;
Código postal.
Sintaxis válidas de la función:
```
```
Colección a Texto Enriquecido(<Colección>)
Colección a Texto Enriquecido(En <Colección> Buscar <Atributo>)
Colección a Texto Enriquecido(En <Colección> Buscar <Atributo 1>;<Atributo
2>;<Atributo 3>)
```
Comportamientos:
✓ Si el parámetro de la función es un atributo de tipo Colección, se convertirán todos los atributos de la
misma a Texto Enriquecido. Por otra parte, si el parámetro es una expresión de búsqueda se
convertirán solamente los elementos indicados en la misma.
✓ En los casos en los que los atributos a presentar sean de tipo numérico, la función contemplará los

formatos de cantidad de decimales expresados en el formato visual del atributo.
✓ Si el valor de un atributo que se está convirtiendo es nulo, no se presenta un error y concatena el
separador de elemento.
✓ Si el tipo de atributo de un elemento que se está convirtiendo es de Referencia a Entidad o Referencia
a Colección, la función convertirá a texto los atributos descriptivos identificadores de la referencia.
✓ Para establecer el formato de la lista, la función toma del atributo “Formato de la colección” de la

```
Colección que se desea convertir los parámetros “Iniciador de grupo”, “Separador de elemento”,
```

```
“Finalizador de grupo” y “Separador de grupo”. La función utiliza estos parámetros con el fin de que
se pueda personalizar el formato del texto a convertir, además, al convertirse en texto Enriquecido,
se admite que en estos parámetros se agreguen Saltos de línea o personalizaciones del formato del
texto como escribir en Negrita. De esta manera, se define que el formato del texto convertido será:
```
<Iniciador de grupo> <Elemento> <Separador de elemento> <Elemento> <Finalizador de
grupo> <Separador de grupo>

✓ Para los casos en los que se encuentre una colección dentro de la colección que estoy convirtiendo, la
función utilizará el formato de la nueva colección por sobre el de la colección superior.

Orden de los elementos:
✓ La función prioriza el Orden de Elementos establecido en la Colección para listar los grupos de
elementos en base al orden establecido por la misma. Si la misma no tiene un orden entonces lista los
elementos en el orden predeterminado de UI.

✓ Los elementos de cada grupo se listarán en el orden en que se disponen los miembros del compuesto
de la Colección.
✓ Si se establece un orden en la expresión de búsqueda utilizada como parámetro de la función,

```
éste prevalecerá por sobre los definidos en los puntos anteriores.
```
```
Ejemplo – Colección Domicilios :
```
```
Formato de la colección:
```
```
Orden de elementos:
```
```
Miembros del compuesto “Domicilio”:
```
```
Colección a Texto Enriquecido (Domicilios)
Devuelve:
```

```
Colección a Texto Enriquecido (En .Domicilios buscar Dirección)
Devuelve:
```
```
Colección a Texto Enriquecido (En .Domicilios buscar Código postal; País; Ciudad; Dirección)
Devuelve:
```
#### Colección a texto internacionalizable(Colección)

```
La función “Colección a texto Internacionalizable()” trabaja de manera similar a “Colección a
Texto Enriquecido()” con la diferencia de que esta permite convertir un conjunto de ítems de una
colección en una lista de elementos de tipo Texto Internacionalizable.
```
```
Sintaxis válidas de la función:
```
```
Colección a Texto Internacionalizable(<Colección>)
Colección a Texto Internacionalizable(En <Colección> Buscar <Atributo>)
Colección a Texto Internacionalizable(En <Colección> Buscar <Atributo 1>;<Atributo
2>;<Atributo 3>)
```
```
Comportamientos en los que difiere respecto de “Colección a Texto Enriquecido()”:
✓ El tipo de atributo Tipo Internacionalizable no admite la modificación del formato del
texto como lo hace el Texto Enriquecido, por lo que, “Colección a Texto Internacionalizable” recibe
los parámetros de “Formato de la colección” y los aplica en la lista convertida como Literales.
```
Permite convertir un conjunto de ítems de una colección en una lista de elementos de tipo Texto
Internacionalizable.

En esta función podemos utilizar como parámetro de entrada tanto un atributo de tipo Colección como
una expresión de búsqueda “En <Colección> Buscar <Atributo>”, siempre y cuando luego de la
instrucción “En” se indique una Colección, por ejemplo, si se desea obtener la lista de direcciones de
un cliente, éstas pueden obtenerse del siguiente modo: En .Domicilios Buscar Dirección.

Adicionalmente, la función admite que se pueda solicitar más de un elemento en la expresión de
búsqueda, para esto, al momento de escribir la expresión se deberán indicar los elementos de la


colección que se desean convertir separándolos con ‘;’, por ejemplo; En .Domicilios Buscar Dirección;
Código postal.

Sintaxis válidas de la función:

Colección a Texto Internacionalizable(<Colección>)

Colección a Texto Internacionalizable(En <Colección> Buscar <Atributo>)

Colección a Texto Internacionalizable(En <Colección> Buscar <Atributo 1>;<Atributo 2>;<Atributo 3>)

**Ejemplos:**

### Información del sistema

#### Instancia Principal()

Devuelve el id de la instancia principal seleccionada en una actividad. Se usa para filtrar las grillas de
vista previa.

**Ejemplos:**

Número a texto(Instancia Principal()) retorna un id único para esa entidad, por ejemplo:
100000000000014

#### Entidad Principal()

Devuelve una referencia a la entidad principal de una actividad. Se usa poder filtrar en los logs para la
vista previa por la referencia a la entidad y el id de la instancia.

**Ejemplos:**

EntidadPrincipal() como valor calculado en un atributo de tipo referencia a entidad, retorna la entidad
en la que se está ingresando una nueva instancia.

#### Operación Principal()

Devuelve el id de la operación principal de un formulario.

**Ejemplos:**

Número a texto(Operación Principal()) retorna siempre 111111111.

#### Usuario()

Devuelve una referencia a la instancia de la entidad Usuario que corresponde al usuario que está
utilizando actualmente el sistema, es decir, el usuario autenticado. Utilizando esta referencia se puede
llegar a cualquier atributo del usuario por ejemplo: Usuario().Nombre.

En este caso, se debe tener en cuenta la seguridad del usuario que está ejecutando la función. Además,
hay ciertos datos que no se podrán visualizar, más allá de la seguridad, por ejemplo: la contraseña.

**Ejemplos:**

Usuario().Nombre de usuario retorna jperez

Usuario().Nombre + ' ' + Usuario().Apellido retorna Juan Perez

Usuario().Tipo de usuario retorna Editor

#### Idioma de Interfaz de Usuario()

Devuelve el valor del enumerado que contiene el idioma y dialecto de los editores o de la aplicación
que está siendo ejecutada en la interfaz de usuario.

**Ejemplos:**

Idioma de interfaz de usuario() retorna Español


#### Idioma de Datos()

Devuelve el valor del enumerado que contiene el idioma y dialecto de los editores o de la aplicación
que está siendo ejecutada en el idioma de datos.

**Ejemplos:**

Idioma de datos() retorna Español

#### Modelo()

Devuelve una referencia a la instancia de Modelo que está siendo ejecutada. Utilizando esta referencia
se puede llegar a cualquier atributo del modelo.

**Ejemplos:**

Modelo().Nombre retorna Editores

Modelo().Identificador de dirección URL retorna editors

#### Ambiente()

Devuelve una referencia a la instancia de Ambiente que está siendo ejecutada. Utilizando esta
referencia se puede llegar a cualquier atributo del ambiente.

**Ejemplos:**

Ambiente().Nombre retorna Desarrollo

Ambiente().URL retorna Development

#### Versión del modelo de aplicación()

Devuelve una referencia a la instancia de Versión del modelo de aplicación que está siendo ejecutada.
Utilizando esta referencia se puede llegar a cualquier atributo de la versión del modelo de aplicación.

**Ejemplos:**

Versión del modelo de aplicación().Nombre retorna Versión 3

Versión del modelo de aplicación().Número retorna 3

#### Build del modelo de aplicación()

Devuelve una referencia a la instancia del build del modelo de aplicación que está siendo ejecutado.
Utilizando esta referencia se puede llegar a cualquier atributo del build del modelo de aplicación.

**Ejemplos:**

Build del modelo de aplicación().Nombre retorna 14

Build del modelo de aplicación().Número retorna 14

#### Versión del modelo de editores()

Devuelve una referencia a la instancia de Versión del Editor que está siendo ejecutada.
Utilizando esta referencia se puede llegar a cualquier atributo de la versión del modelo de editores.

**Ejemplos:**

Versión del modelo de editores().Nombre retorna versión 1

Versión del modelo de editores().Número retorna 1

#### Build del modelo de editores()

Devuelve una referencia a la instancia del build del Editor que está siendo ejecutado. Utilizando esta
referencia se puede llegar a cualquier atributo del build del modelo de editores.

**Ejemplos:**


Build del modelo de editores().Nombre retorna 166

Build del modelo de editores().Número retorna 166

#### Sitio()

Devuelve una referencia a la instancia de Sitio en donde el usuario está autenticado. Utilizando esta
referencia se puede llegar a cualquier atributo del sitio.

**Ejemplos:**

Obtener traducción(Sitio().Nombre;'es') retorna Rosario

Nota: al ser el nombre un valor internacionalizable, es necesario utilizar la función de traducción para
asignarlo en un atributo de texto.

#### Dominio()

Devuelve una referencia a la instancia de Dominio en donde el usuario está autenticado. Utilizando
esta referencia se puede llegar a cualquier atributo del dominio.

**Ejemplos:**

Dominio().Nombre retorna neuralsoft.fastprg.com

#### Explorador()

Devuelve una referencia a la instancia de Browser que se generó cuando el usuario autenticado inició
sesión. Contiene toda la información posible del browser a través del cual se está utilizando la
aplicación. La entidad Log de Seguridad (cuyas instancias se crean cada vez que un usuario inicia sesión)
tiene una referencia a la entidad Browser que contiene la información del browser donde inicia sesión.

**Ejemplos:**

Explorador().Navegador de Internet retorna FakeBrowser

#### Estación de Trabajo()

Devuelve una referencia a la instancia de Puestos de Trabajo en la cual se encuentra autenticado el
usuario.

**Ejemplos:**

Estación de trabajo().Nombre retorna

#### A transformar(Atributo)

Solamente se usa en la grilla de definición de transformaciones, indica que se tiene en cuenta no el
valor del atributo en la instancia origen, si no el valor del atributo que se está transformando.

Además, cuando hay una colección de otra colección (2do nivel o superior): devuelve lo que se quiere
transformar de un atributo en el contexto de un ítem (no todo lo pendiente a transformar sino sólo lo
de un ítem).

**Ejemplos:**

Si la entidad origen de la transformación es la entidad factura y la factura pendiente de transformar
tiene una colección de entregas y dentro una colección de ítems de factura:

Colección de Entregas:

10 - may san martin 2054 Items de factura:

```
mesa 1
```
silla 6

10 - jun ov lagos 880 Items de factura:

```
escritorio 2
```

Si el usuario ingresa para transformar 1 mesa, 1 silla y 1 escritorio, el resultado en los ítems en la
entidad destino será:

Colección de Entregas:

10 - may san martin 2054 Items de factura:

```
mesa 1
```
silla 1

10 - jun ov lagos 880 Items de factura:

```
escritorio 1
```
#### Pendiente de transformar()

Devuelve la cantidad total pendiente de transformar para una instancia/ítem según sea el contexto de
la transformación, en transformaciones de tipo parcial.

#### Esnulo(Atributo)

Devuelve verdadero si el valor del atributo es nulo, y falso si el atributo tiene algún valor.

**Ejemplos:**

Esnulo (texto base) devuelve verdadero antes de asignarle un valor

#### Noesnulo(Atributo)

Devuelve falso si el valor del atributo es nulo, y verdadero si el atributo tiene algún valor.

**Ejemplos:**

Noesnulo (texto base) devuelve falso antes de asignarle un valor y verdadero al asignarle un valor

#### Valor anterior(Atributo)

**Características del operador:**

El operador ‘valor anterior()’ brinda el valor anterior de un atributo para una instancia, es decir, el valor
del atributo en la última versión persistida de la instancia. Esto permite, por ejemplo, comparar el valor
actual del atributo con el valor anterior. Para utilizarlo, el usuario debe invocar al operador y especificar
dentro de los paréntesis el nombre del atributo del cual se desea conocer su valor anterior.

**Sintaxis:**

Valor anterior(<Atributo>)

**Restricciones:**

El operador no admite parámetros de un contexto ajeno al de la instancia sobre la cual es invocado.

Categoría de tipo de atributo de entrada admitidos:

- Simple
- Enumerado
- Secuencia
- Referencia a Entidad
- Referencia a Colección

**Valor de retorno:**

Retorna el mismo tipo de atributo que se ingresa como parámetro, el valor de este será el de la última
instancia persistida o nulo.


**Comportamiento:**

El operador retorna el valor del atributo solicitado en la última versión persistida de la instancia,
independientemente si difiere del valor actual o si el valor anterior y el valor actual son iguales. En el
caso de que no se encuentre un valor anterior para el atributo especificado, se retorna el valor nulo.

**Ejemplo en Regla de negocios:**

Condición de ejecución: valor anterior(Cliente) <> Cliente

De esta manera, la acción condicional de la regla de negocios se ejecutará solamente si el valor anterior
y el valor actual del atributo Cliente de la instancia son diferentes, es decir, si se modifica el Cliente en
la instancia.

#### Imputaciones Pendientes(Nombre imputación)

Dada una instancia determinada, la función retornará si ha encontrado imputaciones pendientes para
la misma.

#### A imputar()

Esta función retorna sólo aquellos valores que entraron en tolerancia o en saldo de conversión de los
elegidos para imputar.

Se distinguen los siguientes casos:

1 - En el caso de que se pida el valor de un atributo (que no es el imputable) de la cabecera o de
una colección que no es la que contiene el atributo imputable, retorna el valor correspondiente del
atributo solicitado de la instancia que entro en tolerancia o en saldo de conversión.

2 - En el caso de que se pida el valor de un atributo que no es el imputable, pero pertenece a la
colección del atributo imputable o una de un nivel inferior, retorna el valor del atributo solicitado pero
solo de los ítems que entraron en tolerancia o saldo de conversión según corresponda.

3 - En el caso de que se pida el valor del atributo imputable se deberá retornar el valor que entro
en tolerancia o saldo de conversión según corresponda. Si el atributo imputable estaba en una
colección se deberá retornar una colección con el valor que entro en tolerancia o saldo de conversión
según corresponda.

Solamente se usa en la grilla de definición de reglas de cancelación en imputaciones.

Ejemplo: En una factura con colección de productos, donde el atributo imputable es Item.Cantidad
pero entro en tolerancia sólo 2 productos de toda la colección o saldo de conversion, se puede utilizar
la expresión Aimputar(Items.producto) para utilizar sólo los ítems de productos que entraron en
tolerancia o saldo de conversión.

#### Instancias a imputar(Entidad base de imputación)

Esta función retornará las instancias que están en memoria cuando un usuario las seleccione dentro
de una actividad de imputación, es decir, retornará una referencia a la entidad base que tenga la
imputación.

Para invocarla se definirá de la siguiente manera:

Instancias a imputar(entidad)

Siendo "entidad" una entidad que contiene una imputación.

**Ejemplos:**

1 - Se modela una entidad "Pago" la cual a su vez desencadena en la entidad "Movimiento de
proveedores".

2 - En Movimiento de Proveedores se agrega una imputación.


3 - Seguidamente, se crea una actividad de única instancia con imputación llamada "Pago con
imputación".

4 - Se define una RN para crear ítems en una colección con los comprobantes seleccionados para
imputar el pago.

5 - Entonces, se podrá definir como expresión de asignación de valores:

Instancias a imputar(Movimiento de proveedores)

Esta expresión retornará la referencia a las instancias seleccionadas en la actividad de única instancia
con imputación al momento de crear e imputar el pago.

Además, se deberán tener en cuenta las siguientes observaciones:

1 - Si se utiliza esta función en un lugar que no sea una actividad de imputación retornará nulo.
Es decir, siguiendo con el ejemplo anterior, esto ocasionará que:

- Si se crea el Pago por una actividad de única instancia no se asigne ningún valor en el atributo.
- Si se crea el Pago por la actividad de única instancia con imputación, en este caso si retornará
    las instancias seleccionadas al momento de imputar.

2.- Al utilizar esta función aunque devuelva una referencia no se puede acceder a otro atributo de esa
instancia mediante el uso de pathfield, es decir, no se podrá utilizar expresiones como: Instancias a
imputar(movimiento proveedores).fecha.

3.- En caso de necesitar obtener el valor de otro atributo de la referencia obtenida en memoria se
deberá usar una expresión de En buscar, por ejemplo, “En Movimiento de proveedores buscar fecha
cuando esta instancia = instancias a imputar(Movimiento de proveedores)”.

#### Valor a imputar (Referencia a instancia a imputar, Tipo de atributo imputable)

Retorna un valor numérico, esta función recibe como parámetro la referencia a las instancias
seleccionadas para imputar en una actividad de imputación y retorna el valor ingresado en el atributo
imputable al momento de imputar la instancia.

La invocación a esta función se define de la siguiente manera:

valor a imputar(instancia a imputar; tipo de atributo imputable)

Siendo instancia a imputar una referencia a una instancia seleccionada en la imputación (valor
resultante de la función instancias a imputar), y el parámetro tipo de atributo imputable corresponde
a un enumerado, el cual tendrá los siguientes valores posibles:

1 - Entrada: atributo de entrada en una imputación de doble atributo imputable, o en caso de
imputaciones de un único atributo imputable también se utilizará esta opción para definirlo.

2 - Salida: atributo imputable de salida configurado en imputaciones de atributo imputable doble.

Si esta expresión se evalúa en otro lugar que no sea una actividad de imputación retornará nulo.

Por ejemplo, siguiendo con el mismo caso indicado anteriormente para la función de instancias a
imputar, si además de la acción de crear ítem se define en la RN una acción de modificación de ítem
que asigne en un campo el resultado de esta función, agregará en el atributo el valor del importe
ingresado cuando se imputó la instancia:

#### Autorizaciones Pendientes(Nombre autorización)

Dada una instancia determinada, la función retornará si ha encontrado autorizaciones pendientes para
la misma.

#### Transformaciones Pendientes(Nombre transformación)

Dada una instancia determinada, la función retornará si ha encontrado transformaciones pendientes
para la misma.


#### Valor Actual(Secuenciador)

Devuelve el valor actual de un secuenciador, si es posible.

#### Horarios laborales(Calendario, Día)

A partir de un calendario específico y un día determinado, la función retornará los horarios laborales
del día indicado.

Esta función será utilizada para conocer los horarios laborales dentro de un calendario, al momento de
presentar la semana laboral.
**Ejemplos:**

#### Clasificación de instancias de entidades paramétricas( )

No recibe parámetros. Utiliza la función Entidad propia de dominio()

Retorno: Clasificación de elemento dinámico

Cuando las instancias de entidades paramétricas sean creadas en el dominio donde fue creada la
entidad, se considerarán de Sistema. En el caso contrario, es decir, en el caso que una entidad pase a
otro dominio y ahí se cree una instancia, ésa instancia tendrá clasificación de Usuario.

**Ejemplos:**

La entidad Tipo de documento es paramétrica, se envían algunas instancias desde el dominio donde se
crea la entidad. Luego, en otro dominio se crea otra instancia. En ese dominio, en el ABM se crea una
columna calculada donde se indique la función Clasificación de instancias de entidades paramétricas().
La instancia creada en el dominio hijo, retorna Usuario, mientras que las otras instancias retornan
Sistema.

#### Clasificación de herramientas dinámicas( )

No recibe parámetros. Utiliza la función Modelo de dominio raíz()

Retorno: Clasificación de elemento dinámico

Si el modelo es de dominio raíz, la clasificación será de sistema. Si el modelo no es del dominio raíz,
tendrá clasificación de usuario.

#### Obtener coordenadas geográficas()

Esta función no recibe parámetros y retorna un tipo de atributo Coordenadas (latitud y longitud). Este
atributo indica las coordenadas geográficas actuales del dispositivo usado. Las mismas son un
hipervínculo a la aplicación de mapas que se tenga configurada.

**Ejemplos:**

#### Obtener precisión geográfica()

Esta función no recibe parámetros y retorna un atributo de tipo Precisión. Este atributo indica la
precisión de la posición geográfica actual del dispositivo.

**Ejemplos:**


#### Editado por usuario(Atributo)

Determina si el valor de un atributo fue ingresado por el usuario, recibe como parámetro el atributo
sobre el cual se desea consultar si el valor actual que posee fue asignado por el usuario y retorna
"verdadero" o "falso" según corresponda.

**Ejemplos:**

Editado por usuario(Fecha)

- Verdadero: el valor actual del atributo fue asignado manualmente por el usuario.
- Falso: el valor del atributo no fue ingresado por el usuario.

#### Calculado por valor inicial(Atributo)

Determina si el valor de un atributo fue asignado por un valor inicial, recibe como parámetro el atributo
sobre el cual se desea consultar si el valor actual que posee fue asignado por valor inicial y retorna
"verdadero" o "falso" según corresponda.

**Ejemplos:**

Calculado por valor inicial(Fecha)

- Verdadero: el valor actual del atributo fue calculado por un valor inicial.
- Falso: el valor del atributo no fue calculado por un valor inicial.

#### Retorna nulo()

Existen situaciones de negocio por las cuales en los procesos desarrollados se requiere blanquear
atributos, asignando a estos un valor nulo. Para este tipo de situaciones es posible utilizar la función
que permite asignar a cualquier atributo del sistema un valor nulo. Esta función no requiere de
parámetro de entrada y su forma de invocación es Retorna nulo().

Consideraciones:

Puede utilizarse para asignar un valor nulo a cualquier atributo independientemente del tipo de
atributo que posean.

**Ejemplos:**

Se crea una Regla de negocios por botón de modificación de instancia actual para limpiar un formulario.
Entonces, al presionar el botón, se les asigna Retorna nulo() en el valor a cada uno de los atributos de
la entidad donde aplica.


Un ejemplo de uso es ingresar los valores, confirmar. Presionar el botón y reingresar los valores. En el
historial de la entidad para esa instancia, se observa de la siguiente manera:

#### Base de datos()

Esta función devuelve una referencia a la base de datos actual de la sesión.

#### Clave única por servicio Web()

La regla de negocio que consume un servicio web puede devolver la clave única para identificar a la
instancia desde donde se ejecuta.

Esto se configura en la acción de la regla de negocio.

#### Evaluar()

El operador Evaluar permite obtener el resultado de una Expresión Dinámica previamente guardada
en una Instancia, logrando así la creación de Expresiones Dinámicas.


Comportamiento:
El operador **Evaluar** ejecuta una Expresión Dinámica utilizando como contexto la Instancia o Ítem que
se le envía como primer parámetro. El Tipo de Atributo resultante de evaluar esta expresión, es el Tipo
de Atributo configurado en la definición de la Expresión Dinámica.

**Ejemplos:**

Si se quiere inicializar de manera automática los descuentos de los ítems de comprobante de una
factura según el rubro de estos, podemos modelar este proceso de la siguiente manera:

Primero, debemos modelar la Entidad que poseerá las Instancias de las Expresiones Dinámicas

Una vez dada de alta esta Entidad, se deben dar de alta las Instancias de la misma que contendrán las
Expresiones Dinámicas

Para este ejemplo, modelaremos la Entidad **Factura** de la siguiente manera:

En la Entidad **Factura** , dentro de la colección **Items de Comprobante** , desplegaremos la colección
**Descuentos** y allí modificaremos los siguientes Atributos:

**Porcentaje**
En **Valor inicial** escribimos la siguiente expresión:

Evaluar(Ítem padre.Producto; En Descuentos por rubro primer Expresión Dinámica cuando Rubro =
Ítem padre.Producto.Rubro)

**Subtotal**
En **Valor calculado** escribimos la siguiente expresión:

Ítem padre.Subtotal

**Importe**
En **Valor inicial** escribimos la siguiente expresión:

Subtotal*Porcentaje/100

De esta manera, el operador ejecutará las **Expresiones dinámicas** de la Entidad **Descuentos por rubro**
e inicializará el valor de **Porcentaje** según el **Rubro** del **Producto**.

Como podemos observar, en el caso de **Tela** , que corresponde al rubro **Textil** , inicializa el porcentaje
en 20:


Mientras que, en el caso de Auriculares, que pertenecen al rubro Electrónica, inicializa el porcentaje
en 10:

#### Firmar con certificado(Texto a firmar, Certificado, Clave privada, Algoritmo)

Función utilizada para generar el CMS al momento de intentar autenticarse en un servicio web. Cómo
se invoca: Firmar con certificado(Texto;Certificado;Clave;Algoritmo)

Parámetros que recibe:

Parámetro 1 : Texto a firmar

Parámetro 2 : Certificado

Parámetro 3 : Clave privada

Parámetro 4 : Algoritmo de encriptación. Los algoritmos soportados son:

- Sha1withRsa
- Sha256With Rsa
- Sha512WithRsa

Valor de retorno: Texto. Genera el CMS al momento de intentar autenticarse en un web service.

#### Generar reporte(Referencia a Reporte por bandas)

Función utilizada para generar un reporte por bandas a partir de la instancia desde la cuál se invoca la
función.

Parámetros que recibe:

- Reporte por bandas: indica el reporte por bandas que se va a generar como resultado de la
    función.

### Uso interno

#### Valor de tolerancia de imputación()

Devuelve el valor de la diferencia al realizar una imputación cuando se entra en Tolerancia. Solo aplica
para ser utilizada dentro de la solapa “Reglas de cancelación” en la edición de una imputación de una
entidad.


#### Identificador de JVM()

Función de sistema que permite obtener en un proceso el identificador de la JVM que atendió el mismo.

Esta información es utilizada como auditoría en muchos lugares del sistema como lo puede ser por
ejemplo en el procesamiento de colas, para lograr identificar la JVM que atendió el procesamiento de
cada una de las instancias de la misma.

#### Estado de usuario(Usuario)

Evalúa el estado del usuario según las políticas del sistema. Los posibles valores de retorno serán:

- Bloqueado. El usuario se encuentra momentáneamente bloqueado, dependiendo de la
configuración de políticas, se podrá desbloquear automáticamente o deberá realizarse de forma
manual.
- Inhabilitado. Se inhabilita el usuario por diferentes motivos:
    - Inhabilitación directa del usuario
    - Inhabilitación de una Unidad Organizacional a la que pertenece un usuario
    - Inhabilitación por políticas de inhabilitación con respecto a fechas de expiración
- Activo. El usuario se encuentra habilitado para utilizar el sistema.

#### Solicita código de autorización a Telegram(Texto, Entero, Teléfono celular)

Recibe por parámetro los datos necesarios para el servicio de Telegram y retorna el código de autorización
provisto por la API de Telegram.

#### Validar código Telegram(Texto, Entero, Teléfono celular, Texto, Texto)

Valida que la cuenta de notificación este autorizada a utilizar el servicio de Telegram.
Devuelve un valor de tipo booleano

#### Cambios a comunicar para vínculos de seguridad()

Determina si se modificaron datos en objetos de vínculos de seguridad que deben ser comunicados a
los dominios que confían.

#### Chequeo inicio JVM()

Chequea si tiene que iniciar una nueva jvm. Se utiliza en el Marketplace.

#### Crear resultado ejecución()

Función para crear resultado ejecución en grabación de casos de prueba

#### Descargar blob desde URL(URL)

Descargar blob desde URL externa. La imagen queda en la entidad Binario.

**Ejemplos:**

Descargar blob desde URL('https://www.neuralsoft.com/wp-content/uploads/2023/04/Isologotipo-
NeuralSoft-Final-2048x537.png') retorna

#### Extrae texto de Json para telegram()

Extrae texto de Json para telegram


#### Extraer metadata de binario()

Extraer metadata de binario

**Ejemplos:**

En la entidad binario se tiene un atributo Blob, se agrega una columna calculada con la función:

Extraer metadata de binario(blob) y muestra el contenido de la metadata.

#### Fecha expiración de token por usuario()

Indica instante en que expira el token de recuperación de contraseña por usuario.

#### Generar enlace de descarga para el agente de dispositivos()

No recibe ningún parámetro y devuelve un texto enriquecido internacionalizable.

#### Inicia la sesión de Telegram()

Envía código de autorización a Telegram para iniciar sesión.

#### SHA256(Blob)

Calcula un hash usando SHA-256. Se conoce como SHA-256 al Algoritmo de Hash Seguro (Secure Hash
Algorithm) de 256 bits, que se utiliza para la seguridad criptográfica. Estos algoritmos generan hashes
(cadenas de caracteres de longitud fija) irreversibles y únicos.

**Ejemplos:**

En la entidad binario se tiene un atributo Blob, se agrega una columna calculada con la función:

Sha256(blob) y muestra el contenido de la imagen encriptada.

#### Token alfanumérico()

Devuelve el token para contraseña de usuario nuevo, o recuperación de contraseña de usuario
existente.

**Ejemplos:**

Token alfanumérico(1;10)

### Financieras

AMORTIZ.LIN(costo, fecha_compra, primer_período, costo_residual, período, tasa, [base])

AMORTIZ.PROGRE(costo, fecha_compra, primer_período, costo_residual, período, tasa, [base])

CANTIDAD.RECIBIDA(liquidación, vencimiento, inversión, descuento, [base])

CUPON.DIAS(liquidación, vencimiento, frecuencia, [base])

CUPON.DIAS.L1(liquidación, vencimiento, frecuencia, [base])

CUPON.DIAS.L2(liquidación, vencimiento, frecuencia, [base])

CUPON.FECHA.L1(liquidación, vencimiento, frecuencia, [base])

CUPON.FECHA.L2(liquidación, vencimiento, frecuencia, [base])

CUPON.NUM(liquidación, vencimiento, frecuencia, [base])

DB(costo, valor_residual, vida, período, [mes])

DDB(costo, valor_residual, vida, período, [factor])

DURACION(liquidación, vencimiento, cupón, rendimiento, frecuencia, [base])

DURACION.MODIF(liquidación, vencimiento, cupón, rendimiento, frecuencia, [base])


DVS(costo, valor_residual, vida, período_inicial, período_final, [factor], [sin_cambios])

INT.ACUM(emisión, primer_interés, liquidación, tasa, v_nominal, frecuencia, [base], [método_calc])

INT.ACUM.V(emisión, liquidación, tasa, v_nominal, [base])

INT.EFECTIVO(int_nominal, núm_per_año)

INT.PAGO.DIR(tasa, período, núm_per, va)

LETRA.DE.TES.PRECIO(liquidación, vencimiento, descuento)

LETRA.DE.TES.RENDTO(liquidación, vencimiento, precio)

LETRA.DE.TEST.EQV.A.BONO(liquidación, vencimiento, descuento)

MONEDA.DEC(moneda_fraccionaria, fracción)

MONEDA.FRAC(moneda_decimal, fracción)

NPER(tasa, pago, va, [vf], [tipo])

PAGO(tasa, nper, va, [vf], [tipo])

PAGO.INT.ENTRE(tasa, núm_per, vp, per_inicial, per_final, tipo)

PAGO.PRINC.ENTRE(tasa, núm_per, vp, per_inicial, per_final, tipo)

PAGOINT(tasa, período, núm_per, va, [vf], [tipo])

PAGOPRIN(tasa, período, núm_per, va, [vf], [tipo])

PRECIO(liquidación, vencimiento, tasa, rendimiento, valor_de_rescate, frecuencia, [base])

PRECIO.DESCUENTO(liquidación, vencimiento, descuento, amortización, [base])

PRECIO.PER.IRREGULAR.1(liquidación, vencimiento, emisión, primer_cupón, tasa, rendimiento,
amortización, frecuencia, [base])

PRECIO.PER.IRREGULAR.2(liquidación, vencimiento, último_interés, tasa, rendimiento, amortización,
frecuencia, [base])

PRECIO.VENCIMIENTO(liquidación, vencimiento, emisión, tasa, rendimiento, [base])

RENDTO(liquidación, vencimiento, tasa, precio, amortización, frecuencia, [base])

RENDTO.DESC(liquidación, vencimiento, precio, amortización, [base])

RENDTO.PER.IRREGULAR.1(liquidación, vencimiento, emisión, primer_cupón, tasa, precio,
amortización, frecuencia, [base])

RENDTO.PER.IRREGULAR.2(liquidación, vencimiento, último_interés, tasa, precio, amortización,
frecuencia, [base])

RENDTO.VENCTO(liquidación, vencimiento, emisión, tasa, precio, [base])

SLN(costo, valor_residual, vida)

SYD(costo, valor_residual, vida, período)

TASA(núm_per, pago, va, [vf], [tipo], [estimar])

TASA.DESC(liquidacion, vencimiento, precio, amortización, [base])

TASA.INT(liquidacion, vencimiento, inversión, valor_de_rescate, [base])

TASA.NOMINAL(tasa_efectiva, núm_per_año)

TIR(valores, [estimar])

TIR.NO.PER(valores, fechas, [estimar])

TIRM(valores, tasa_financiamiento, tasa_reinversión)

VA(tasa, nper, pago, [vf], [tipo])

VF(tasa,núm_per,pago,[va],[tipo])

VF.PLAN(principal,programación)

VNA(tasa,valor1,[valor2],...)

VNA.NO.PER(tasa, valores, fechas)


## Anexo II: Atributos

```
Ejemplo Significado
```
Nombre Entidad.Nombre Atributo (^) Atributo de Entidad
Nombre Entidad.Nombre Atributo Referencia.Nombre
Atributo
Atributo que se obtiene a través de
otro atributo de categoría
referencia. Ejemplo: Factura.Cliente
minorista.Nombre
Nombre Entidad.Nombre Atributo Referencia
Inversa.Nombre Atributo en la entidad referenciada
inversamente
Cliente.Cliente comprador en
Factura.Nro de Factura
Nombre Entidad.Nombre Atributo de la Colección
Referenciada.Nombre Atributo
Atributo que se obtiene a través de
otro atributo de categoría referencia
a elemento de colección. Ejemplo:
Factura.Dirección del cliente.Calle
Nombre Entidad.Nombre Acumulador.Nombre Atributo (^) Acumulador que se obtiene al estar
definida la Entidad como una
dimensión en la definición del
Acumulador. Es importante aclarar,
que no se permite el uso de
pathields a través de atributos del
acumulador, en las expresiones
dentro de un acumulador solo
pueden usarse los atributos,
dimensiones y pathfields a través de
las dimensiones del acumulador.
NombreEntidad.NombreAcumuladorReferenciaInversa.
NombreAtributo
Por ejemplo, en la entidad Factura
hay una referencia a Cliente y
además hay un acumulador llamado
Suma de total por cliente, cuyo
atributo es Importe y la dimensión es
Cliente. La siguiente expresión:
“Cliente. Referencia inversa al
acumulador Suma de total por
cliente.Importe” Esto me da la suma
del total facturado al Cliente.
Nombre Entidad.Nombre Atributo Referencia
Inversa.Nombre Atributo
Nombre entidad.Nombre atributo de tipo
secuencia.Nombre partición
Muestra el valor de una partición de
un atributo de tipo secuencia. Por
ejemplo: auto.patente.letras
muestra ABC.
Retorna texto o número
dependiendo del tipo de partición
(alfanumérico o numérico).
Nombre entidad.Nombre atributo de tipo secuencia (^) Muestra el valor de la secuencia. Si
tiene una sola partición, se debe
usar la misma, y si tiene más de una,
se tiene que usar la partición que
tiene todas las particiones
concatenadas. Por ejemplo:
auto.patente muestra ABC 123


```
Si tiene una sola partición, retorna
texto o número, dependiendo del
tipo de partición (alfanumérico o
numérico).
Si tiene 2 o más particiones, retorna
texto, independientemente de los
tipos de las particiones. Ejemplo:
partición 1 de 3 dígitos, valor: 3,
partición 2 de 3 dígitos, valor: 5,
resultado texto: 003005.
```
Nombre Entidad.Nombre Colección (^) Colección en una Entidad
Nombre Entidad.Nombre Colección.Nombre Atributo (^) Colección que contiene sólo el
atributo indicado.
Nombre Entidad.Nombre Colección.Nombre atributo
dentro de compuesto
Colección que contiene un
compuesto (no se nombra al
compuesto)
Nombre Entidad.Nombre Compuesto. Nombre atributo
dentro del compuesto
Un atributo dentro de un
compuesto.
.Nombre Atributo Colección
.Nombre Atributo.Nombre Atributo Colección
Devuelve el valor del atributo
colección en la instancia actual. Solo
se puede usar dentro de una de las
“operaciones sobre colecciones”
(sumar, buscar, promedio, etc.) y
sirve para que se realice una
operación en una colección con los
valores de la instancia actual
solamente.
Por ejemplo, si en la entidad Factura
hay una colección llamada Items, la
expresión: Factura.Items retorna los
ítems de todas las facturas, pero
.Items retorna los ítems de la factura
actual.