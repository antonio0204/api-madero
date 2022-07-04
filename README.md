# Technical Challenge Spot (Backend Engineer) (GeoData)
##### _Crear solucion que ayude a obtener el precio agregado (promedio, mínimo y máximo) por m2 un código postal_

[![N|Solid](https://spot2.mx/_next/static/media/logo_green.d421cdc8.png)](https://spot2.mx/)

Para la siguiente solucion utlizamos el stack:
- Python (lenguaje programacion)
- Flask Rest Api(Framework)
- etl (carga datos)
- flask_testing (Framework Test)

## La consulta al API tendría que ser de la siguiente manera:
```sh
https://git.heroku.com/api-madero.git/price-m2/zip-codes/aggregate/construction_type={1-7}
```
Donde:
- zip_code = codigo postal propiedad
- aggregate = max', 'min', 'avg
- construction_types = tipo construccion


Para Ejecutar el siguiente API publicado en Heroku, se debe seguir primero los pasos de la transferencia de datos para garantizar el uso adecuado de la API 

https://github.com/ronald0204/etl-carga-datos

##### Creado y Desarrollado por: *Ronal Antonio Aguirre Villalobos*
