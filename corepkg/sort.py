def sort_price(products):

    return sorted(
        products,
        key=lambda x: x["price"]
    )


def sort_rating(products):

    return sorted(
        products,
        key=lambda x: x["rating"],
        reverse=True
    )


def sort_popular(products):

    return sorted(
        products,
        key=lambda x: x["like"],
        reverse=True
    )
