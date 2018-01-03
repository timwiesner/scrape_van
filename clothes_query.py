import requests, json

# TO do: Make sure program works by tags or type
# To Do: List pretty?
def get_products(site):
    url_template = 'https://www.{}.com/products.json'
    url = url_template.format(site)
    r = requests.get(url)
    json_data = r.json()
    data = []
    for each in json_data['products']:
        title = each['title']
        product_type = each['product_type']
        tags = each['tags']
        data.append({'title':title, 'product_type':product_type, 'tags':tags})
    get_types(data)

def get_types(products):
    product_types = []
    for p in products:
        product_types.append(p["product_type"])
    product_types = sorted(list(set(product_types)))
    display_results(product_types)
    get_type = input("Enter product type: ")
    get_tags(products, get_type)


def get_tags(products, type):
    products_by_type = []
    product_tags = []
    for p in products:
        if type == p["product_type"]:
            products_by_type.append(p)
            tags = p["tags"]
            for tag in tags:
                product_tags.append(tag)
    product_tags = sorted(list(set(product_tags)))
    display_results(product_tags)
    get_tag = input("Enter tag from above list: ")
    get_results(products_by_type, get_tag)


def get_results(products_by_type, get_tag):
    # TO DO: If tag listed on all products, delete
    potential_products_by_tag = []
    for p in products_by_type:
        tags = p["tags"]
        for tag in tags:
            if get_tag == tag:
                potential_products_by_tag.append(p)
    display_results(potential_products_by_tag)


def display_results(items):
    result = json.dumps(items, indent=2)
    print(result)


def run_program():
    site = input("Company: ").lower()
    get_products(site)

run_program()
