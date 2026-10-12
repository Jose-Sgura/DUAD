import sqlalchemy
#revisando existen más maneras de adornar la verificación de versión
#utilicé la verficiación brindanda por el profe  y ubicación de paquete

print("="*50)
print("INSTALLATION´S VALIDATION - SQALchemy")
print("="*50)
print(f"SQL version: {sqlalchemy.__version__}")
print(f"Package location: {sqlalchemy.__file__}")
print(f"="*50)
print("Installation verified")