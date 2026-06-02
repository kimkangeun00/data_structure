import tkinter as tk

def show_products(product_list, product_frame, add_to_cart):

    for widget in product_frame.winfo_children():
        widget.destroy()

    row = 0
    column = 0

    for product in product_list:

        card = tk.Frame(
            product_frame,
            bg="#f5f5f5",
            width=240,
            height=360,
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


        photo = tk.PhotoImage(
        file=product["image"]
        
        )

        is_soldout = product["stock"] <= 0

        photo = photo.subsample(4, 4)

        image_label = tk.Label(
        card,
        image=photo,
        bg="#f5f5f5",
        bd=0,
        width=200,
        height=200
        )

        image_label.image = photo

        image_label.pack(
        pady=15
        )

        if is_soldout:

          soldout_label = tk.Label(
              card,
              text="SOLD OUT",
              font=("Arial", 18, "bold"),
              fg="red",
          )
          soldout_label.place(
              x=40,
              y=90
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

        stock_label = tk.Label(
         card,
         text=f"재고 : {product['stock']}개",
         font=("Arial", 11),
         fg="gray",
          bg="#f5f5f5"
        )

        stock_label.pack(
           anchor="w",
           padx=20
        )


        cart_button = tk.Button(
            card,
            text="장바구니 담기",
            command=lambda p=product: add_to_cart(p),
            font=("맑은 고딕", 9, "bold"),

        
            fg="#222222",

            activebackground="#444444",
            activeforeground="white",

            bd=0,
            relief="flat",

            padx=10,
            pady=4,

            cursor="hand2"
        )
        if is_soldout:

          cart_button.config(
           text="품절",
           state="disabled",
           bg="#cccccc",
           fg="white",
           cursor="arrow"
        )


    

        cart_button.pack(
            pady=10
        )


        column += 1

        if column > 5:
         column = 0
         row += 1
        
