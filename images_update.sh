#!/bin/bash
# IMPORTANTE! Para ejecutar este script simpre ejecutarlo con el puntero en el lugar que se encuentra el mismo.
# El objetivo de este script es permitirnos actualizar rapidamente las imagenes que involucran al circuito de RAG y nos deje hacer la prueba sobre contenedores lo mas rapido posible.
#  -- Explicacion de procedimiento --
# Cada usuario tendra su version interna individual de trabajo. ej: 1
# Las imagenes se crearan con el nombre de nuestro usuario y el nombre de la api. ej: jbossetti_chat:1, jbossetti_adobe:1, jbossetti_ui:1
# La idea es solo cambiar de version interna cuando queramos hacer un punto de quiebre entre una y otra. 
# ej: si estamos trabajando en la version interna 1 y solo hacemos cambios sobre api de chat, no creamos una version nueva, actualizamos version 1 y probamos, docker es inteligente y solo actualiza la imagen de la api chat.
# -- Mantenimiento --
# A medida que dejemos versiones atras ir borrandolas, las imagenes son pesaditas.
# TODO: Ir tageando el repositorio para el creado de imagenes por version. O tener un repositorio de imagenes.

usuario_actual=$USER

# Listar las imágenes que comienzan con el nombre del usuario y mostrar sus tags
docker images --format "{{.Repository}}:{{.Tag}}" | grep "^$usuario_actual" | grep -v ":latest" | while read -r image; do
  echo "$image"
done

read -p "TAG nuevo para actualizar los contenedores, recordar que se actualizara adobe, chat y ui: " NEW_TAG

if [ -z "$NEW_TAG" ]; then
  echo "Por favor, proporciona un nuevo tag para las imágenes."
  exit 1
fi

# Carpetas que contienen los Dockerfiles
DIRECTORIES=("core/adobe" "core/chat" "ui")

# Nombres de las imágenes correspondientes a cada carpeta
IMAGES=("${usuario_actual}_adobe" "${usuario_actual}_chat" "${usuario_actual}_ui")

# Iterar sobre las carpetas e imágenes
for i in "${!DIRECTORIES[@]}"; do
  DIR=${DIRECTORIES[$i]}
  IMAGE=${IMAGES[$i]}
  
  echo "Construyendo imagen en $DIR con el nombre $IMAGE:$NEW_TAG..."
  
  # Construir la imagen
  docker build -t "$IMAGE:$NEW_TAG" "$DIR"
  
  # Cargamos como ultima version la creada actualmente
  docker tag "$IMAGE:$NEW_TAG" "$IMAGE:latest"
  
  echo "Imagen $IMAGE:$NEW_TAG construida y etiquetada como ultima version."
done

echo "Todas las imágenes han sido actualizadas con el nuevo tag: $NEW_TAG"