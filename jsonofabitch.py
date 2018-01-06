import requests, json

def get_product_types(site, p_type=1):
    products = []
    product_types = []
    products_by_type = []

    # Get site
    url = "https://www.{0}.com/products.json".format(site)
    r = requests.get(url)
    json_data = r.json()
    for each in json_data['products']:
        title = each['title']
        product_type = each['product_type']
        products.append({
            'title': title,
            'product_type': product_type})

    # set to 1(all) by default if missing argument
    if p_type == 1:
        # return all product types
        for p in products:
            product_types.append(p["product_type"])
        # product_types = list(set(product_types))
        # return product_types
        print(product_types)
    else:
        # return products with specific type
        for p in products:
            if p_type == p["product_type"]:
                products_by_type.append(p)
        # products_by_type = list(set(products_by_type))
        # return products_by_type
        print(products_by_type)


get_product_types('fashionnova')



# def get_product_tags(site, tag=1):
    # 2. With shop name, tag = all, return all tags
    # 4. Shop name, product_tag="" , return products with specific tag

# def get_products(type, tag):
    # 5. With type and tag, return products with matching type and tag
