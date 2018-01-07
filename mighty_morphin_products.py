import requests, json

def get_product_types(site, p_type=1):
    products = []
    product_types = []
    products_by_type = []

    url = "https://www.{0}.com/products.json".format(site)
    r = requests.get(url)
    json_data = r.json()

    for each in json_data['products']:
        title = each['title']
        product_type = each['product_type']
        products.append({
            'title': title,
            'product_type': product_type})

    if p_type == 1:
        for p in products:
            product_types.append(p["product_type"])
        print(sorted(set(product_types)))
    else:
        for p in products:
            if p_type == p["product_type"]:
                products_by_type.append(p["title"])
        print(sorted(set(products_by_type)))
        # print(products_by_type['title'])



def get_product_tags(site, p_tag=1):
    products = []
    product_tags = []
    products_by_tag = []

    url = "https://www.{0}.com/products.json".format(site)
    r = requests.get(url)
    json_data = r.json()

    for each in json_data['products']:
        title = each['title']
        tags = each['tags']
        products.append({
            'title': title,
            'tags': tags})

    if p_tag == 1:
        for p in products:
            for tag in p["tags"]:
                product_tags.append(tag)
        print(sorted(set(product_tags)))
    else:
        for p in products:
            for tag in p["tags"]:
                if p_tag == tag:
                    products_by_tag.append(p["title"])
        print(sorted(set(products_by_tag)))



def get_products(site, p_type, p_tag):
    # 5. With type and tag, return products with matching type and tag
    products = []
    products_to_return = []

    url = "https://www.{0}.com/products.json".format(site)
    r = requests.get(url)
    json_data = r.json()

    for each in json_data['products']:
        title = each['title']
        product_type = each['product_type']
        tags = each['tags']
        products.append({
            'title': title,
            'product_type': product_type,
            'tags': tags})

    for p in products:
        if p_type == p["product_type"]:
            products_to_return.append(p["title"])
        for tag in p["tags"]:
            if p_tag == tag:
                products_to_return.append(p["title"])

    print(sorted(set(products_to_return)))



get_product_types(site='fashionnova', p_type='Pants')
