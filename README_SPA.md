# **DrivenData_DengueFever**

Predicción de casos de fiebre del dengue en San Juan (Puerto Rico) e Iquitos (Perú) basado en datos 
meteorológicos y datos históricos de casos de fiebre del dengue.

## ¿Puedes predecir las epidemias locales de Dengue?

La fiebre del dengue es una enfermedad transmitida por mosquitos que ocurre en partes tropicales y 
subtropicales del mundo. En casos leves, los síntomas son similares a los de la gripe: fiebre, erupción 
cutánea y dolor muscular y articular. En casos severos, la fiebre del dengue puede causar sangrado severo, 
presión arterial baja e incluso la muerte.

Debido a que es transmitido por mosquitos, la dinámica de transmisión del dengue está relacionada con 
variables climáticas como la temperatura y la precipitación. Aunque la relación con el clima es compleja, 
un número creciente de científicos argumenta que es probable que el cambio climático produzca cambios 
distributivos que tendrán importantes implicaciones para la salud pública en todo el mundo.

En los últimos años, la fiebre del dengue se ha extendido. Históricamente, la enfermedad ha sido más 
frecuente en el sudeste asiático y las islas del Pacífico.

Utilizando los datos ambientales recopilados por varias agencias del Gobierno Federal de los EE. UU., 
Desde los Centros para el Control y la Prevención de Enfermedades hasta la Administración Nacional 
Oceánica y Atmosférica del Departamento de Comercio de los EE. UU, ¿Puede predecir el número de casos de 
fiebre del dengue reportados cada semana en San Juan, Puerto Rico e Iquitos, Perú?

Esta es una competencia de práctica de nivel intermedio. Su tarea es predecir el número de casos de 
dengue cada semana (en cada ubicación) en función de las variables ambientales que describen los cambios 
de temperatura, precipitación, vegetación y más.

La comprensión de la relación entre el clima y la dinámica del dengue puede mejorar las iniciativas de 
investigación y la asignación de recursos para ayudar a combatir las pandemias que amenazan la vida.

## Predecir la próxima pandemia

Los datos para esta competición provienen de múltiples fuentes destinadas a apoyar la iniciativa 
“Predict the Next Pandemic”. Los datos de vigilancia del dengue son proporcionados por los Centros para 
el Control y la Prevención de Enfermedades de EE. UU., así como por la Unidad 6 de Investigación Médica 
Naval del Departamento de Defensa y el Centro de Vigilancia Sanitaria de las Fuerzas Armadas, en 
colaboración con el gobierno peruano y las universidades de EE. UU. Los datos ambientales y climáticos 
son proporcionados por la Administración Nacional Oceánica y Atmosférica (NOAA), una agencia del 
Departamento de Comercio de los Estados Unidos.

En sus propias palabras:

Las predicciones precisas del dengue ayudarían a los trabajadores de salud pública ... y a las personas 
de todo el mundo a tomar medidas para reducir el impacto de estas epidemias. Pero predecir el dengue es 
una tarea considerable que requiere la consolidación de diferentes conjuntos de datos sobre la incidencia 
de enfermedades, el clima y el medio ambiente.

Este es un problema complicado, sin duda. Pero los datos reales a menudo son complicados y desordenados. 
Estudie utilizando los siguientes recursos, ¡sus ideas podrían salvar vidas!

LINKS

1. [Dengue Forecasting Homepage](http://dengueforecasting.noaa.gov/)
2. [CDC Dengue Overview](http://www.cdc.gov/Dengue/)
3. [NOAA Wiki](https://en.wikipedia.org/wiki/National_Oceanic_and_Atmospheric_Administration)

## Descripción del problema

Su objetivo es predecir el valor de la columna **_total_cases_** para cada (ciudad, año, semana del año) en el 
conjunto de prueba. Hay dos ciudades, San Juan e Iquitos, con datos de prueba para cada ciudad que 
abarcan 5 y 3 años respectivamente. 
Realizará una entrega que contenga predicciones para ambas ciudades. 
Los datos para cada ciudad se han concatenadodentro de una columna de ciudad que indica la fuente (sj para 
San Juan e iq para Iquitos). 
El conjunto de prueba es un futuro puro, lo que significa que los datos de la prueba son secuenciales y no 
se superponen con ninguno de los datos de entrenamiento. En todo momento, los valores faltantes se han 
rellenado como NaN.
