# Encuestas por voz sobre IP - Aplicaciones TCP/IP

Se desarrolla e implementa trabajo final para la cátedra de Aplicaciones TCP/IP a fin de llevar adelante una solución con los conceptos abordados en ella.

## Introducción

Se trata del desarrollo e implementación de un sistema de *encuestas por voz, adquisición, procesamiento y visualización de los datos* correspondientes a los resultados de las encuestas en cuestión.

## Sobre este documento

**“Encuestas por voz sobre IP”** se produce en el contexto de la cátedra Aplicaciones TCP/IP, de la carrera de Ing. en Telecomunicaciones, en la Universidad Nacional de Río Cuarto por Bibiana Rivadeneira.

Se encuentra bajo la licencia:

[![](https://i.imgur.com/bduHyZr.png)](https://creativecommons.org/licenses/by-sa/4.0/deed.es)

Este es un resumen legible por humanos (y no un sustituto) de la licencia. Advertencia.

Usted es libre de:
* **Compartir** — copiar y redistribuir el material en cualquier medio o formato
* **Adaptar** — remezclar, transformar y construir a partir del material para cualquier propósito, incluso comercialmente.

* La licenciante no puede revocar estas libertades en tanto usted siga los términos de la licencia

Bajo los siguientes términos:

* **Atribución** — Usted debe dar crédito de manera adecuada, brindar un enlace a la licencia, e indicar si se han realizado cambios. Puede hacerlo en cualquier forma razonable, pero no de forma tal que sugiera que usted o su uso tienen el apoyo de la licenciante.
* No hay restricciones adicionales — No puede aplicar términos legales ni medidas tecnológicas que restrinjan legalmente a otras a hacer cualquier uso permitido por la licencia.
***

**ÍNDICE DE CONTENIDOS**

[TOC]

## Objetivos

* Aplicar y reforzar conceptos de la pila de protocolos TCP/IP  a una solución tecnológica.
* Desarrollar e implementar un sistema de encuestas por voz que permita adquirir, procesar y visualizar datos referentes a dichas encuestas.
* Emplear tecnologías de código abierto.

## Resumen

Se trata de un sistema de **encuestas por voz**, más específicamente a través de llamadas telefónicas cursadas sobre el **protocolo de internet**, adquisición de los datos registrados durante las encuestas en cuestión, (DTMF) **procesamiento y visualización de los mismos en un portal web**.

## Palabras clave

debian, docker, asterisk, freepbx, ivr, miscapp, sip, rtp, udp, python, flask, api, dash, wireshark

### Diagrama

El sistema se representa mediante el siguiente diagrama simbólico:

![](https://i.imgur.com/BZ6xOij.png)
*Diagrama simbólico sistema de encuestas por VoIP*

* **Cliente**: Terminal telefónica para cursar la llamada de voz sobre IP y comenzar una interacción hombre-máquina.
* **Archivos de sonido**: Grabaciones predefinidas para los mensajes con los que interactúa el cliente.
* **Lógica de llamadas**: Los archivos de sonido se reproducen siguiendo una lógica de decisiones simples en función de las respuestas del cliente.
* **Servidor VoIP**: Cursa las llamadas por VoIP y realiza la adquisición de los datos resultados de las encuestas.
* **Servidor Web**: En el que se procesan los datos de los resultados y se generan gráficos amigables con estadísticas de los mismos, a visualizar en un portal web.

#### Tecnologías

Tecnologías a implementar en el sistema:

* **[Docker](https://www.docker.com) client e [imagen](https://github.com/flaviostutz/freepbx)**: Contenedor con distribución [Debian](https://www.debian.org/), [Asterisk](https://www.asterisk.org), [FreePBX](https://www.freepbx.org), módulos [IVR](https://en.wikipedia.org/wiki/Interactive_voice_response).
* **[Asterisk 15](https://www.asterisk.org)**: Distribución open source para soluciones VoIP y lógica por voz.
* **[FreePBX 14](https://www.freepbx.org)**: Interfáz gráfica basada en web (open source) para administrar Asterisk.
* **[Módulos IVR](https://en.wikipedia.org/wiki/Interactive_voice_response)**: *(Interactive Voice Response)*
* **[MiscApplications](https://github.com/FreePBX/miscapps)**: Módulo requerido para enrutar las llamadas a la encuesta.
* **[Zoiper](https://www.zoiper.com/)**: Cliente de VoIP disponible para GNU/Linux y Android, entre otros.
* **[Flask API](https://hackmd.io/yjWHcWePSG-HLwWh46FyPA?both)**: Framework open source escrito en Python para crear APIs.
* **[Dash](https://plot.ly/products/dash/)**: Biblioteca de Python para visualización amigable e interactiva de datos a partir de json.

## Descripción

Se instala, configura e implementa un sistema de encuestas por voz sobre el protocolo de internet ([IVR](https://en.wikipedia.org/wiki/Interactive_voice_response) en VoIP). Se describen a continuación las diferentes partes que componen el sistema, respondiendo al diagrama antes expuesto.

### Servidor

Una distribución GNU/Linux [Debian](https://www.debian.org/) hostea al servidor [Asterisk](https://www.asterisk.org/) *versión 15* de VoIP. Se emplea [FreePBX](https://www.freepbx.org) *(Interfáz gráfica web para administración de Asterisk)*, versión 14.

Se emplean módulos [IVR](https://en.wikipedia.org/wiki/Interactive_voice_response) para brindar la posibilidad de interacción con mensajes automáticos de voz y reportes de respuestas de los usuarios, más específicamente de la señalización, de los tonos DTMF.

### Cliente

### Lógica

A partir de un conjunto de archivos de audio, se reproducen ante los siguientes eventos:

* **Llamada entrante**: Mensaje de bienvenida
* **Registrar una encuesta**: Mensaje de encuesta y las opciones correspondientes a la respuesta.
    * **Opción para registrar encuesta**
    * **Opción para repetir mensaje**
    * **Opción para salir**
* **Respuesta**: Mensaje de respuesta registrada, Mensaje de respuesta no registrada, mensaje de salida.

## Diseño

El diseño del sistema puede ser descripto en "capas" correspondientes a los módulos que componen el sistema de encuestas por voz sobre el protocolo de internet.

Se dockerizan las tecnologías a implementar sobre una distribución GNU/Linux.

### Capa 1: Docker

Cliente docker, corriendo sobre un Debian 10, capa de abstracción para desplegar en contenedores las herramientas requeridas para el servidor de VoIP.

### Capa 2: Asterisk

Servidor de VoIP que proporciona funcionalidades de una central telefónica (PBX) para llamadas de voz sobre el protocolo de internet.

### Capa 3: IVR, MiscApp

Módulos de respuestas de voz interactiva y para desvío de llamada de extensión a la encuesta.

### Capa 4: Procesamiento y visualización

Se diseña e implementa una API con python y flask para servir los resultados de las encuestas, extraídos del logfile de Asterisk, mientras que se ejecuta una aplicación web con dash para visualizar los mismos.

## Procedimiento

El entorno de desarrollo vive en una distribución GNU/Linux, Debian o basada en Debian.

### Requisitos previos

#### [Docker](https://www.docker.com/)

![](https://i.imgur.com/nb10yZv.png)

1. **El primer paso es `eliminar instalaciones previas de docker`, en una terminal:**

```sh
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get autoremove
sudo apt-get autoclean
```

Si no había instalaciones existentes de docker, la terminal debería mostrarte esto:

```sh
Reading package lists... Done
Building dependency tree
Reading state information... Done
Package 'docker-engine' is not installed, so not removed
```

**2. Obtener algunas herramientas previas, en la terminal:**

```sh
sudo apt-get update
```

Al finalizar, escribir:

```sh
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
```

**3. Agregar la GPG key oficial de docker:**

```sh
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable
OK
```

```sh
sudo apt-key fingerprint 0EBFCD88

pub   4096R/0EBFCD88 2017-02-22
      Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid                  Docker Release (CE deb) <docker@docker.com>
sub   4096R/F273FCD8 2017-02-22
```

```sh
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

**4. Instalar docker-ce**

```sh
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

**5. Elegir la versión de instalación**

Listar las versiones disponibles para su instalación
```sh
apt-cache madison docker-ce
```

```sh
 docker-ce | 5:18.09.6~3-0~debian-buster | https://download.docker.com/linux/debian buster/stable amd64 Packages
 docker-ce | 5:18.09.5~3-0~debian-buster | https://download.docker.com/linux/debian buster/stable amd64 Packages
 docker-ce | 5:18.09.4~3-0~debian-buster | https://download.docker.com/linux/debian buster/stable amd64 Packages
 docker-ce | 5:18.09.3~3-0~debian-buster | https://download.docker.com/linux/debian buster/stable amd64 Packages
 docker-ce | 5:18.09.2~3-0~debian-buster | https://download.docker.com/linux/debian buster/stable amd64 Packages
 docker-ce | 5:18.09.1~3-0~debian-buster | https://download.docker.com/linux/debian buster/stable amd64 Packages
 docker-ce | 5:18.09.0~3-0~debian-buster | https://download.docker.com/linux/debian buster/stable amd64 Packages
 docker-ce | 18.06.3~ce~3-0~debian | https://download.docker.com/linux/debian buster/stable amd64 Packages
 docker-ce | 18.06.2~ce~3-0~debian | https://download.docker.com/linux/debian buster/stable amd64 Packages
 docker-ce | 18.06.1~ce~3-0~debian | https://download.docker.com/linux/debian buster/stable amd64 Packages
 docker-ce | 18.06.0~ce~3-0~debian | https://download.docker.com/linux/debian buster/stable amd64 Packages
 docker-ce | 18.03.1~ce-0~debian | https://download.docker.com/linux/debian buster/stable amd64 Packages
 docker-ce | 18.03.0~ce-0~debian | https://download.docker.com/linux/debian buster/stable amd64 Packages
 docker-ce | 17.12.1~ce-0~debian | https://download.docker.com/linux/debian buster/stable amd64 Packages
 docker-ce | 17.12.0~ce-0~debian | https://download.docker.com/linux/debian buster/stable amd64 Packages
```
**6. ¡Instalar docker!**

Para este ejemplo de instalación se usa `5:18.09.6~3-0~debian-buster` (la primera opción). En el siguiente comando se reemplaza `<VERSION_STRING> docker-ce-cli=<VERSION_STRING>` la versión deseada:

```sh
sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io
```

```sh
sudo apt-get install docker-ce=5:18.09.6~3-0~debian-buster docker-ce-cli=5:18.09.6~3-0~debian-buster containerd.io
```

Para verificar la instalación ingresar el siguiente comando en la terminal:

```sh
sudo docker run hello-world
```

Si todo está bien se muestra en la terminal:

```sh
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

#### [Git](https://git-scm.com/)

![](https://i.imgur.com/PdDs6qR.png)

```
sudo apt install git
```

### Asterisk + FreePBX + Módulos IVR

#### Descargar y levantar la imagen

```sh
git clone https://github.com/flaviostutz/freepbx
cd freebpx
sudo docker-compose up -d
```
Ir a [http://localhost/](http://localhost/)

![](https://i.imgur.com/klhKNJM.png)
*FreePBX*

#### Configuración básica en FreePBX

Setear un nombre de usuario y contraseña, email e iniciar la configuración.

![](https://i.imgur.com/qEGxgUj.png)
*Configuración FreePBX*

##### Agregar extensiones y test básico

Se agregan dos extensiones PJSIP (usuarios) en la red de área local para llevar a cabo un test de funcionamiento inicial del servidor.

###### Breve descripción de PJSIP

PJSIP es una librería de código abierto para la comunicación multimedia, escrita en `C` que implementa los protocolos SIP, SDP, RTP, entre otros.

En el menú `Aplicattions -> Extensions`, en la pestaña `PJSIP Extensions` `Add Extension`. Se setean parámetros para dos usuarios de testing:

![](https://wiki.freepbx.org/download/attachments/28770747/new-pjsip.png?version=1&modificationDate=1441991403000&api=v2&effects=border-simple,blur-border)

![](https://wiki.freepbx.org/download/attachments/28182079/general-ext-settings.png?version=1&modificationDate=1441197323000&api=v2&effects=border-simple,blur-border)

Usuario 1:
* User Extension: 101
* Display Name: bibiana
* Outbound CID:
* Secret: 101

Usuario 2:
* User Extension: 102
* Display Name: lucas
* Outbound CID:
* Secret: 102

Para averiguar la dirección IP de la LAN que corresponde al servidor de VoIP:

```sh
ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp9s0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN group default qlen 1000
    link/ether 74:86:7a:fe:37:56 brd ff:ff:ff:ff:ff:ff
3: wlp6s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 9c:2a:70:d4:07:95 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.29/24 brd 192.168.1.255 scope global dynamic noprefixroute wlp6s0
       valid_lft 83313sec preferred_lft 83313sec
    inet6 fdc8:94bb:2fce:7c00:62f0:587d:3bb1:5034/64 scope global dynamic noprefixroute
       valid_lft 6943sec preferred_lft 3343sec
    inet6 fe80::cebd:1b6c:b719:3da4/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
```

La interfáz de red es la **wlp6s0** y su dirección IPv4 es **192.168.1.29**. Que corresponde al *dominio* para los clientes.

###### Zoiper en Android

Se emplea el cliente de VoIP ![](https://www.zoiper.com/) para ambos usuarios y se inicia una llamada.

![](https://i.imgur.com/R7GC86m.png)

![](https://i.imgur.com/UDLvzld.png)

![](https://i.imgur.com/G2XRkKr.png)
*Seleccionar la opc Skip*

![](https://i.imgur.com/pzkxK2x.png)

![](https://i.imgur.com/vc4uEFC.png)

###### Zoiper en Debian

Se realizan los mismos pasos de configuración

![](https://i.imgur.com/gARz0lF.png)

##### Misc Apps

Se requiere el módulo [miscapps](https://github.com/FreePBX/miscapps) para dirigir las llamadas hacia una extensión, a la encuesta.

```bash
git clone https://github.com/FreePBX/miscapps
tar -cvzf miscapps.tar.gz miscapps
```

En `Admin` -> `Module Admin`

![](https://i.imgur.com/CWpR85H.png)

`Upload modules` y elegir el tar.gz recién creado.

En `Module Admin`, elegir `Misc Apps` y click en `Install`.
##### Importación de announcements

Se crean o descargan los mensajes de voz con los que interactúa el usuario en formatos de audio y de 8bits.

*Se generan audios a partir de un [conversor online de texto a voz](http://www.fromtexttospeech.com/)*

En el menú `System recording`, click en `Announcements`, en el menú `Applications`, click en `Announcements`:

* `+Add recording`, setear un nombre y (opc) descripción del mensaje.
* Importar el archivo de sonido.
* Las opciones restantes permanecen en sus valores por defecto.

Repetir el procedimiento tantas veces como mensajes de voz requiera la aplicación.

#### Crear y configurar una aplicación IVR

Se crea, configura e implementa la aplicación IVR según la [wiki de FreePBX](https://wiki.freepbx.org/display/FPG/IVR+Module+User+Guide).

En el menú `Aplicaciones`, click en `IVR`:

![](https://i.imgur.com/Zv2zSYw.png)

* `+Add IVR`, setear un nombre y (opc) descripción de la aplicación.
* Setear opciones adicionales de la aplicación.

![](https://i.imgur.com/jl2Lxjo.png)

* **IVR Name**: El sabor preferido de helado.
* **IVR Description**: Encuesta sobre preferencias en sabores de helado, para determinar el preferido de la comunidad local.
* **Announcement**: Bienvenida *(announcement creado previamente)*.
* **Direct Dial**: *(Permite al usuario marcar la extensión con la que se desea comunicar directamente, dada la aplicación, se deshabilita.)*  Disabled
* **Timeout**:  10
* **Invalid Retries**:  3
* **Invalid Retry Recording**:
* **Append Original Announcement**: *(Ante ingresos incorrectos del usuario, se reproduce el anuncio de bienvenida)* - ✔
* **Invalid Recording**: SorryAllDone
* **Invalid Destination**: Terminate Call:Hangup
* **Timeout Retries**: 2
* **Timeout Retry Recording**: SorryDidNotHearAnythingTryAgain
* **IVR Entries:** *(ver tabla)*

#### IVRs y announcements

Las aplicaciones IVR, sus entries, announcements y destinos definen la lógica de la encuesta:

##### 1. Bienvenida

|         IVR                  | Announcement |
|                     -------- |     -------- |
| Bienvenida sabores de helado |   Bienvenida |


| Entry |  Destino     |
| ----  | --------     |
| 1     | IVR Género   |

##### 2. Género

| IVR    | Announcement |
| ------ | --------     |
| Género | Género       |

| Entry |         Destino       |
| ------| --------              |
| 1     | Announcement Femenino |
| 2     | Announcement Masculino|
| 3     | Announcement No especifico |

| Announcement | Destino  |
| --------     | -------- |
| Femenino     | IVR Edad |
| Masculino    | IVR Edad |
| No especifico| IVR Edad |

##### 3. Edad

| IVR    | Announcement |
| ------ | --------     |
| Edad   | Edades       |

| Entry |         Destino    |
| ------| --------           |
| 1     | Announcement 18-21 |
| 2     | Announcement 22-30 |
| 3     | Announcement 30-40 |

| Announcement | Destino               |
| --------     | --------              |
| 18-21        | IVR Sabores de helado |
| 22-30        | IVR Sabores de helado |
| 30-40        | IVR Sabores de helado |

##### 4. Sabores

| IVR    | Announcement |
| ------ | --------     |
| Sabores| Sabores      |

| Entry |         Destino         |
| ------| --------                |
| 1     | Announcement chocolate  |
| 2     | Announcement crema      |
| 3     | Announcement frutilla   |
| 4     | Announcement mascarpone |

| Announcement | Destino |
| --------     | --------|
| chocolate    | Hung up |
| crema        | Hung up |
| frutilla     | Hung up |
| mascarpone   | Hung up |

#### Misc App

En `Applications` -> `Misc Applications` -> `Àdd`

![](https://i.imgur.com/shHY0ml.png)

### Adquisición de datos

Las opciones seleccionadas por los usuarios se corresponden a las señales **DTMF** *(Dual-Tone Multi-Frequency)*, para registrar los mismos `Settings` -> `Asterisk Logfile Settings` y setear en `On` DTMF.

![](https://i.imgur.com/vHwoMqd.png)

Las llamadas así como señalización, se registran en el `logfile` de Asterisk, `Reports` -> `Asterisk Logfiles`:

![](https://i.imgur.com/IO7AsYl.png)

Más específicamente, el announcement que se reproduce, corresponde a las opciones seleccionadas por los usuarios y por ende al registro de la encuesta. Se deben "parsear" los datos del log.

### Procesamiento de datos

Se contabilizan las elecciones de los participantes según se registren, luego del establecimiento de la llamada a la extensión que redirecciona a la encuesta, la reproducción de los announcements que se corresponden con las entries antes configuradas, por ejemplo, la siguiente línea:

`[2019-06-11 20:02:24] VERBOSE[4048][C-00000001] file.c: <PJSIP/101-00000000> Playing 'custom/0-bienvenida.slin' `

implica el establecimiento de la llamada, las siguientes:

```
[2019-06-11 20:02:29] VERBOSE[4048][C-00000001] file.c: <PJSIP/101-00000000> Playing 'custom/2-genero.slin' (language 'en')
[2019-06-11 20:02:35] VERBOSE[4048][C-00000001] file.c: <PJSIP/101-00000000> Playing 'custom/2-1-femenino.slin' (language 'en')
```

#### Logfile

implican la elección de género "femenino" por parte de un usuario. Por lo anterior, y conociendo los announcements, se obtiene el logfile (desde el container) como sigue:

```bash
docker ps # para obtener el ID del container
docker exec -it 98fe1e53368f bash # para acceder a la consola
scp /var/log/asterisk/full bibiana@192.168.0.29:freepbx
```

#### API

Se genera una API a partir del procesamiento del archivo "full" con `flask-api`, detectando línea por línea las palabras "playing" y las que correspondan a los announcement de la señalización enviada por el usuario, se genera un diccionario con edades, géneros y sabores elegidos, y se sirven en la api.

```bash
pip install flask-api
```

```python
import json
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

f = open('full', 'r')

playing = []
res_encuesta = {'edades': {'18-21': 0, '21-30': 0, '30-40': 0},
               'géneros': {'F': 0, 'M': 0, 'NE': 0},
               'sabores': {'chocolate': 0, 'crema': 0, 'frutilla': 0, 'mascarpone': 0}}

for linea in f:
    if 'Playing' in str(linea):
        playing.append(linea)

for elem in playing:
    if '18-21' in elem:
        res_encuesta['edades']['18-21'] += 1
    elif '21-30' in elem:
        res_encuesta['edades']['21-30'] += 1
    elif '30-40' in elem:
        res_encuesta['edades']['30-40'] += 1
    if 'femenino' in elem:
        res_encuesta['géneros']['F'] += 1
    elif 'masculino' in elem:
        res_encuesta['géneros']['M'] += 1
    elif 'no-especifico' in elem:
        res_encuesta['géneros']['NE'] += 1
    if 'chocolate' in elem:
        res_encuesta['sabores']['chocolate'] += 1
    elif 'crema' in elem:
        res_encuesta['sabores']['crema'] += 1
    elif 'mascarpone' in elem:
        res_encuesta['sabores']['mascarpone'] += 1

@app.route('/')
def resultado_encuesta():
    return res_encuesta

if __name__ == '__main__':

    # Run app
    app.run(host="localhost",
            port=8000,
            debug=True)
```

```bash
python api.py
```

### Visualización

Se emplea la librería `dash` para visualizar los datos servidos por la api, se realiza un request a la misma, se obtiene el json de los resultados, y se plotean gráficos de barra con las keys y values en los ejes x e y correspondientemente, un dropdown permite visualizar tanto los sabores como edades y géneros.

```bash
pip install dash
```

```python
# coding: utf-8

import dash
import dash_core_components as dcc
import dash_html_components as html

import requests

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
dash_app = dash.Dash(__name__)#, external_stylesheets=external_stylesheets)
dash_app.config['suppress_callback_exceptions']=True

url_resultados = 'http://localhost:8000/'
req_resultados = requests.get(url_resultados)
resultados = req_resultados.json()

opciones = []
for key in resultados.keys():
    opciones.append({'label': key, 'value': key})

dash_app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=opciones,
        placeholder='Seleccione una opción'
    ),
    dcc.Graph(id='my-graph'),
    dcc.Interval(
            id='interval-component',
            interval=1000, # in milliseconds
            n_intervals=0
        )
#    html.Div(id='output-container')
])

@dash_app.callback(
    dash.dependencies.Output('my-graph', 'figure'),
    [dash.dependencies.Input('my-dropdown', 'value')])

def update_graph(selected_dropdown_value):
    res = resultados[selected_dropdown_value]
    x = list(res.keys())
    y = list(res.values())

    return {
        'data': [
            {
            'x': x,
            'y': y,
            'name': selected_dropdown_value,
            'marker': {'size': 1},
            'showlegend': True,
            'type': 'bar'
            }
        ]
    }

@dash_app.callback(
    dash.dependencies.Output('output-container', 'children'),
    [dash.dependencies.Input('my-dropdown', 'value')])
def update_output(value):
    return 'Usuario: "{}"'.format(value)

if __name__ == '__main__':
    dash_app.run_server(
        host="localhost",
        port=8001,
        debug=True)
```

```bash
python dash_app_encuesta.py
```

Se accede a la API desde [http://localhost:8000](http://localhost:8000) y [http://localhost:8001](http://localhost:8001).

## Resultados

Se realizan llamadas desde clientes a la central, marcando la extensión correspondiente a la encuesta, se registran los resultados en `Wireshark`, empleando la opción `Telephony` -> `VoIP calls` -> `Flow Sequence`

```bash
sudo apt install wireshark
sudo wireshark
```

![](https://i.imgur.com/i56ZODo.png)

*Captura llamada de VoIP en Wireshark*

Se pueden observar los paquetes correspondientes al protocolo **SIP** (Session Initiation Protocol), -capas 5, 6 y 7- de señalización, empleado para iniciar, mantener y terminar sesiones en tiempo real, en este caso de voz.

Capturando todos los paquetes entre las IP correspondientes al servidor de VoIP y el cliente:

![](https://i.imgur.com/rHeZlQA.png)
*Captura con filtro Ip scr e IP dst en Wireshark*

Se observa el protocolo **RTP** *(Real Time Protocol)* involucrado -capa 7-, así como el protocolo de transporte **UDP**, típicamente implementado en comunicaciones multimedia en tiempo real, sin corrección de errores ni retransmisión de paquetes.

### API

![](https://i.imgur.com/jXbVZZ0.png)
[http://localhost:8000](http://localhost:8000)

### Visualización

![](https://i.imgur.com/2qEQAIJ.png)

![](https://i.imgur.com/IQzy17m.png)

![](https://i.imgur.com/FaDeOb6.png)

[http://localhost:8001](http://localhost:8001)

## Conclusión

La elección y combinación de herramientas open source o libres forman satisfactoriamente un sistema de encuestas, empleando la implementación y configuración de aplicaciones IVR pensadas para menú, con el correspondiente procesamiento de datos. Se logra entonces la puesta en marcha de un servidor de voz sobre IP, módulos de interacción por voz, adquisición y visualización de datos de la encuesta.

## Proyección

Siendo el sistema un prototipo, se consideran las siguientes mejoras o agregados:

* Obtener un número público para trascender la red LAN.
* Considerar encuestas truncas en el procesamiento de datos.
* Correlacionar géneros, edades y sabores para un mejor análisis de los resultados.

## Referencias

* [Documentación Docker](https://docs.docker.com/)
* [Imagen docker con Asterisk + FreePBX + IVR](https://github.com/flaviostutz/freepbx)
* [Documentación Asterisk](https://www.asterisk.org/community/documentation)
* [Wiki FreePBX](https://wiki.freepbx.org)
* [Flask API](https://www.flaskapi.org/)
* [Documentación Dash](https://dash.plot.ly/)
