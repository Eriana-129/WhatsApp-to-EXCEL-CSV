# Convierte conversaciones de WhatsApp (.txt) a archivos Excel (.xlsx) y CSV | Convert WhatsApp conversations (.txt) to Excel (.xlsx) and CSV files

## Introducción / Introduction

De acuerdo con IBM, el Análisis de Sentimientos, puede definirse como el proceso de analizar grandes volúmenes de texto para determinar si expresa un sentimiento positivo, un sentimiento negativo o un sentimiento neutro (Disponible en https://www.ibm.com/mx-es/topics/sentiment-analysis). Así mismo, se refiere al estudio de las emociones y opiniones expresadas en mensajes digitales, almacenadas en archivos digitales (Disponible en https://www.unglobalpulse.org/wp-content/uploads/2023/12/e-analyticsguide2019.pdf). 

No obstante, para que pueda realizarse este análisis, primero se necesitan los archivos de origen, que muchas veces suelen venir de medios como X o Facebook. En su momento, necesitaba realizar un Análisis de Sentimientos de un chat grupal de WhatsApp, sin embargo, tan solo realizar el primer paso que era transformar los mensajes de WhatsApp, que estaban en formato .txt, a archivos que pudieran ser leidos en software como Excel, R, etc, suponían un gran reto que no encontré fácilmente en tutoriales. Así que comencé a ser autodidácta y resolver el problema.

**Por lo anterior, este repositorio tiene como objetivo presentar dos scripts de Python, para convetir un archivo .txt a excel y csv**, el primer script quita los formatos de negrita, cursiva, monoespaciado y tachado a los mensajes de una conversación de WhatsApp, creando un nuevo archivo .txt limpio. El segundo código, convierte ese nuevo .txt en un archivo .xlsx y .csv, con la ventaja de que mantiene los emoticones (o los convierte a versiones equivalentes) y permite que se conserven los mensajes largos en una sola celda de excel. Este código incluye una barra de progreso. Los archivos entregables .xlsx y .csv, tendrán cuatro columnas llamadas: "Fecha", "Hora", "Remitente", "Mensaje". 

En las pruebas que se realizaron del funcionamiento de los códigos, una conversación de más de 50,000 mensajes, se exportó a .csv y .xlsx en menos de 10 segundos. Cualquier observación que tengan, será bien recibida.

---------------------------------------------------

According to IBM, Sentiment Analysis can be defined as the process of analyzing large volumes of text to determine whether it expresses a positive, negative, or neutral sentiment (Available at https://www.ibm.com/mx-es/topics/sentiment-analysis). It also refers to the study of emotions and opinions expressed in digital messages stored in digital files (Available at https://www.unglobalpulse.org/wp-content/uploads/2023/12/e-analyticsguide2019.pdf).

However, for this analysis to be conducted, the source files are needed, which often come from platforms like X or Facebook. At one point, I needed to perform a Sentiment Analysis of a WhatsApp group chat; however, simply performing the first step, which was transforming the WhatsApp messages from .txt format to files that could be read in software like Excel, R, etc. presented a significant challenge that I couldn't easily find in tutorials. So, I began to teach myself and tried solve the problem.

**Therefore, this repository aims to present two Python scripts to convert a .txt file to Excel and CSV**. The first script removes bold, italic, monospaced, and strikethrough formatting from WhatsApp conversation messages, creating a clean new .txt file. The second script converts that new .txt file into .xlsx and .csv files, with the advantage of preserving emoticons (or converting them to equivalent versions) and allowing long messages to be kept in a single Excel cell. This code includes a progress bar. The deliverable .xlsx and .csv files will have four columns named:"Fecha", "Hora", "Remitente", "Mensaje" which can be translated to "Date," "Time," "Sender," and "Message".

In tests conducted with the code, a conversation of over 50,000 messages was exported to .csv and .xlsx in less than 10 seconds. Any feedback you have will be greatly appreciated.

## Disclaimer

Antes de continuar. Se aclara lo siguiente: 

**Uso bajo su propio riesgo:** Estos códigos se proporcionan "tal cual", sin garantía de ningún tipo. La autora no se hace responsable de ningún daño directo, indirecto, incidental, especial o consecuente que pueda surgir del uso o la incapacidad de usar este software. Al utilizar estos códigos, aceptas que lo haces bajo tu propio riesgo y que eres responsable de cualquier daño o pérdida resultante de su uso. 

---------------------------------------------------

Before proceeding, the following is clarified:

**Use at your own risk:** These scripts are provided "as is," without any warranty of any kind. The author is not responsible for any direct, indirect, incidental, special, or consequential damage that may arise from the use or inability to use this software. By using these scripts, you agree to do so at your own risk and accept responsibility for any damage or loss resulting from their use.

---------------------------------------------------

## Uso / Usage

Primero, descargarás los siguientes códigos:

- letters.py
- whatsapp_converter.py

Después necesitarás instalar las siguientes dependencias:

- tqdm: Para mostrar una barra de progreso en el procesamiento de datos.
- openpyxl: Para leer y escribir archivos Excel (.xlsx).

Luego tendrás que usar el primer código, de esta manera:
```
python letters.py <input_file>
```
Donde, <input_file> es el nombre de la conversación de WhatsApp .txt a la que se le van a quitar los formatos de negrita, cursiva, monoespaciado y tachado. **es obligatorio que pongas el <input_file>** puede tener el nombre que gustes. El archivo de salida será un txt con el nombre "new_XXXXXX.txt", donde XXXXXX es el nombre de tu archivo original.

Finalmente, usarás el segundo código de esta manera:
```
python whatsapp_converter.py <input.txt> <output.csv> <output.xlsx>
```
Donde:
- <input.txt> es el archivo de salida del primer código, es decir, "new_XXXXXX.txt"
- <output.csv> será el archivo de salida csv del segundo código, puedes elegir el nombre que quieras, siempre y cuando lleve la extensión .csv
- <output.xlsx> será el archivo de salida excel del segundo código, puedes elegir el nombre que quieras, siempre y cuando lleve la extensión .xlsx

---------------------------------------------------

First you will download the following scripts:

- letters.py
- whatsapp_converter.py

Then you will need to install the following dependencies:

- tqdm: To display a progress bar during data processing.
- openpyxl: To read and write Excel (.xlsx) files.

```
pip install tqdm openpyxl
```
Next you will need to use the first script like this:
```
python letters.py <input_file>
```
Where <input_file> is the name of the WhatsApp conversation .txt file from which bold, italic, monospace, and strikethrough formats will be removed. **It is mandatory to include the <input_file>** the file name is up to you. The output file will be named like this: "new_XXXXXX.txt", where XXXXXX is the original name of your file. 

Finally, you will use the second script like this:
```
python whatsapp_converter.py <input.txt> <output.csv> <output.xlsx>
```
Where:

- <input.txt> is the output file from the first script, that is, "new_XXXXXX.txt".
- <output.csv> will be the CSV output file from the second script; you can choose any name you want, as long as it has the .csv extension.
- <output.xlsx> will be the Excel output file from the second script; you can choose any name you want, as long as it has the .xlsx extension.

## Resultados / Results

Los archivos .csv y .xlsx deben de verse de esta manera:
| Fecha | Hora | Remitente | Mensaje |
|-------|------|-----------|---------|
|19/1/2024|9:31 p. m.| phone number XXXXXXXXXXXX|ABCDEFG|
|20/1/2024|10:20 a. m.| phone number XXXXXXXXXXXX|HIJKLM|
|21/1/2024|7:25 p. m.| phone number XXXXXXXXXXXX|NOPQRST|
|22/1/2024|4:48 p. m.| phone number XXXXXXXXXXXX|UVWXYZ|

