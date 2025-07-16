import random
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("랜덤 아이템 뽑기")
root.geometry("300x450")

# 이미지 로딩 및 리사이즈
random_image = ImageTk.PhotoImage(Image.open("mO3ouHJ2BjWxmYyRyb36ER85dZyedrAGMdGzDkX9oU55FDEXJQJ9ozt8WPRWwGmDBn5HOqZxAkZOS9_RGNf34A.png").resize((300, 300)))
first_image = ImageTk.PhotoImage(Image.open("Zenith.png").resize((300, 300)))
second_image = ImageTk.PhotoImage(Image.open("76593b3e1c4efbec44871f5ec839bc53f7bb281c4fab7eac7dd1b28efa3b.png").resize((300, 300)))
third_image = ImageTk.PhotoImage(Image.open("pngtree-expressive-poop-character-for-stickers-png-image_15680971.png").resize((300, 300)))
fourth_image = ImageTk.PhotoImage(Image.open("Stone-PNG-Image.png").resize((300, 300)))
fifth_image = ImageTk.PhotoImage(Image.open("FtrCushionWhoopee_Remake_2_0.png").resize((300, 300)))


def change_image(event):
    rrandom = random.randint(1, 5)
    if rrandom == 1:
        label.config(image=first_image)
        label2.config(text="제니스\n공격력⭐⭐⭐⭐⭐\n예능감⭐\n능력⭐⭐⭐⭐⭐")
    elif rrandom == 2:
        label.config(image=second_image)
        label2.config(text="최.강.삼.성 뭐꼬! 부채\n공격력⭐⭐⭐⭐⭐\n예능감⭐⭐⭐⭐⭐\n능력⭐⭐⭐⭐⭐")
    elif rrandom == 3:
        label.config(image=third_image)
        label2.config(text="똥\n공격력⭐\n예능감⭐⭐⭐⭐\n능력⭐⭐")
    elif rrandom == 4:
        label.config(image=fourth_image)
        label2.config(text="짱돌\n공격력⭐⭐⭐⭐\n예능감⭐⭐⭐\n능력⭐")
    else:
        label.config(image=fifth_image)
        label2.config(text="방귀쿠션\n공격력⭐⭐\n예능감⭐⭐⭐⭐⭐\n능력⭐⭐⭐⭐")

# 라벨로 이미지와 텍스트 표시
label = tk.Label(root, image=random_image)
label.pack()
label.bind("<Button-1>", change_image)  # 클릭 시 이미지 변경

label2 = tk.Label(root, text="랜덤뽑기")
label2.pack()

# 루프 실행
root.mainloop()
