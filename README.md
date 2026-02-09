# Actividad A5.2 – Compute Sales

## Información general

Este repositorio contiene la solución de la **Actividad A5.2**, correspondiente al ejercicio **Compute Sales**, desarrollado en **Python**. El programa procesa archivos JSON, calcula el total de ventas de una empresa y cumple con el estándar **PEP-8**, verificado mediante **flake8** y **pylint**.

El programa:

* Se ejecuta desde **línea de comandos**
* Recibe **dos archivos JSON como parámetros**
* Maneja **errores sin detener la ejecución**
* Muestra resultados en **consola y archivo**
* Incluye el **tiempo de ejecución**
* No presenta errores en **flake8 ni pylint**

---

## Requisitos del sistema

Para ejecutar el programa se requiere:

* **Python 3.10 o superior**
* Consola o terminal (PowerShell, CMD o Terminal)
* Paquetes de análisis estático:

```bash
pip install flake8 pylint
```

---

## Estructura del repositorio

```
A01796900_A5.2/
│
├── compute_sales.py
├── README.md
├── SalesResults.txt
├── TC1.ProductList.json
├── TC1.Sales.json
├── TC2.Sales.json
├── TC3.Sales.json

```

---

## Programa – Compute Sales

### Descripción

El programa lee:

1. Un archivo JSON con el **catálogo de productos y precios**
2. Un archivo JSON con el **registro de ventas**

Con esta información, calcula el **total de ventas**, considerando el precio de cada producto y su cantidad. Si un producto no existe en el catálogo, se muestra un mensaje de error en consola y el programa continúa su ejecución.

El resultado se presenta de forma legible para el usuario.

---

### Ejecución

El programa se ejecuta desde la raíz del proyecto con el siguiente comando:

```bash
python compute_sales.py priceCatalogue.json salesRecord.json
```

Ejemplo de ejecución con casos de prueba:

```bash
python compute_sales.py TC1.ProductList.json TC1.Sales.json
python compute_sales.py TC1.ProductList.json TC2.Sales.json
python compute_sales.py TC1.ProductList.json TC3.Sales.json
```

Cada ejecución **sobrescribe el archivo `SalesResults.txt`** con los resultados correspondientes al caso ejecutado.

---

### Salida

* Resultados mostrados en consola
* Archivo generado/actualizado: `SalesResults.txt`
* Tiempo total de ejecución incluido en ambos

Ejemplo en consola:

```
SALES RESULTS
====================
Total Sales: 2481.86
Execution Time (seconds): 0.00031
```

---

## Casos de prueba

Se ejecutaron **tres casos de prueba (TC1, TC2 y TC3)** proporcionados en la actividad.

* Los resultados obtenidos coinciden con los valores esperados
* En el **TC3** se muestran mensajes de error por productos no encontrados, cumpliendo con el manejo de errores solicitado

## Análisis estático

El programa fue validado con las siguientes herramientas:

### flake8

Sin errores ni advertencias.

### pylint

```
Your code has been rated at 10.00/10
```

Esto garantiza el cumplimiento del estándar **PEP-8** y buenas prácticas de programación.

---

## Autor

**Nombre:** Arturo González Corona
**Matrícula:** A01796900
**Actividad:** A5.2 – Pruebas y Calidad de Software
