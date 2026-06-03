import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

from corepkg.order import OrderQueue
from corepkg.cart import Cart
from tkinter import messagebox
from outputkg.cart_output import open_cart
from outputkg.order_output import open_orders
from outputkg.product_output import show_products

import tkinter as tk
from datetime import datetime
from data.products import products

from corepkg.search import search_name

from corepkg.sort import (
    sort_price,
    sort_rating,
    sort_popular
)

from PIL import Image, ImageTk
import os
from tkinter import PhotoImage


window = tk.Tk()

order_queue = OrderQueue()
cart = Cart()

window.title("TEAM TETR SHOP")

window.state("zoomed")

window.configure(bg="white")

top_menu_frame = tk.Frame(
    bg="white"
)

top_menu_frame.pack(
    fill="x",
    pady=(10, 0),
    padx=40
)

menu_frame = tk.Frame(
    top_menu_frame,
    bg="white"
)

menu_frame.pack(
    side="right"
)

header_frame = tk.Frame(
    window,
    bg="white"
)

header_frame.pack(
    fill="x",
    pady=(10, 20),
    padx=40
)

title = tk.Label(
    header_frame,
    text="TEAM TETR SHOP",
    font=("Arial", 20, "bold"),
    bg="white",
    cursor="hand2"
)

title.pack(
    side="left",
    padx=(80, 30)
)

search_frame = tk.Frame(
    header_frame,
    bg="white"
)

search_frame.pack(
    side="left",
    padx=(80,0),
    pady=10,
)



sort_frame = tk.Frame(
    window,
    bg="white"
)

sort_frame.pack(
    pady=5
)

search_outer = tk.Frame(
    search_frame,
    bg="#f1f1f1",
    padx=20,
    pady=4
    )

search_outer.pack(
    side="left",
    padx=20
)
search_entry = tk.Entry(
    search_outer,
    font=("맑은 고딕", 14),
    bd=0,
    bg="#f1f1f1",
    width=55
)

search_entry.pack(
    side="left"
)

canvas = tk.Canvas(
    window,
    bg="white",
    highlightthickness=0
)

scrollbar = tk.Scrollbar(
    window,
    orient="vertical",
    command=canvas.yview
)

scrollable_frame = tk.Frame(
    canvas,
    bg="white"
)
scrollable_frame.configure(width=1200)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas_window=canvas.create_window(
    (0, 0),
    window=scrollable_frame,
    anchor="nw"
)

canvas.configure(
    yscrollcommand=scrollbar.set
)

canvas.pack(
    side="left",
    fill="both",
    expand=True
)

def resize_canvas(event):
    canvas.itemconfig(canvas_window, width=event.width)

canvas.bind("<Configure>", resize_canvas)

scrollbar.pack(
    side="right",
    fill="y"
)

def _on_mousewheel(event):

    canvas.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
    )


canvas.bind_all(
    "<MouseWheel>",
    _on_mousewheel
)

banner_frame=tk.Frame(
    scrollable_frame,
    bg="white",
    height=400
)

print("banner_frame 생성됨")

banner_frame.pack(
    fill="x",
    pady=20
)

product_frame=tk.Frame(
    scrollable_frame,
    bg="white"
)

banner_target={
    0:1,
    1:12,
    2:16,
    3:5,
    5:4
}

product_frame.pack()
for i in range(6):
    product_frame.grid_columnconfigure(i, weight=1)

banner_images_list = []

for i in range(6):

    img_path = os.path.join(
        "banner_images",
        f"banner_0{i+1}.png"
    )

    
    img = Image.open(img_path)

    img.thumbnail((300,350))

    photo = ImageTk.PhotoImage(img)

    banner_images_list.append(photo)

    banner = tk.Label(
        banner_frame,
        image=photo,
        bg="lightgray",
        bd=1,
        relief="solid",
        cursor="hand2"
    )

    banner.grid(
        row=0,
        column=i,
        padx=0,
        sticky="nsew"
    )

    if i in banner_target:
        banner.bind(
            "<Button-1>",
            lambda e, pid=banner_target[i]:
            banner_add_product(pid)
        )

