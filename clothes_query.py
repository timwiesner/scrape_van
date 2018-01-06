import requests, json

# TO do: Make sure program works by tags or type
# TO DO: Error handling

def get_site():
	welcome = (
		"Enter a Shopify Store. I.e. 'fashionnova', 'gymshark', 'unifclothing', "
		"'ripndipclothing', 'sisterjane', 'cr7', 'untuckit', 'rebeccaminkoff', "
		"'jackthreads', 'thirdlove', 'teddyfresh', 'teeturtle', 'theyetee', "
		"'onlyny', 'chicnico' "
		)
	print(welcome)
	store = input("Store: ").lower()
	get_products(store)


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
		data.append({
			'title': title,
			'product_type': product_type,
			'tags': tags})
	# print("Product types for " + site + ":")
	get_types(data)


def get_types(products):
	product_types = []
	for p in products:
		product_types.append(p["product_type"])
	product_types = sorted(list(set(product_types)), key=str.lower)
	display_results(product_types)
	get_type = input("Enter product type: ")
	# print("Products with type " + get_type + ":")
	get_tags(products, get_type)

# Normalize - unique tags and types
def get_tags(products, p_type):
	products_by_type = []
	product_tags = []
	for p in products:
		if p_type.lower() == p["product_type"].lower():
			products_by_type.append(p)
			tags = p["tags"]
			for tag in tags:
				product_tags.append(tag)
	product_tags = sorted(list(set(product_tags)), key=str.lower)
	display_results(product_tags)
	get_tag = input("Enter tag from above list: ")
	# print("Product with tag " + get_tag + ":")
	get_results(products_by_type, get_tag)


def get_results(products_by_type, get_tag):
	# TO DO: Narrow down tags. If tag listed on all products, delete?
	products_by_tag = []
	for p in products_by_type:
		tags = p["tags"]
		for tag in tags:
			if get_tag.lower() == tag.lower():
				products_by_tag.append(p)
	print("\n\nMatching Products:")
	display_results(products_by_tag)


def display_results(items):
	result = json.dumps(items, indent=2)
	print(result)


def run_program():
	get_site()


run_program()
