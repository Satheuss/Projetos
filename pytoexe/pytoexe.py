import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import subprocess
import threading
import os
import ctypes

#pillow
try:
    from PIL import Image
    TEM_PILLOW = True
except ImportError:
    TEM_PILLOW = False

#cor
COR_FUNDO = "#2031b8"
COR_DESTAQUE = "#ffde00"
COR_TEXTO = "white"

#carrega a fonte Aero no windows
CAMINHO_FONTE = "Aero.ttf"
FONTE_TITULO = ("Arial", 16, "bold") #fonte backup

if os.path.exists(CAMINHO_FONTE):
    try:
        ctypes.windll.gdi32.AddFontResourceExW(os.path.abspath(CAMINHO_FONTE), 0x10, 0)
        FONTE_TITULO = ("Aero", 24)
    except Exception:
        pass

def escolher_arquivo():
    caminho = filedialog.askopenfilename(title="Selecionar .py", filetypes=[("Python", "*.py")])
    if caminho:
        campo_arquivo.delete(0, tk.END)
        campo_arquivo.insert(0, caminho)

def escolher_destino():
    caminho = filedialog.askdirectory(title="Pasta de Destino")
    if caminho:
        campo_destino.delete(0, tk.END)
        campo_destino.insert(0, caminho)

def escolher_icone():
    #png ico
    caminho = filedialog.askopenfilename(
        title="Selecionar Ícone", 
        filetypes=[("Imagens (ICO ou PNG)", "*.ico *.png")]
    )
    if caminho:
        campo_icone.delete(0, tk.END)
        campo_icone.insert(0, caminho)

def iniciar_geracao():
    if not campo_arquivo.get() or not campo_destino.get():
        messagebox.showwarning("Aviso", "Por favor, selecione o arquivo .py e a pasta de destino!")
        return

    #png sem pillow
    if campo_icone.get().lower().endswith(".png") and not TEM_PILLOW:
        messagebox.showerror("Erro", "Para usar PNG como ícone, você precisa instalar o Pillow.\nAbra o terminal e digite: pip install pillow")
        return

    frame_oculto.pack(fill=tk.BOTH, expand=True, pady=10)
    botao_converter.config(state=tk.DISABLED)
    log_widget.config(state=tk.NORMAL)
    log_widget.delete('1.0', tk.END)
    progresso_barra.start(15) 
    
    threading.Thread(target=executar_conversao, daemon=True).start()

def executar_conversao():
    py_file = campo_arquivo.get()
    dest_dir = campo_destino.get()
    icon_file = campo_icone.get()
    icone_final = icon_file
    
    #png pra ico por enquanto
    if icon_file and icon_file.lower().endswith(".png"):
        janela.after(0, atualizar_log, "Convertendo imagem PNG para ICO...\n")
        try:
            img = Image.open(icon_file)
            icone_final = os.path.join(dest_dir, "icone_convertido.ico")
            img.save(icone_final, format="ICO", sizes=[(256, 256)])
            janela.after(0, atualizar_log, "Ícone convertido com sucesso!\n")
        except Exception as e:
            janela.after(0, atualizar_log, f"Erro ao converter PNG: {e}\n")
            janela.after(0, finalizar, 1)
            return

    comando = ["pyinstaller", "--onefile", "--distpath", dest_dir]
    
    if var_sem_console.get():
        comando.append("--noconsole")
    if icone_final:
        comando.append(f"--icon={icone_final}")
    
    comando.append(py_file)

    try:
        processo = subprocess.Popen(
            comando, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, 
            text=True, shell=True 
        )

        for linha in processo.stdout:
            janela.after(0, atualizar_log, linha)

        processo.wait() 
        janela.after(0, finalizar, processo.returncode)
        
    except Exception as e:
        janela.after(0, atualizar_log, f"\nERRO FATAL: {str(e)}")
        janela.after(0, finalizar, 1)

def atualizar_log(texto):
    log_widget.config(state=tk.NORMAL)
    log_widget.insert(tk.END, texto)
    log_widget.see(tk.END)
    log_widget.config(state=tk.DISABLED)

def finalizar(codigo_retorno):
    progresso_barra.stop()
    botao_converter.config(state=tk.NORMAL)
    
    if codigo_retorno == 0:
        messagebox.showinfo("Sucesso", "Conversão concluída com êxito!")
    else:
        messagebox.showerror("Erro", "Falha na conversão. Verifique o log.")

#config janela
janela = tk.Tk()
janela.title("Gerador de EXE")
janela.geometry("600x600") 
janela.configure(bg=COR_FUNDO)
janela.eval('tk::PlaceWindow . center')

tk.Label(janela, text="Transforme .py em .exe", font=FONTE_TITULO, bg=COR_FUNDO, fg=COR_DESTAQUE).pack(pady=20)

frame_inputs = tk.Frame(janela, bg=COR_FUNDO)
frame_inputs.pack(pady=5, padx=20, fill=tk.X)

tk.Label(frame_inputs, text="Código .py:", bg=COR_FUNDO, fg=COR_TEXTO).grid(row=0, column=0, sticky="w", pady=5)
campo_arquivo = tk.Entry(frame_inputs, width=45)
campo_arquivo.grid(row=0, column=1, padx=10)
tk.Button(frame_inputs, text="Procurar", bg=COR_DESTAQUE, fg="black", command=escolher_arquivo).grid(row=0, column=2)

tk.Label(frame_inputs, text="Salvar em:", bg=COR_FUNDO, fg=COR_TEXTO).grid(row=1, column=0, sticky="w", pady=5)
campo_destino = tk.Entry(frame_inputs, width=45)
campo_destino.grid(row=1, column=1, padx=10)
tk.Button(frame_inputs, text="Procurar", bg=COR_DESTAQUE, fg="black", command=escolher_destino).grid(row=1, column=2)

tk.Label(frame_inputs, text="Ícone (ICO/PNG):", bg=COR_FUNDO, fg=COR_TEXTO).grid(row=2, column=0, sticky="w", pady=5)
campo_icone = tk.Entry(frame_inputs, width=45)
campo_icone.grid(row=2, column=1, padx=10)
tk.Button(frame_inputs, text="Procurar", bg=COR_DESTAQUE, fg="black", command=escolher_icone).grid(row=2, column=2)

var_sem_console = tk.BooleanVar(value=True)
tk.Checkbutton(
    janela, text="Esconder a tela preta do terminal ao abrir o .exe", 
    variable=var_sem_console, bg=COR_FUNDO, fg=COR_TEXTO, 
    selectcolor=COR_FUNDO, activebackground=COR_FUNDO, activeforeground=COR_TEXTO
).pack(pady=10)

#fonte botao gerar executavel
botao_converter = tk.Button(
    janela, text="GERAR EXECUTÁVEL", font=("Times New Roman", 11, "bold"), 
    bg="#4CAF50", fg="white", activebackground="#1E7222", 
    command=iniciar_geracao, padx=20, pady=5
)
botao_converter.pack(pady=5)

frame_oculto = tk.Frame(janela, bg=COR_FUNDO)

progresso_barra = ttk.Progressbar(frame_oculto, orient=tk.HORIZONTAL, length=450, mode='indeterminate')
progresso_barra.pack(pady=10)

tk.Label(frame_oculto, text="Log do Processo:", bg=COR_FUNDO, fg=COR_DESTAQUE).pack(anchor="w", padx=20)
log_widget = scrolledtext.ScrolledText(frame_oculto, height=12, width=65, bg="black", fg="#00ff00", font=("Consolas", 9))
log_widget.pack(pady=5, padx=20)

janela.mainloop()