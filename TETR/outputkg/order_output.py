import tkinter as tk

from tkinter import messagebox

from datetime import datetime

def open_orders(window, order_queue):

    order_window = tk.Toplevel(window)

    order_window.title("주문 / 배송")

    order_window.geometry("500x500")

    order_window.configure(bg="white")


    title = tk.Label(
        order_window,
        text="주문 내역",
        font=("Arial", 22, "bold"),
        bg="white"
    )

    title.pack(pady=20)


    orders = order_queue.get_orders()
    orders.reverse()  # 최신 주문이 위에 오도록 순서 뒤집기


    if len(orders) == 0:

        empty_label = tk.Label(
            order_window,
            text="주문 내역이 없습니다.",
            font=("Arial", 14),
            bg="white"
        )

        empty_label.pack(pady=30)

        return


    for order in orders:

        order_frame = tk.Frame(
            order_window,
            bg="#f5f5f5",
            bd=1,
            relief="solid"
        )

        order_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )


        name_label = tk.Label(
            order_frame,
            text=order["name"],
            font=("Arial", 15, "bold"),
            bg="#f5f5f5"
        )

        name_label.pack(
            anchor="w",
            padx=15,
            pady=(10, 0)
        )


        time_label = tk.Label(
            order_frame,
            text=order["time"],
            font=("Arial", 11),
            fg="gray",
            bg="#f5f5f5"
        )

        time_label.pack(
            anchor="w",
            padx=15,
            pady=(0, 10)
        )