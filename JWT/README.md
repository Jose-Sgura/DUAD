Ventaja frente a un caché indefinido:

Memoria acotada: las frutas que nadie pide se borran solas y el caché no crece sin límite (importante en el plan gratis de 30 MB).
Datos menos desactualizados: si alguna invalidación fallara (por ejemplo, Redis caído justo al editar), el dato viejo desaparece solo en vez de quedarse para siempre.
Lo más pedido se queda: con la expiración deslizante, las frutas populares se mantienen en caché y las poco consultadas se liberan.


Archivo	Contenido
app.py	Rutas de la API
auth.py	Validación del token y decorador login_required
db.py	Tablas y DBManager (acceso a la base de datos)
JWT_Manager.py	JWTManager para crear y verificar tokens
cache_manager.py	CacheManager: capa de caché sobre Redis (get / set / delete)
docker-compose.yml	(se me olvidó quitarlo anteriormente, pensé en usarlo pero preferí hacerlo desde la nube como se nos enseñó)
generate_keys.py	Genera el par de llaves RSA