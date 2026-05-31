def search_name(products, keyword):

    result = []

    for product in products:

        if keyword in product["name"]:
            result.append(product)

    return result


def search_keyword(products, keyword):

    result = []

    for product in products:

        if keyword in product["keyword"]:
            result.append(product)

    return result
