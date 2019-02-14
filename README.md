#Para ejecutar

* Instalar Python 3   
[Python 3](https://www.python.org/downloads/)

* Ejecurtar   
  `$ python -m venv [Ruta donde se descargo el repositorio]/readxlsb`   
  `$ source [Ruta donde se descargo el repositorio]/readxlsb`

* Dentro de la ruta de readxlsb ejecutar   
  `$ pip install -r requirements.txt`

* Para levantar el servicio   
  `$ python init.py`

El servicio se desplega en la ruta: http://localhost:5000/rows   
El Body de invocación es:

```javascript
{
	"fileName":"2019-02-12-Gioconda-Virgen v12.xlsb",
	"sheet":"6. Registro de Operaciones",
	"cells": [
		{"row":1,"column":2},
		{"row":7,"column":3}
	]
}
```

