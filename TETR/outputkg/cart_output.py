import tkinter as tk

from tkinter import messagebox

from datetime import datetime


def open_cart(
    window,
    cart,
    order_queue,
    products,
    show_products,
    product_frame,
    add_to_cart
):

    cart_window = tk.Toplevel(window)

    cart_window.title("장바구니")

    cart_window.geometry("700x600")

    cart_window.configure(bg="white")


    title = tk.Label(
        cart_window,
        text="장바구니 목록",
        font=("Arial", 24, "bold"),
        bg="white"
    )

    title.pack(pady=20)


    # 주문하기 함수
    def order_items():

        items = cart.get_items()

        if len(items) == 0:

            messagebox.showwarning(
                "장바구니",
                "장바구니가 비어있습니다."
            )

            return


        first_name = items[0]["name"]

        if len(items) > 1:

            order_name = f"{first_name} 외 {len(items)-1}개"

        else:

            order_name = first_name


        order_data = {

            "name": order_name,

            "time": datetime.now().strftime("%Y-%m-%d %H:%M")

        }


        order_queue.enqueue(order_data)

        for item in items:

          if item["stock"] > 0:

            item["stock"] -= 1


        # 장바구니 전체 삭제
        cart.clear_cart()

        show_products(
         products,
         product_frame,
         add_to_cart
    )


        messagebox.showinfo(
            "주문 완료",
            "주문이 완료되었습니다."
        )


        cart_window.destroy()
        show_products(products)


    # 주문하기 버튼
    order_button = tk.Button(
        cart_window,
        text="주문하기",
        font=("맑은 고딕", 11, "bold"),
        bg="#222222",
        fg="white",
        bd=0,
        padx=15,
        pady=6,
        cursor="hand2",
        command=order_items
    )

    order_button.pack(pady=(0, 15))


    # 스크롤 캔버스
    cart_canvas = tk.Canvas(
        cart_window,
        bg="white",
        highlightthickness=0
    )

    cart_scrollbar = tk.Scrollbar(
        cart_window,
        orient="vertical",
        command=cart_canvas.yview
    )

    cart_scrollable_frame = tk.Frame(
        cart_canvas,
        bg="white"
    )


    cart_scrollable_frame.bind(
        "<Configure>",
        lambda e: cart_canvas.configure(
            scrollregion=cart_canvas.bbox("all")
        )
    )


    cart_canvas.create_window(
        (0, 0),
        window=cart_scrollable_frame,
        anchor="nw",
        width=660
    )

    cart_canvas.configure(
        yscrollcommand=cart_scrollbar.set
    )


    cart_canvas.pack(
        side="left",
        fill="both",
        expand=True
    )

    cart_scrollbar.pack(
        side="right",
        fill="y"
    )


    # 삭제 함수
    def remove_item(product):

        cart.remove_cart(product)

        cart_window.destroy()

        open_cart()


    items = cart.get_items()


    # 비었을 때
    if len(items) == 0:

        empty_label = tk.Label(
            cart_scrollable_frame,
            text="장바구니가 비어있습니다.",
            font=("Arial", 14),
            bg="white"
        )

        empty_label.pack(pady=30)

        return


    # 상품 출력
    for product in items:

        item_frame = tk.Frame(
            cart_scrollable_frame,
            bg="#f5f5f5",
            bd=1,
            relief="solid",
            width=620,
            height=180
        )

        item_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        item_frame.pack_propagate(False)


        # 이미지 프레임
        image_frame = tk.Frame(
            item_frame,
            width=140,
            height=140,
            bg="white"
        )

        image_frame.pack_propagate(False)

        image_frame.pack(
            side="left",
            padx=15,
            pady=15
        )


        # 이미지
        photo = tk.PhotoImage(
            file=product["image"]
        )

        photo = photo.subsample(6, 6)


        image_label = tk.Label(
            image_frame,
            image=photo,
            bg="white",
            bd=0
        )

        image_label.image = photo

        image_label.pack(expand=True)


        # 정보 영역
        info_frame = tk.Frame(
            item_frame,
            bg="#f5f5f5"
        )

        info_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )


        # 상품명
        name_label = tk.Label(
            info_frame,
            text=product["name"],
            font=("Arial", 18, "bold"),
            bg="#f5f5f5"
        )

        name_label.pack(
            anchor="w"
        )


        # 가격
        price_label = tk.Label(
            info_frame,
            text=f"{product['price']}원",
            font=("Arial", 14),
            bg="#f5f5f5"
        )

        price_label.pack(
            anchor="w",
            pady=(8, 0)
        )


        # 별점
        rating_label = tk.Label(
            info_frame,
            text=f"⭐ {product['rating']}",
            font=("Arial", 12),
            bg="#f5f5f5"
        )

        rating_label.pack(
            anchor="w",
            pady=(8, 0)
        )


        # 좋아요
        like_label = tk.Label(
            info_frame,
            text=f"♥ {product['like']}",
            font=("Arial", 12),
            bg="#f5f5f5"
        )

        like_label.pack(
            anchor="w"
        )


        # 삭제 버튼
        delete_button = tk.Button(
            item_frame,
            text="삭제",
            font=("맑은 고딕", 10, "bold"),
            bg="#d9534f",
            fg="white",
            bd=0,
            padx=14,
            pady=5,
            cursor="hand2",
            command=lambda p=product: remove_item(p)
        )

        delete_button.pack(
            side="right",
            padx=20
        )