for i in range(6):
    banner_frame.grid_columnconfigure(i,weight=1)

banner_frame.grid_rowconfigure(0,weight=1)

def go_home(event=None):
    search_entry.delete(0,tk.END)
    show_products(
        products,
        product_frame,
        add_to_cart
    )

title.bind(
    "<Button-1>",
    go_home
)

def banner_add_product(product_id):

    for product in products:

        if product["id"] == product_id:

            answer = messagebox.askyesno(
                "상품 추가",
                f"{product['name']}을(를)\n장바구니에 담으시겠습니까?"
            )

            if answer:
                add_to_cart(product)

            return

def add_to_cart(product):

    current_count=cart.count_product(product)

    if current_count>=product["stock"]:
        messagebox.showwarning(
            "재고 부족",
            "재고보다 많이 담을 수 없습니다."
        )
        return
    
    cart.add_cart(product)

    messagebox.showinfo(
        "장바구니",
        f"{product['name']} 장바구니 추가 완료"
    )





def search_product():

    keyword = search_entry.get()

    result = search_name(
        products,
        keyword
    )

    show_products(
    result,
    product_frame,
    add_to_cart
)

search_button = tk.Button(
    search_outer,
    text="⌕",
    font=("맑은 고딕", 18),
    bd=0,
    bg="#f1f1f1",
    activebackground="#f1f1f1",
    cursor="hand2",
    command=search_product
)

search_button.pack(
    side="left",
    padx=10
)


cart_open_button = tk.Button(
    menu_frame,
    text="장바구니",
    font=("맑은 고딕", 11),
    command=lambda: open_cart(
     window,
     cart,
     order_queue,
     products,
     show_products,
     product_frame,
     add_to_cart
  ),
    bg="white",
    bd=0,
    relief="flat",
    cursor="hand2",
    activebackground="white"
)

cart_open_button.pack(
    side="left",
    padx=10
)
order_button = tk.Button(
    menu_frame,
    text="주문/배송",
    font=("맑은 고딕", 11),
    bg="white",
    bd=0,
    relief="flat",
    cursor="hand2",
    activebackground="white",
    command=lambda: open_orders(
    window,
    order_queue
)
)

order_button.pack(
    side="left",
    padx=10
)

price_button = tk.Button(
    sort_frame,
    text="가격순",
    font=("맑은 고딕", 10),
    fg="#2E2E2E",
    bg="#f5f5f5",
    bd=0,
    relief="flat",
    padx=12,
    pady=5,
    cursor="hand2",
    activebackground="#ebebeb",
    command=lambda:
    show_products(
      sort_price(products),
      product_frame,
      add_to_cart
)
)

price_button.pack(
    side="left",
    padx=5
)


rating_button = tk.Button(
    sort_frame,
    text="별점순",
    font=("맑은 고딕", 10),
    fg="#2E2E2E",
    bg="#f5f5f5",
    bd=0,
    relief="flat",
    padx=12,
    pady=5,
    cursor="hand2",
    activebackground="#ebebeb",
    command=lambda:
    show_products(
        sort_rating(products),
        product_frame,
        add_to_cart
    )   
)

rating_button.pack(
    side="left",
    padx=5)

popular_button = tk.Button(
    sort_frame,
    text="인기순",
    font=("맑은 고딕", 10),
    fg="#2E2E2E",
    bg="#f5f5f5",
    bd=0,
    relief="flat",
    padx=12,
    pady=5,
    cursor="hand2",
    activebackground="#ebebeb",
    command=lambda:
    show_products(
    sort_popular(products),
    product_frame,
    add_to_cart
)
)

popular_button.pack(
    side="left",    
    padx=5
)



show_products(
    products,
    product_frame,
    add_to_cart
)

window.mainloop()
