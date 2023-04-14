import tkinter as tk

# Funções de callback para os botões
def selecionar_barramento_a():
    barramento_atual.set("A")

def selecionar_barramento_b():
    barramento_atual.set("B")

def somar():
    barramento = barramento_atual.get()
    valor = int(entry_valor.get())
    if barramento == "A":
        valor_atual = int(entry_r_a.get())
        entry_r_a.delete(0, tk.END)
        entry_r_a.insert(0, str(valor_atual + valor))
    elif barramento == "B":
        valor_atual = int(entry_r_b.get())
        entry_r_b.delete(0, tk.END)
        entry_r_b.insert(0, str(valor_atual + valor))

def resetar():
    entry_r_a.delete(0, tk.END)
    entry_r_a.insert(0, "0")
    entry_r_b.delete(0, tk.END)
    entry_r_b.insert(0, "0")

# Função de callback para o evento de rolagem do mouse
def on_mousewheel(event):
    if event.delta > 0:
        canvas.yview_scroll(-1, "units")
    else:
        canvas.yview_scroll(1, "units")

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora")

# Interface para barramento A
frame_a = tk.Frame(root)
frame_a.grid(row=0, column=0, padx=10, pady=10)

label_barramento_a = tk.Label(frame_a, text="Barramento A")
label_barramento_a.pack()

entry_r_a = tk.Entry(frame_a, width=10)
entry_r_a.pack()

# Interface para barramento B
frame_b = tk.Frame(root)
frame_b.grid(row=0, column=1, padx=10, pady=10)

label_barramento_b = tk.Label(frame_b, text="Barramento B")
label_barramento_b.pack()

entry_r_b = tk.Entry(frame_b, width=10)
entry_r_b.pack()

# Interface para resultado
frame_resultado = tk.Frame(root)
frame_resultado.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

label_resultado = tk.Label(frame_resultado, text="Resultado")
label_resultado.pack()

entry_valor = tk.Entry(frame_resultado, width=10)
entry_valor.pack()

# Barra de status para exibir o barramento atual
barramento_atual = tk.StringVar()
label_status = tk.Label(root, textvariable=barramento_atual, bd=1, relief=tk.SUNKEN, anchor=tk.W)
label_status.grid(row=2, column=0, columnspan=2, sticky=tk.W+tk.E)

# Configurações iniciais
entry_r_a.insert(0, "0")
entry_r_b.insert(0, "0")
entry_valor.insert(0, "0")
barramento_atual.set("A")

# Configuração do evento de rolagem do mouse na interface do barramento B
canvas = tk.Canvas(frame_b, height=100)
canvas.pack(side=tk.LEFT, fill=tk.Y)
scrollbar = tk.Scrollbar(frame_b, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind_all("<MouseWheel>", on_mousewheel)
canvas.create_window((0,0), window=entry_r_b)
label_barramento_c.config(relief=tk.RAISED)
update_canvas()

#Função de callback para a seleção do barramento C
def selecionar_barramento_c():
barramento_atual.set("C")
label_barramento_a.config(relief=tk.RAISED)
label_barramento_b.config(relief=tk.RAISED)
label_barramento_c.config(relief=tk.SUNKEN)
update_canvas()

#Função de callback para o botão Somar
def somar():
resultado.set(int(entry_r0.get()) + int(entry_r1.get()) + int(entry_r2.get()) + int(entry_r3.get()))

#Função de callback para o botão Resetar
def resetar():
entry_r0.delete(0, tk.END)
entry_r1.delete(0, tk.END)
entry_r2.delete(0, tk.END)
entry_r3.delete(0, tk.END)
resultado.set(0)

#Criação dos widgets para a interface principal
root = tk.Tk()
root.title("Interface Principal")

canvas = tk.Canvas(root)
canvas.grid(row=0, column=0, columnspan=3)

scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.grid(row=0, column=3, sticky=tk.NS)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

frame_registradores = tk.Frame(canvas)
canvas.create_window((0,0), window=frame_registradores, anchor=tk.W)

label_r0 = tk.Label(frame_registradores, text="R0:")
label_r0.grid(row=0, column=0)
entry_r0 = tk.Entry(frame_registradores)
entry_r0.grid(row=0, column=1)

label_r1 = tk.Label(frame_registradores, text="R1:")
label_r1.grid(row=1, column=0)
entry_r1 = tk.Entry(frame_registradores)
entry_r1.grid(row=1, column=1)

label_r2 = tk.Label(frame_registradores, text="R2:")
label_r2.grid(row=2, column=0)
entry_r2 = tk.Entry(frame_registradores)
entry_r2.grid(row=2, column=1)

label_r3 = tk.Label(frame_registradores, text="R3:")
label_r3.grid(row=3, column=0)
entry_r3 = tk.Entry(frame_registradores)
entry_r3.grid(row=3, column=1)

label_resultado = tk.Label(frame_registradores, text="Resultado:")
label_resultado.grid(row=4, column=0)
entry_resultado = tk.Entry(frame_registradores, state=tk.DISABLED)
entry_resultado.grid(row=4, column=1)

#Criação dos botões para seleção do barramento
barramento_atual = tk.StringVar()
label_barramento_a = tk.Label(frame_registradores, text="Barramento A", relief=tk.SUNKEN, width=15, anchor=tk.W)
label_barramento_a.grid(row=5, column=0, pady=5)
label_barramento_b = tk.Label(frame_registradores, text="Barramento B", relief=tk.RAISED, width=15, anchor=tk.W)
label_barramento_b.grid(row=5, column=1, pady=5)
label_barramento_c = tk.Label(frame_registradores, text="Barramento C", relief=tk.RAISED, width=15, anchor=tk.W)
label_barramento_c.grid(row=5, column=2, pady=5)

#Configuração dos callbacks para os eventos de clique nos botões de barramento
label_barramento_a.bind("<Button-1>", selecionar_barramento_a)
label_barramento_b.bind("<Button-1>", selecionar_barramento_b)
label_barramento_c.bind("<Button-1>", selecionar_barramento_c)

#Criação dos botões para somar e resetar
btn_somar = tk.Button(frame_registradores, text="Somar", command=somar)
btn_somar.grid(row=6, column=0, columnspan=2, pady=10)

btn_resetar = tk.Button(frame_registradores, text="Resetar", command=resetar)
btn_resetar.grid(row=6, column=2, pady=10)

#Variável para armazenar o resultado da soma
resultado = tk.StringVar()
resultado.set(0)

#Função auxiliar para atualizar o canvas
def update_canvas():
canvas.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))

root.mainloop()
