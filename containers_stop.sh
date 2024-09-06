#!/bin/bash
usuario_actual=$USER
container_adobe=${usuario_actual}_adobe
container_chat=${usuario_actual}_chat
container_ui=${usuario_actual}_ui

echo "Deteniendo y eliminando los contenedores"
docker rm -f ${container_adobe}
docker rm -f ${container_chat}
docker rm -f ${container_ui}

echo "Contenedores detenidos y eliminados correctamente."