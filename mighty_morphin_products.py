import requests, json

def get_product_types(site, p_type=1):
    url = "https://www.{0}.com/products.json".format(site)
    r = requests.get(url)
    json_data = r.json()
    products = json_data['products']
    result = []

    if p_type == 1:  # Return all product types if left empty
        for p in products:
            product_type = p['product_type']
            result.append(product_type)
    else:  # Return products with specific type
        for p in products:
            if p_type == p['product_type']:
                title = p['title']
                result.append(title)

    result = sorted(list(set(result)))
    result = json.dumps(result, indent=2)
    print(result)


def get_product_tags(site, p_tag=1):
    url = "https://www.{0}.com/products.json".format(site)
    r = requests.get(url)
    json_data = r.json()
    products = json_data['products']
    result = []

    if p_tag == 1:  # Return all tags
        for p in products:
            for tag in p['tags']:
                result.append(tag)
    else:  # Return products with specific tag
        for p in products:
            for tag in p['tags']:
                if p_tag == tag:
                    title = p['title']
                    result.append(title)

    result = sorted(list(set(result)))
    result = json.dumps(result, indent=2)
    print(result)



def get_products(site, p_type, p_tag):
    url = "https://www.{0}.com/products.json".format(site)
    r = requests.get(url)
    json_data = r.json()
    products = json_data['products']
    result = []

    for p in products:
        if p_type == p['product_type']:
            for tag in p['tags']:
                if p_tag == tag:
                    title = p['title']
                    result.append(title)

    result = sorted(list(set(result)))
    result = json.dumps(result, indent=2)
    print(result)




# get_product_types(site='gymshark')
# get_product_types(site='fashionnova')
# get_product_types(site='teddyfresh')
# get_product_types(site='gymshark', p_type='T-shirt')
# get_product_types(site='fashionnova', p_type='Skirts')
# get_product_tags(site='gymshark')
# get_product_tags(site='fashionnova')
# get_product_tags(site='teddyfresh')
get_product_tags(site='teddyfresh', p_tag='Baseball Cap')
# get_product_tags(site='gymshark', p_tag='size:s')

# get_products(site='gymshark', p_type='T-shirt', p_tag='size:s')


# Reference
# Companies:
#     'fashionnova',
#     'gymshark',
#     'unifclothing',
#     'ripndipclothing',
#     'sisterjane',
#     'cr7',
#     'untuckit',
#     'rebeccaminkoff',
#     'jackthreads',
#     'thirdlove',
#     'teddyfresh',
#     'teeturtle',
#     'theyetee',
#     'onlyny',
#     'chicnico'
