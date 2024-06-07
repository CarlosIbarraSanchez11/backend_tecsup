from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

# Instancia de la clase
db = SQLAlchemy()
migrate = Migrate()