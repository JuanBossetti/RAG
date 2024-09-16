#!/bin/bash
# IMPORTANTE! Asegurarse tener una BD ya creada antes de correr este script.
# El objetivo de este script es que nos permita levantar rapidamente un set de contenedores que son requeridos para RAG en versionados especificos y probar rapidamente el circuito.
# -- Explicacion de procedimiento --
# Con el script de "images_update.sh" vas a crear tus versiones internas de las apis de RAG.
# Indicas las versiones que cada api que quieras levantar en conjunto. ej: version, 1 de adobe, 2 de chat y 4 de ui.
# Indicas el puerto externo para acceder a la api de procesamiento de documento.
# Indicas el puerto externo para acceder por ui al chatbot.
# Indicas el nombre de red que queres para este conjunto de contenedores. (Es importante para que se conozcan entre si, no es recomendable meterlos en una red ya existente)

usuario_actual=$USER

# Lista las imágenes que comienzan con el nombre del usuario y mostrar sus tags
docker images --format "{{.Repository}}:{{.Tag}}" | grep "^$usuario_actual" | grep -v ":latest" | while read -r image; do
  echo "$image"
done

read -p "ADOBE | TAG de imagen - [default: latest]: " tag_adobe
tag_adobe=${tag_adobe:-latest}

# TODO: Repensar el lugar de esto, el script esta en otra carpeta, fuera del repositorio
echo
if ! python3 /mnt/datos/desarrollo/development_tools/scripts_container/list_ports.py; then    
    echo "No se puede listar los puertos porque no se encuentra el script."
fi

read -p "ADOBE | puerto externo: " port_adobe
if [ -z "$port_adobe" ]; then
  echo "Error: No se ingresó el puerto externo de la API ADOBE. El script terminará."
  exit 1
fi

echo
read -p "CHAT | TAG de imagen - [default: latest]: " tag_chat
tag_chat=${tag_chat:-latest}

echo
read -p "UI | TAG de imagen - [default: latest]: " tag_ui
tag_ui=${tag_ui:-latest}

# TODO: Repensar el lugar de esto, el script esta en otra carpeta, fuera del repositorio
echo
if ! python3 /mnt/datos/desarrollo/development_tools/scripts_container/list_ports.py; then    
    echo "No se puede listar los puertos porque no se encuentra el script."
fi

read -p "UI | puerto externo: " port_ui
if [ -z "$port_ui" ]; then
  echo "Error: No se ingresó el puerto externo de la API UI. El script terminará."
  exit 1
fi

echo
echo "Listando redes Docker existentes:"
docker network ls --format "{{.Name}}" | grep "^$usuario_actual"

read -p "Ingrese el nombre de la red Docker que desea usar o crear: " nombre_red

if [ -z "$nombre_red" ]; then
  echo "Error: No se ingresó el nombre de la red. El script terminará."
  exit 1
fi

network_name="${usuario_actual}_${nombre_red}"

if ! docker network ls | grep -q "$network_name"; then
  echo "Creando la red Docker $network_name"
  docker network create "${network_name}"
fi

#TODO: Como hacemos con la bd? Conectada aparte? No podemos meterlos en la misma red de la bd, se van a pisar.

echo
echo
# ---  1ro | contenedor de adobe --- 
docker run -d --name ${usuario_actual}_adobe --env-file .env -v /mnt/datos/desarrollo/documentos/rag/:/app/docs -e PORT=7001 -p ${port_adobe}:7001 --network $network_name ${usuario_actual}_adobe:${tag_adobe}
# --- 2do | contenedor de chat ---
# Este contenedor no se expone hacia afuera, es interno de la red.
docker run -d --name ${usuario_actual}_chat --env-file .env -e PORT=7000 --network $network_name ${usuario_actual}_chat:${tag_chat}
# --- 3ro | contenedor de ui ---
# Ya se setea la variable de entorno para conectarse al servicio de chat.
docker run -d --name ${usuario_actual}_ui -e API_CHAT=http://${usuario_actual}_chat:7000/rag-api -p ${port_ui}:8501 --network $network_name ${usuario_actual}_ui:${tag_ui}


echo "Todos los contenedores han sido levantados"
