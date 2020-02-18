# **DrivenData_DengueFever**

Competition Hosted by DrivenData

LINK: https://www.drivendata.org/competitions/44/dengai-predicting-disease-spread/page/82/

Competition end date: June 28, 2020, 7:38 p.m.

## Can you predict local epidemics of dengue fever?

Dengue fever is a mosquito-borne disease that occurs in tropical and sub-tropical parts of the world. In mild cases, 
symptoms are similar to the flu: fever, rash, and muscle and joint pain. In severe cases, dengue fever can cause severe 
bleeding, low blood pressure, and even death.

Because it is carried by mosquitoes, the transmission dynamics of dengue are related to climate variables such as 
temperature and precipitation. Although the relationship to climate is complex, a growing number of scientists argue that 
climate change is likely to produce distributional shifts that will have significant public health implications worldwide.

In recent years dengue fever has been spreading. Historically, the disease has been most prevalent in Southeast Asia and 
the Pacific islands. These days many of the nearly half billion cases per year are occurring in Latin America.

Using environmental data collected by various U.S. Federal Government agencies—from the Centers for Disease Control and 
Prevention to the National Oceanic and Atmospheric Administration in the U.S. Department of Commerce—can you predict the 
number of dengue fever cases reported each week in San Juan, Puerto Rico and Iquitos, Peru?

This is an intermediate-level practice competition. Your task is to predict the number of dengue cases each week (in each 
location) based on environmental variables describing changes in temperature, precipitation, vegetation, and more.

An understanding of the relationship between climate and dengue dynamics can improve research initiatives and resource 
allocation to help fight life-threatening pandemics.

## Predict the Next Pandemic Initiative

The data for this competition comes from multiple sources aimed at supporting the Predict the Next Pandemic Initiative. 
Dengue surveillance data is provided by the U.S. Centers for Disease Control and prevention, as well as the Department 
of Defense's Naval Medical Research Unit 6 and the Armed Forces Health Surveillance Center, in collaboration with the 
Peruvian government and U.S. universities. Environmental and climate data is provided by the National Oceanic and 
Atmospheric Administration (NOAA), an agency of the U.S. Department of Commerce.

In their own words:

    _*Accurate dengue predictions would help public health workers ... and people around the world take steps to reduce the impact of these epidemics. But predicting dengue is a hefty task that calls for the consolidation of different data sets on disease incidence, weather, and the environment.*_

This is a complicated and messy problem, to be sure. But real data is often complicated and messy. Study up using the 
resources below—your insights could save lives!

You can learn more here:

1. [Dengue Forecasting Homepage](http://dengueforecasting.noaa.gov/)
2. [CDC Dengue Overview](http://www.cdc.gov/Dengue/)
3. [NOAA Wiki](https://en.wikipedia.org/wiki/National_Oceanic_and_Atmospheric_Administration)

## Problem description

Su objetivo es predecir el valor de la columna **_total_cases_** para cada (ciudad, año, semana del año) en el 
conjunto de prueba. Hay dos ciudades, San Juan e Iquitos, con datos de prueba para cada ciudad que 
abarcan 5 y 3 años respectivamente. 
Realizará una entrega que contenga predicciones para ambas ciudades. 
Los datos para cada ciudad se han concatenadodentro de una columna de ciudad que indica la fuente (sj para 
San Juan e iq para Iquitos). 
El conjunto de prueba es un futuro puro, lo que significa que los datos de la prueba son secuenciales y no 
se superponen con ninguno de los datos de entrenamiento. En todo momento, los valores faltantes se han 
rellenado como NaN.
