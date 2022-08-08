<div align="center" id="top"> 
  &#xa0;

  <!-- <a href="https://r5dschallenge_lmgarzon.netlify.app">Demo</a> -->
</div>

<h1 align="center">R5 Ds Challenge</h1>

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/{{YOUR_GITHUB_USERNAME}}" target="_blank">Author</a>
</p>

<br>

## 🎯 About ##
En este proyecto se quiere reducir las pérdidas por fraudes debidas a siniestros viales teniendo en cuenta una base de datos con 15,420 y 33 variables.
## ✨ Features ##

✔️ Análisis descriptiva y creación del modelo; esta parte se encuentra en el archivo **index.ipynb** aquí se hace todo el proceso desde: la lectura, depuración, análisis y construcción del modelo, y a lo largo de este se van describiendo los pasos.

Al final de todo se eligió el modelo XGBoost, ya que arrojo las mejores métricas y el tiempo de ejecución no es tan largo. Por otro lado cabe resaltar que la precisión y sobretodo el recall para este caso no fueron muy buenas, para futuros modelo sería interesante aplicar métodos de reducción de la dimensionalidad antes de probar los algoritmos de clasificación, evaluar las diferentes variables y trabajar algunos métodos de balanceo, ya que no es muy común que hayan casos de fraudes. También seria interesante reclasificar las categorías de las variables de entrada. 

✔️ Automatización del trains y predict se encuentran en los archivos **train.py** y **predict.py**, los resultados de este paso se encuentran en el archivo **model_trainer_execute.ipynb** y el modelo se encuentra en la carpeta **./models/model.pickle**

✔️ Como utilizar este modelo para reducir las pérdidas de fraude; Seria importante definir un periodo, por ejemplo cada mes se van a revisar los accidentes registrados para ingresar estos datos y ver las predicciones del modelo para categorizar este accidente como un fraude o no. En caso de ser fraude hacer un estudio más sofisticado con esas personas

✔️ Para llevar este modelo a producción seguiría los siguientes pasos:
Con el modelo entrenado y exportado en .pickle, cargo el repositorio a un proveedor de la nube (Google, AWS, Azure,...) mediante streamlit expongo un API la cual va a consumir el cliente y este a su vez consume el modelo.

Este modelo debe ser reentrenar cada cierto periodo, para evaluar sus métricas y en caso de que se presente desmejoras evaluar de nuevo otro tipo de modelo.

## ✅ Instrucciones para ejecutar el proyecto ##

Before starting 🏁, you need to have 
[Git](https://git-scm.com) and 
[Python](https://www.python.org/) installed.
[Pip](https://pip.pypa.io/en/stable/cli/pip_install/) installed.
## 🏁 Starting ##

```bash
# Clone this project
$ git clone https://github.com/marcelamu9/r5-ds-challenge_lmgarzon

# Access
$ cd r5-ds-challenge_lmgarzon

# Install dependencies
$ pip -r requirements.txt


```

&#xa0;




<a href="#top">Back to top</a>
