from simpleApi.celery import app
from myapiAsync.models import Product
from myapiAsync.serializers import ProductSerializer
from time import sleep
import random


@app.task(bind=True)
def add(self, prod_data=None):
    prod_serialize = ProductSerializer(data=prod_data)
    if prod_serialize.is_valid():
        prod_serialize.save()
    self.update_state(state='Dispatching', meta={'progress': '33'})
    sleep(random.randint(5, 10))  # pre-processing the dataset in machine learning pipeline,...

    self.update_state(state='Running', meta={'progress': '66'})
    sleep(random.randint(5, 10))  # training the algorithm,...

    self.update_state(state='Finishing', meta={'progress': '100'})
    sleep(random.randint(5, 10))  # reporting metrics, saving the model,...

    return prod_serialize

@app.task(bind=True)      
def update(self,products=None, prod_data=None):
    product_serialize = ProductSerializer(products, data=prod_data,partial=True) 
    if product_serialize.is_valid(): 
        product_serialize.save() 
    
    self.update_state(state='Dispatching', meta={'progress': '33'})
    sleep(random.randint(5, 10))  # pre-processing the dataset in machine learning pipeline,...

    self.update_state(state='Running', meta={'progress': '66'})
    sleep(random.randint(5, 10))  # training the algorithm,...

    self.update_state(state='Finishing', meta={'progress': '100'})
    sleep(random.randint(5, 10))  # reporting metrics, saving the model,...

    return product_serialize


