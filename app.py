from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from flask_swagger_ui import get_swaggerui_blueprint




# Init app
app=Flask(__name__)
app.app_context().push()
basedir = os.path.abspath(os.path.dirname(__file__))




#SWAGGER UI 


SWAGGER_URL = '/apidocs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)









# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# Init db
db=SQLAlchemy(app)
# Init ma
ma=Marshmallow(app)
# Product class/Model
class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True) 
    name =db.Column(db.String(100),unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)


    def __init__(self,name,description,price,qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

#Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields =('id','name','description','price','qty')

#Init schema
product_schema = ProductSchema()
products_schema =ProductSchema(many=True)


@app.route('/')
def send_mes():


    return jsonify({"message":"You are on product api head to link/apicos for docs"})    
#Create a Product 
@app.route('/product',methods=['POST'])
def add_product():


    name = request.json['name']
    description  = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product=Product(name,description,price,qty)
    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)
# get all product
@app.route('/product',methods=['GET'])
def get_product():
    all_products=Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)
# single product
@app.route('/product/<id>',methods=['GET'])
def get_single_product(id):
    product=Product.query.get(id)
    return product_schema.jsonify(product)

# update product    
@app.route('/product/<id>',methods=['PUT'])
def update_product(id):

    product=Product.query.get(id)

    name = request.json['name']
    description  = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    product.name=name
    product.description=description
    product.price=price
    product.qty=qty
    
    db.session.commit()

    return product_schema.jsonify(product)

#delete products
@app.route('/product/<id>',methods=['DELETE'])
def delete_single_product(id):
    """
    file: swagger.yaml
    """

 
    product=Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product)






if __name__=='__main__':
    app.run(debug=True)