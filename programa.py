import tkinter as tk

# Configuração da janela principal
root = tk.Tk()
root.title("Simulador de CPU")

# Função para resetar o simulador ao estado inicial


def reset():
    for entry in r_entries.values():
        entry.delete(0, tk.END)
    barramento_a_var.set("R0") # Define o valor padrão do Barramento A como "R0"
    barramento_b_var.set("R0") # Define o valor padrão do Barramento B como "R0"
    barramento_c_var.set("R0") # Define o valor padrão do Barramento C como "R0"

# Verifica o valor nos registradores


def PeekR():
    r_values = {}
    for label in r_labels:
        r_entry = r_entries[label]
        value = r_entry.get()  # Obter o valor da caixa de texto
        # Tentar converter o valor para um número inteiro
        try:
            r_value = int(value)
        except ValueError:
            # Se a conversão falhar, definir um valor padrão, por exemplo, 0
            r_value = 0
        r_values[label] = r_value
    return r_values

# Função auxiliar para atualizar caixa de texto do registrador


def atualizar_caixa_texto(resultado, barramento_c_label, r_entries):
    if barramento_c_label in r_entries:
        r_entry = r_entries[barramento_c_label]
        r_entry.delete(0, tk.END)
        r_entry.insert(0, str(resultado))

# Função para obter os valores atuais dos registradores


def peek_r(r_labels, r_entries):
    r_values = {}
    for label in r_labels:
        r_entry = r_entries[label]
        value = r_entry.get()  # Obter o valor da caixa de texto
        # Tentar converter o valor para um número inteiro
        try:
            r_value = int(value)
        except ValueError:
            # Se a conversão falhar, definir um valor padrão, por exemplo, 0
            r_value = 0
        r_values[label] = r_value
    return r_values

# Criação da variável de operação
operacao_var = tk.StringVar()

# Função que executará as operações na interface gráfica.

def update_interface():
    # Obtém a operação selecionada
    operacao = operacao_var.get()

    # Chama a função correspondente com base na operação selecionada
    if operacao == "Adição":
        adicao()
    elif operacao == "Subtração":
        subtracao()
    elif operacao == "Multiplicação":
        multiplicacao()
    elif operacao == "Divisão":
        divisao()

# Função para realizar a adição


def adicao():
    # Obtém o rótulo do registrador A selecionado
    barramento_a_label = barramento_a_var.get()
    # Obtém o rótulo do registrador B selecionado
    barramento_b_label = barramento_b_var.get()
    # Obtém o rótulo do registrador C selecionado
    barramento_c_label = barramento_c_var.get()
    # Obtém os valores atuais dos registradores
    r_values = peek_r(r_labels, r_entries)
    # Obtém o valor correto do registrador A selecionado
    barramento_a = r_values[barramento_a_label]
    # Obtém o valor correto do registrador B selecionado
    barramento_b = r_values[barramento_b_label]
    resultado = barramento_a + barramento_b  # Realiza a operação
    # Atualiza o valor do registrador C com o resultado
    r_values[barramento_c_label] = resultado

    atualizar_caixa_texto(resultado, barramento_c_label, r_entries)

# Função para realizar a subtração


def subtracao():
    # Obtém o rótulo do registrador A selecionado
    barramento_a_label = barramento_a_var.get()
    # Obtém o rótulo do registrador B selecionado
    barramento_b_label = barramento_b_var.get()
    # Obtém o rótulo do registrador C selecionado
    barramento_c_label = barramento_c_var.get()
    # Obtém os valores atuais dos registradores
    r_values = peek_r(r_labels, r_entries)
    # Obtém o valor correto do registrador A selecionado
    barramento_a = r_values[barramento_a_label]
    # Obtém o valor correto do registrador B selecionado
    barramento_b = r_values[barramento_b_label]
    resultado = barramento_a - barramento_b  # Realiza a operação
    # Atualiza o valor do registrador C com o resultado
    r_values[barramento_c_label] = resultado

    atualizar_caixa_texto(resultado, barramento_c_label, r_entries)

# Função para realizar a multiplicação


def multiplicacao():
    # Obtém o rótulo do registrador A selecionado
    barramento_a_label = barramento_a_var.get()
    # Obtém o rótulo do registrador B selecionado
    barramento_b_label = barramento_b_var.get()
    # Obtém o rótulo do registrador C selecionado
    barramento_c_label = barramento_c_var.get()
    # Obtém os valores atuais dos registradores
    r_values = peek_r(r_labels, r_entries)
    # Obtém o valor correto do registrador A selecionado
    barramento_a = r_values[barramento_a_label]
    # Obtém o valor correto do registrador B selecionado
    barramento_b = r_values[barramento_b_label]
    resultado = barramento_a * barramento_b  # Realiza a operação
    # Atualiza o valor do registrador C com o resultado
    r_values[barramento_c_label] = resultado

    atualizar_caixa_texto(resultado, barramento_c_label, r_entries)

# Função para realizar a divisão


def divisao():
    # Obtém o rótulo do registrador A selecionado
    barramento_a_label = barramento_a_var.get()
    # Obtém o rótulo do registrador B selecionado
    barramento_b_label = barramento_b_var.get()
    # Obtém o rótulo do registrador C selecionado
    barramento_c_label = barramento_c_var.get()
    # Obtém os valores atuais dos registradores
    r_values = peek_r(r_labels, r_entries)
    # Obtém o valor correto do registrador A selecionado
    barramento_a = r_values[barramento_a_label]
    # Obtém o valor correto do registrador B selecionado
    barramento_b = r_values[barramento_b_label]

    if barramento_b != 0:
        # Realiza a operação de divisão inteira
        resultado = barramento_a // barramento_b
        # Atualiza o valor do registrador C com o resultado
        r_values[barramento_c_label] = resultado
        atualizar_caixa_texto(resultado, barramento_c_label, r_entries)
    else:
        # Lidar com erro de divisão por zero
        tk.messagebox.showerror("Erro", "Divisão por zero não é permitida.")


# Criação das caixas de texto para os registradores
r_entries = {}  # Dicionário para armazenar as entradas r_entry

# Lista dos rótulos para as entradas r_entry em maiúsculas
r_labels = ['R0', 'R1', 'R2', 'R3']
for label in r_labels:
    r_entries[label] = tk.Entry(root)

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

# Criação do botão de execução
executar = tk.Button(root, text="Executar", command=update_interface)

# Função para atualizar a variável de operação
def atualizar_operacao(value):
    operacao_var.set(value)

# Criação dos botões de seleção de operação da ULA
ula_adicao = tk.Button(root, text="Adição", command=lambda: atualizar_operacao("Adição"))
ula_subtracao = tk.Button(root, text="Subtração", command=lambda: atualizar_operacao("Subtração"))
ula_multiplicacao = tk.Button(root, text="Multiplicação", command=lambda: atualizar_operacao("Multiplicação"))
ula_divisao = tk.Button(root, text="Divisão", command=lambda: atualizar_operacao("Divisão"))


# Criação do botão de reset
resetar = tk.Button(root, text="Resetar", command=reset)

# Posicionamento dos elementos na interface gráfica usando grid
for i, label in enumerate(r_labels):
    r_label = tk.Label(root, text=label.upper() + ":")
    r_entry = r_entries[label]
    r_label.grid(row=i, column=0, sticky="e")
    r_entry.grid(row=i, column=1)

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
