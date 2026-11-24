# Memòria Colonial — código y web

Exportación de la versión publicada el 24 de noviembre de 2026.
Commit de origen: 1577c50290afc5b4b6cca540aec48e97f1f25ccd

## Instalar
Publicar el contenido de dist/ con Nginx, Apache o Caddy y HTTPS. No requiere backend, base de datos ni compilación. Las rutas son relativas. mobile.html permite revisar el diseño en un marco de móvil.

## Editar
Los HTML, CSS y JS están en dist/. Los datos están en dist/data-es.json y dist/data-ca.json. content/ conserva el documento de investigación y los scripts de generación. Para regenerar los datos y traducciones: Python 3 y python build.py. Editar content/source-es.json para cambios persistentes en español y content/translate-ca.py para la traducción catalana. El generador de interfaz content/build-ui.py toma los textos españoles de dist/index.html y contiene los catalanes.

## Dependencias externas
Leaflet desde unpkg; cartografía OpenStreetMap; WebLLM y modelo Qwen descargados al navegador al activar la IA local. El chatbot online no está configurado. La voz utiliza speechSynthesis y voces locales del dispositivo.

## GitHub
Este ZIP no incluye credenciales, historial Git ni la configuración de identidad del alojamiento anterior. Descomprimir e importar en el repositorio elegido. Conservar dist/ y content/ para continuar el desarrollo. Revisar los derechos de documentos, referencias y logotipos antes de elegir una licencia pública.
