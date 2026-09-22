from fastapi import FastAPI, Request
from mockData import products
from dtos import ProductDTO
app = FastAPI()

# normal path
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# path params
@app.get("/products")
def get_products():
    return products


@app.get("/product/{product_id}")
def get_one_products(product_id:int):
    ##if product availabe with the id, return product, else return error message.
    for oneproduct in products:
        if oneproduct.get("id") == product_id:
            return oneproduct
    return {
        "error":"product not found for this ID."
    }

#Query Params

@app.get("/greet")
def greet_user(name:str, age:int):
    return {
        "greet": f"Hello {name}, your age is {age}"
    }

#request
@app.get("/greet")
def greet_user(request:Request):
    query_params = dict(request.query_params)
    print(query_params)
    return {
        "greet": f"Hello{query_params.get("name")}, your age is{query_params.get("age")}"
    }

##body, headers - request headers, query params
##Difference type of HTTP Methods, pydantic
@app.post("/create_products")
def create_produt(product_data:ProductDTO):
    product_data = product_data.model_dump()
    products.append(product_data)
    return{"status":"product created successfully...", "data":products}

#put method
@app.put("/update_products{products_id}")
def update_products(products_data:ProductDTO, products_id:int):
    for index, oneProducts in enumerate(products): #enumerate  is a method that give index number + data.
        products[index] = products_data.model_dump
        return{"status":"product updated successfully.."}
    return {
        "error":"product not found for this ID."
    }

#delete method
@app.delete("/delete_product/{product_id}")
def delete_product():
    for index, one_product in enumerate(products):
        if one_product.get("id") == product_id:
            deleted_product = products.pop(index)
            return {"status":"product deleted successfully..","product":{}}
    return{
        "error":"product not found for this id"
    }
##how to validate data - DTOS(Data Transfer objects)
##how to call different HHTP Methoda - Any tools?