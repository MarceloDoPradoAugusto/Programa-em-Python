import tkinter as tk

# Configuração da janela principal
root = tk.Tk()
root.title("Simulador de CPU")


ula_estado_operacao = tk.StringVar()

# Função chamada quando um botão de seleção de operação for clicado


def selecionar_operacao(operacao):
    ula_estado_operacao.set(operacao)

# Função para atualizar a interface gráfica quando os botões forem clicados


def update_interface():
    barramento_a = barramento_a_var.get()
    barramento_b = barramento_b_var.get()
    barramento_c = barramento_c_var.get()
    # Obtém o estado da operação selecionada na ULA
    operacao = ula_estado_operacao.get()
    resultado 

    # Executar a operação correspondente na ULA e atualizar os registradores
    if operacao == "adicao":
        resultado = int(barramento_a) + int(barramento_b)
    elif operacao == "subtracao":
        resultado = int(barramento_a) - int(barramento_b)
    elif operacao == "multiplicacao":
        resultado = int(barramento_a) * int(barramento_b)
    elif operacao == "divisao":
        resultado = int(barramento_a) / int(barramento_b)

    # Atualizar os valores nos registradores de acordo com o resultado da operação
    if barramento_c == "R0":
        r0_entry.delete(0, tk.END)
        r0_entry.insert(0, str(resultado))
    elif barramento_c == "R1":
        r1_entry.delete(0, tk.END)
        r1_entry.insert(0, str(resultado))
    elif barramento_c == "R2":
        r2_entry.delete(0, tk.END)
        r2_entry.insert(0, str(resultado))
    elif barramento_c == "R3":
        r3_entry.delete(0, tk.END)
        r3_entry.insert(0, str(resultado))


# Função para resetar o simulador ao estado inicial
def reset():
    r0_entry.delete(0, tk.END)
    r1_entry.delete(0, tk.END)
    r2_entry.delete(0, tk.END)
    r3_entry.delete(0, tk.END)


# Criação das caixas de texto para os registradores
r0_label = tk.Label(root, text="R0:")
r0_entry = tk.Entry(root)
r1_label = tk.Label(root, text="R1:")
r1_entry = tk.Entry(root)
r2_label = tk.Label(root, text="R2:")
r2_entry = tk.Entry(root)
r3_label = tk.Label(root, text="R3:")
r3_entry = tk.Entry(root)

# Criação das caixas de seleção para os barramentos
barramento_a_label = tk.Label(root, text="Barramento A:")
barramento_a_var = tk.StringVar(root)
barramento_a_var.set("R0")
barramento_a_optionmenu = tk.OptionMenu(
    root, barramento_a_var, "R0", "R1", "R2", "R3")
barramento_b_label = tk.Label(root, text="Barramento B:")
barramento_b_var = tk.StringVar(root)
barramento_b_var.set("R0")
barramento_b_optionmenu = tk.OptionMenu(
    root, barramento_b_var, "R0", "R1", "R2", "R3")
barramento_c_label = tk.Label(root, text="Barramento C:")
barramento_c_var = tk.StringVar(root)
barramento_c_var.set("R0")
barramento_c_optionmenu = tk.OptionMenu(
    root, barramento_c_var, "R0", "R1", "R2", "R3")

# Criação dos botões de seleção de operação da ULA
ula_adicao = tk.Button(root, text="Adição")
ula_subtracao = tk.Button(root, text="Subtração")
ula_multiplicacao = tk.Button(root, text="Multiplicação")
ula_divisao = tk.Button(root, text="Divisão")

# Criação do botão de execução
executar = tk.Button(root, text="Executar", command=update_interface)

# Criação do botão de reset
resetar = tk.Button(root, text="Resetar", command=reset)

# Posicionamento dos elementos na interface gráfica usando grid
r0_label.grid(row=0, column=0, sticky="e")
r0_entry.grid(row=0, column=1)
r1_label.grid(row=1, column=0, sticky="e")
r1_entry.grid(row=1, column=1)
r2_label.grid(row=2, column=0, sticky="e")
r2_entry.grid(row=2, column=1)
r3_label.grid(row=3, column=0, sticky="e")
r3_entry.grid(row=3, column=1)
barramento_a_label.grid(row=0, column=2, sticky="e")
barramento_a_optionmenu.grid(row=0, column=3)
barramento_b_label.grid(row=1, column=2, sticky="e")
barramento_b_optionmenu.grid(row=1, column=3)
barramento_c_label.grid(row=2, column=2, sticky="e")
barramento_c_optionmenu.grid(row=2, column=3)
ula_adicao.grid(row=4, column=0)
ula_subtracao.grid(row=4, column=1)
ula_multiplicacao.grid(row=4, column=2)
ula_divisao.grid(row=4, column=3)
executar.grid(row=5, column=0, columnspan=2)
resetar.grid(row=5, column=2, columnspan=2)

# Iniciar loop de eventos da interface gráfica
root.mainloop()
