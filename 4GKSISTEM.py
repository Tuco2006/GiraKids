import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        # Pegando os valores de entrada
        valores = [float(entry.get()) if entry.get().strip() else 0 for entry in entries]

        # Cálculo do NF e Peso
        nf = valores[0] * 0.05 + valores[1] * 0.14 + valores[2] * 0.08 + valores[5] * 0.04 + valores[6] * 0.10 + valores[7] * 57.00 + valores[8] * 195.00 + valores[9] * 19.00
        nf2 = valores[3] * 0.16 + valores[4] * 0.44 + valores[10] * 45.00 + valores[11] * 26.00 + valores[12] * 2.33 + valores[13] * 97.50 + valores[14] * 19.00
        peso = valores[0] * 0.01 + valores[1] * 0.01 + valores[2] * 0.01 + valores[13] * 6.00 + valores[9] * 6.00 + valores[5] * 0.003 + valores[6] * 0.006 + valores[7] * 6.00
        peso2 = valores[3] * 0.025 + valores[4] * 0.05 + valores[8] * 10.00 + valores[10] * 10.00 + valores[12] * 0.0035 + valores[11] * 0.5 + valores[14] * 10.00

        total_nf = nf + nf2
        total_peso = peso + peso2

        # Lógica para determinar o tamanho das caixas
        tamanhos = []
        regras_caixas = [
            (1000, 1500, 2000, '30x30x35', '40x40x40', '50x60x50', '70x50x60'),
            (100, 400, 1000, '30x30x35', '40x40x40', '50x60x50', '70x50x60'),
            (1000, 1500, 2000, '30x30x35', '40x40x40', '50x60x50', '70x50x60'),
            (800, 1200, 1700, '30x30x35', '40x40x40', '50x60x50', '70x50x60'),
            (500, 700, 1200, '30x30x35', '40x40x40', '50x60x50', '70x50x60')
        ]

        for i in range(min(5, len(valores))):  # Garantindo que a lista não estoure
            qtd = valores[i]
            limite1, limite2, limite3, tam1, tam2, tam3, tam4 = regras_caixas[i]

            if qtd <= limite1:
                tamanhos.append(tam1)
            elif qtd <= limite2:
                tamanhos.append(tam2)
            elif qtd <= limite3:
                tamanhos.append(tam3)
            else:
                tamanhos.append(tam4)

        # Exibindo os resultados na interface
        resultado_texto = f"NF: R$ {total_nf:.2f}\nPeso: {total_peso:.2f} kg\n\n"
        for i, tamanho in enumerate(tamanhos):
            resultado_texto += f"Caixa {i+1}: {tamanho} - {campos[i]}: {valores[i]} unidades\n"

        resultado_label.config(text=resultado_texto)

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Criando a interface gráfica
root = tk.Tk()
root.title("Gira Kids - Cálculo de Produtos")
root.geometry("500x700")

# Definindo os campos (produtos)
campos = ["1pol", "2pol", "27mm", "32mm", "45mm", "Cap 1", "Cap 2", "Square/Globinho",
          "GV Todas", "Pedestal X", "Hack", "Cuba", "Pelúcia", "Chiclete", "Pedestal Redondo"]
entries = []

# Criando a interface
for i, campo in enumerate(campos):
    tk.Label(root, text=campo).grid(row=i, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Botão de calcular
botao_calcular = tk.Button(root, text="Calcular", command=calcular, bg="green", fg="white")
botao_calcular.grid(row=len(campos), column=0, columnspan=2, pady=20)

# Label para exibir os resultados
resultado_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
resultado_label.grid(row=len(campos) + 1, column=0, columnspan=2, pady=10)

root.mainloop()
