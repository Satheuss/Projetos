import random
import requests
from PIL import Image, ImageTk
from io import BytesIO
import tkinter as tk

imagens = [
    "https://i.pinimg.com/736x/6e/e7/13/6ee713f339bc13d41dcaca41ae7dbc3f.jpg",
    "https://i.pinimg.com/736x/58/93/89/589389b12a92d31922df2763c41ee660.jpg",
    "https://i.pinimg.com/736x/9c/30/9e/9c309e5b01580527fc18800d99b96763.jpg",
    "https://i.pinimg.com/736x/9f/fb/09/9ffb09c5b49505fba29f414ad060efd0.jpg",
    "https://i.pinimg.com/736x/ef/02/65/ef0265efe674e86762eeae3a253badd8.jpg",
    "https://i.pinimg.com/736x/78/ab/cf/78abcf485343f175a4737e958a4821ec.jpg",
    "https://i.pinimg.com/736x/e3/e5/d2/e3e5d2a2423e4be1bc94f1690e24750d.jpg",
    "https://i.pinimg.com/736x/74/78/60/747860bd41e2c17c2ebc2deced164076.jpg",
    "https://i.pinimg.com/736x/b8/9f/69/b89f69f6c8cde742d8b0ab1ba98e1356.jpg",
    "https://i.pinimg.com/736x/6b/30/0d/6b300d3da00fc33ee92dc052cff534a7.jpg",
    "https://i.pinimg.com/736x/52/5a/66/525a66b59480e284eb727650f4ee42f2.jpg",
    "https://i.pinimg.com/736x/ca/a5/e4/caa5e46f6b75f22dbf5eed1eb3298aee.jpg",
    "https://i.pinimg.com/736x/2d/1f/58/2d1f58250d46e3c18b65f448c1e964e8.jpg",
    "https://i.pinimg.com/736x/e6/73/1e/e6731e84b4e4082ad9f4772ba443d182.jpg",
    "https://i.pinimg.com/736x/45/fb/85/45fb850789b347eea1c9b42d363b7e6e.jpg",
    "https://i.pinimg.com/736x/55/b4/e5/55b4e56e518ede6b4896bbe863a8b317.jpg",
    "https://i.pinimg.com/736x/88/2b/3a/882b3aee1edf27ab49951f45a8682500.jpg",
    "https://i.pinimg.com/1200x/ea/05/4f/ea054fdba8eeed92509bee1b976a308f.jpg",
    "https://i.pinimg.com/736x/e4/a8/60/e4a86020d6091cf7529fba2b2772796d.jpg",
    "https://i.pinimg.com/736x/43/f1/f2/43f1f231d5856ba18c964e204951d239.jpg",
    "https://i.pinimg.com/736x/f0/0b/cf/f00bcf048af41adb435b510f39238107.jpg"
    
]

def mostrar_imagem():
    url = random.choice(imagens)

    resposta = requests.get(url)
    img = Image.open(BytesIO(resposta.content))

    img = img.resize((400, 400))

    img_tk = ImageTk.PhotoImage(img)

    label.config(image=img_tk)
    label.image = img_tk

janela = tk.Tk()
janela.title("Imagens Aleatórias")
janela.configure(bg="#570CD1")

label = tk.Label(janela)
label.pack()

botao = tk.Button(janela, text="Nova Imagem", command=mostrar_imagem)
botao.pack()
botao.configure(bg="#FFE600")

mostrar_imagem()

janela.mainloop()