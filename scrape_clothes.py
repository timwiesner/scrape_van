import requests, json

# shopify_sites = {'fashionnova', 'gymshark', 'shoploganpaul', 'donomano'}
shopify_sites = {'unifclothing'}

url_template = 'https://www.{}.com/products.json'

for s in shopify_sites:
    url = url_template.format(s)
    print(s)

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
            'tags': tags
        })

    result = json.dumps(data)
    print(result)
