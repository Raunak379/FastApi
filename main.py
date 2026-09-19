from fastapi import FastAPI, Request
from mockData import products
app = FastAPI()

# normal path
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# path params
@app.get("/products")
def get_products():
    return products


@app.get("/product/{product_id}/{date}")
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