from flask import Flask
from models import db
from routes import bp as routes_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()


app.register_blueprint(routes_bp)

if __name__ == '__main__':
    app.run(debug=True)
