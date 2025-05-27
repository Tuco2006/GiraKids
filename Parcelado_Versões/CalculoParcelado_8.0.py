import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        # Pegando os valores de entrada
        valores = [float(entry.get().replace(',', '.')) if entry.get().strip() else 0 for entry in entries]

        valor1 = (valores[0] * 0.331) + valores[0]
        valor2 = (valores[0] * 0.450) + valores[0]
        valor3 = (valores[0] * 0.532) + valores[0]
        valor4 = (valores[0] * 0.617) + valores[0]
        valor5 = (valores[0] * 0.699) + valores[0]
        valor6 = (valores[0] * 0.782) + valores[0]
        valor7 = (valores[0] * 0.850) + valores[0]
        valor8 = (valores[0] * 0.950) + valores[0]
        valor9 = (valores[0] * 1.050) + valores[0]
        valor10 = (valores[0] * 1.150) + valores[0]
        valor11 = (valores[0] * 1.250) + valores[0]
        valor12 = (valores[0] * 1.450) + valores[0]

        # Exibindo os resultados na interface
        resultado_texto = f"Formas de pagamento:\n\nValor em 1x: R$ {valor1:.2f}\n\nValor em 2x: R$ {valor2:.2f}\n\nValor em 3x: R$ {valor3:.2f}\n\nValor em 4x: R$ {valor4:.2f}\n\nValor em 5x: R$ {valor5:.2f}\n\nValor em 6x: R$ {valor6:.2f}\n\nValor em 7x: R$ {valor7:.2f}\n\nValor em 8x: R$ {valor8:.2f}\n\nValor em 9x: R$ {valor9:.2f}\n\nValor em 10x: R$ {valor10:.2f}\n\nValor em 11x: R$ {valor11:.2f}\n\nValor em 12x: R$ {valor12:.2f} \n\n"

        resultado_label.config(text=resultado_texto)

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Criando a interface gráfica
root = tk.Tk()
root.title("Gira Kids - Cálculo de Parcelado")
root.geometry("500x600")

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