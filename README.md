# Boveda
Esta es la bóveda de datos del equipo de datos de la delegada para la eficiencia administrativa y presupuestal. Se encuentra alojado en un servidor virtual en infraestructura propia de la entidad y hace uso de Docker para brindar aislamiento y atomicidad a cada uno de los componentes, mientras a su vez se facilita el backup.

## Estructura
Operativamente está constituida por 3 grandes componentes:
1. Componente almacenamiento crudo de archivos con sFTP.
2. Componente capa de traducción de FTP a SQL
3. COmponente Postgres SQL para datos ya estructurados y limpios.

### Componente sFTP
Este contenedor utiliza vsftpd, un cliente web para vsftpd y finalmente una api en python para el fetching automático de archivos con periodicidad.

1. Contenedor vsftpd
1. Contenedor API fetch
2. Contenedor monstaFTP para UI.

### Componente capa de traducción
Este componente está en construcción, motivo por el que aún sus métodos son abstractos y aún no cuenta con componentes claramente definidos. La intención es que haciendo uso de APIs u otros mecanismos, se logre traducir archivos excel a queries SQL que se puedan añadir al componente 3 de Postres.

### Componente Postgres.
Este componente existe con el fin de facilitar el estudio y exploración de datos tras la limpieza de datos y con menos problemas de procesamiento que trabajando con excel. Existe de cara a prepararnos para una transición digital al concepto de bóveda unificada de datos a nivel VD.

## Estructura del repositorio

1. Directorio para backups automatizados de la bóveda.
1. Directorio para código
