import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        # Pegando os valores de entrada
        valores = [float(entry.get().replace(',', '.')) if entry.get().strip() else 0 for entry in entries]

        valor1 = valores[0] * 1.05
        valor2 = valores[0] * 1.16
        valor3 = valores[0] * 1.24
        valor4 = valores[0] * 1.25
        valor5 = valores[0] * 1.26
        valor6 = valores[0] * 1.67
        valor7 = valores[0] * 1.78
        valor8 = valores[0] * 1.92
        valor9 = valores[0] * 1.95
        valor10 = valores[0] * 1.97
        valor11 = valores[0] * 2.50
        valor12 = valores[0] * 7.90

        # Exibindo os resultados na interface
        resultado_texto = f"Valor1x: R$ {valor1:.2f}\nValor2x: {valor2:.2f}\nValor3x: {valor3:.2f}\nValor4x: {valor4:.2f}\nValor5x: {valor5:.2f}\nValor6x: {valor6:.2f}\nValor7x: {valor7:.2f}\nValor8x: {valor8:.2f}\nValor9x: {valor9:.2f}\nValor10x: {valor10:.2f}\nValor11x: {valor11:.2f}\nValor12x: {valor12:.2f} \n\n"

        resultado_label.config(text=resultado_texto)

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Criando a interface gráfica
root = tk.Tk()
root.title("Gira Kids - Cálculo de Parcelado")
root.geometry("500x500")

# Definindo os campos (produtos)
campos = ["Valor total do pedido R$:"]
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