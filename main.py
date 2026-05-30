import tkinter as tk

from data.products import products

from corepkg.search import search_name

from corepkg.sort import (
    sort_price,
    sort_rating,
    sort_popular
)


window = tk.Tk()

window.title("TEAM TETR SHOP")

window.geometry("800x600")

window.configure(bg="white")


title = tk.Label(
    window,
    text="TEAM TETR SHOP",
    font=("Arial", 24, "bold"),
    bg="white"
)

title.pack(pady=10)


search_entry = tk.Entry(
    window,
    width=30,
    font=("Arial", 14)
)

search_entry.pack(pady=10)


product_frame = tk.Frame(
    window,
    bg="white"
)

product_frame.pack(fill="both", expand=True)


def show_products(product_list):

    for widget in product_frame.winfo_children():
        widget.destroy()

    for product in product_list:

        card = tk.Frame(
            product_frame,
            bg="#f5f5f5",
            bd=1,
            relief="solid"
        )

        card.pack(
            pady=10,
            padx=20,
            fill="x"
        )

        name_label = tk.Label(
            card,
            text=product["name"],
            font=("Arial", 16, "bold"),
            bg="#f5f5f5"
        )

        name_label.pack(anchor="w", padx=10)

        price_label = tk.Label(
            card,
            text=f"{product['price']}원",
            font=("Arial", 13),
            bg="#f5f5f5"
        )

        price_label.pack(anchor="w", padx=10)

        rating_label = tk.Label(
            card,
            text=f"⭐ {product['rating']}",
            font=("Arial", 12),
            bg="#f5f5f5"
        )

        rating_label.pack(anchor="w", padx=10)
        
        like_label = tk.Label(
             card,
             text=f"♥ {product['like']}",
             font=("Arial", 12),
             bg="#f5f5f5"
       )

        like_label.pack(anchor="w", padx=10)

        


def search_product():

    keyword = search_entry.get()

    result = search_name(
        products,
        keyword
    )

    show_products(result)


search_button = tk.Button(
    window,
    text="검색",
    command=search_product,
    font=("Arial", 12)
)

search_button.pack(pady=5)


button_frame = tk.Frame(
    window,
    bg="white"
)

button_frame.pack(pady=10)


price_button = tk.Button(
    button_frame,
    text="가격순",
    command=lambda:
    show_products(sort_price(products))
)

price_button.grid(row=0, column=0, padx=5)


rating_button = tk.Button(
    button_frame,
    text="별점순",
    command=lambda:
    show_products(sort_rating(products))
)

rating_button.grid(row=0, column=1, padx=5)


popular_button = tk.Button(
    button_frame,
    text="인기순",
    command=lambda:
    show_products(sort_popular(products))
)

popular_button.grid(row=0, column=2, padx=5)


show_products(products)

window.mainloop()