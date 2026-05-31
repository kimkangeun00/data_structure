from corepkg.cart import Cart
from tkinter import messagebox

import tkinter as tk

from data.products import products

from corepkg.search import search_name

from corepkg.sort import (
    sort_price,
    sort_rating,
    sort_popular
)


window = tk.Tk()

cart = Cart()

window.title("TEAM TETR SHOP")

window.state("zoomed")

window.configure(bg="white")


title = tk.Label(
    window,
    text="TEAM TETR SHOP",
    font=("Arial", 24, "bold"),
    bg="white"
)

title.pack(pady=10)

search_frame = tk.Frame(
    window,
    bg="white"
)

search_frame.pack(
    fill="x",
    pady=10
)

center_frame = tk.Frame(
    search_frame,
    bg="white"
)

center_frame.pack(
    side="left",
    expand=True,
    padx=(520, 0)
)


right_frame = tk.Frame(
    search_frame,
    bg="white"
)

right_frame.pack(
    side="right",
    padx=(0, 300)
)

sort_frame = tk.Frame(
    window,
    bg="white"
)

sort_frame.pack(
    pady=5
)

top_frame = tk.Frame(
    window,
    bg="white"
)

top_frame.pack(
    pady=10
)

search_entry = tk.Entry(
    center_frame,
    font=("Arial", 14)
)

search_entry.pack(
    side="left",
    padx=5
)

product_frame = tk.Frame(
    window,
    bg="white"
)

product_frame.pack(fill="both", expand=True)

def add_to_cart(product):

    cart.add_cart(product)

    messagebox.showinfo(
        "장바구니",
        f"{product['name']} 장바구니 추가 완료"
    )

def open_cart():

    cart_window = tk.Toplevel(window)

    cart_window.title("장바구니")

    cart_window.geometry("500x500")


    title = tk.Label(
        cart_window,
        text="장바구니 목록",
        font=("Arial", 20, "bold")
    )

    title.pack(pady=20)


    items = cart.get_items()


    if len(items) == 0:

        empty_label = tk.Label(
            cart_window,
            text="장바구니가 비어있습니다."
        )

        empty_label.pack()

        return


    for product in items:

        item_frame = tk.Frame(
            cart_window,
            bd=1,
            relief="solid",
            padx=10,
            pady=10
        )

        item_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )


        name_label = tk.Label(
            item_frame,
            text=product["name"],
            font=("Arial", 14, "bold")
        )

        name_label.pack(anchor="w")


        price_label = tk.Label(
            item_frame,
            text=f"{product['price']}원"
        )

        price_label.pack(anchor="w")

def show_products(product_list):

    for widget in product_frame.winfo_children():
        widget.destroy()

    row = 0
    column = 0

    for product in product_list:

        card = tk.Frame(
            product_frame,
            bg="#f5f5f5",
            width=300,
            height=400,
            bd=1,
            relief="solid"
        )

        card.grid(
            row=row,
            column=column,
            padx=20,
            pady=20
        )

        card.grid_propagate(False)


        image_space = tk.Frame(
            card,
            bg="#d9d9d9",
            width=250,
            height=200
        )

        image_space.pack(
            pady=15
        )

        image_space.pack_propagate(False)


        image_label = tk.Label(
            image_space,
            text="IMAGE",
            bg="#d9d9d9",
            font=("Arial", 14)
        )

        image_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )


        name_label = tk.Label(
            card,
            text=product["name"],
            font=("Arial", 15, "bold"),
            bg="#f5f5f5"
        )

        name_label.pack(anchor="w", padx=20)


        price_label = tk.Label(
            card,
            text=f"{product['price']}원",
            font=("Arial", 13),
            bg="#f5f5f5"
        )

        price_label.pack(anchor="w", padx=20)


        rating_label = tk.Label(
            card,
            text=f"⭐ {product['rating']}",
            font=("Arial", 12),
            bg="#f5f5f5"
        )

        rating_label.pack(anchor="w", padx=20)


        like_label = tk.Label(
            card,
            text=f"♥ {product['like']}",
            font=("Arial", 12),
            bg="#f5f5f5"
        )

        like_label.pack(anchor="w", padx=20)


        cart_button = tk.Button(
            card,
            text="장바구니 담기",
            command=lambda p=product:
            add_to_cart(p)
        )

        cart_button.pack(
            pady=10
        )


        column += 1

        if column > 5:
         column = 0
         row += 1
        


def search_product():

    keyword = search_entry.get()

    result = search_name(
        products,
        keyword
    )

    show_products(result)


search_button = tk.Button(
    center_frame,
    text="검색",
    command=search_product,
    font=("Arial", 12)
)

search_button.pack(
    side="left",
    padx=5)

cart_open_button = tk.Button(
    right_frame,
    text="장바구니",
    font=("Arial", 11),
    command=open_cart
)

cart_open_button.pack(
    side="left",
    padx=30
)
order_button = tk.Button(
    right_frame,
    text="주문조회",
    font=("Arial", 11)
)

order_button.pack(
    side="left",
    padx=5
)

price_button = tk.Button(
    sort_frame,
    text="가격순",
    command=lambda:
    show_products(sort_price(products))
)

price_button.pack(
    side="left",
    padx=5
)


rating_button = tk.Button(
    sort_frame,
    text="별점순",
    command=lambda:
    show_products(sort_rating(products))
)

rating_button.pack(
    side="left",
    padx=5)

popular_button = tk.Button(
    sort_frame,
    text="인기순",
    command=lambda:
    show_products(sort_popular(products))
)

popular_button.pack(
    side="left",    
    padx=5
)



show_products(products)

window.mainloop()
