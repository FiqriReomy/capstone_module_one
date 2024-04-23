import config.config as cf


def create_and_update(name, category, price, stock, product_id=0):
    if product_id == 0:
        last_product_id = max(product.get('product_id', 0) for product in cf.products)
        new_product_id = last_product_id + 1
        newproduct = {'product_id' : new_product_id, 'name' : name, 'category':category, 'price':price, 'stock':stock}
        cf.products.append(newproduct)
        cf.products_save()
        
    else :
        for product in cf.products:
            if product['product_id'] == product_id:
                product['name'] = name
                product['category'] = category
                product['price'] = price
                product['stock'] = stock
        cf.products_save()

                
def get_product_by_id(product_id):
        for product in cf.products:
            if product.get('product_id') == product_id:
                return product

def exist_product_name(name):

    exist_product = list(filter(lambda x:x['name'] == name, cf.products))
   
    
    if len(exist_product) != 0:
        return None, 'Product name is already exist'
    else  :
        if len(name) < 5 :
            return False, 'Product name character less than 5 character' 
        else : 
            return True , f'{name} is successfully added as new product' 
    
    
