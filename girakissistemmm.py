import tkinter as tk
from tkinter import messagebox


def calcular():
    try:
        # Entradas para as quantidades
        a = float(entry_a.get()) if entry_a.get() else 0
        b = float(entry_b.get()) if entry_b.get() else 0
        c = float(entry_c.get()) if entry_c.get() else 0
        d = float(entry_d.get()) if entry_d.get() else 0
        e = float(entry_e.get()) if entry_e.get() else 0
        f = float(entry_f.get()) if entry_f.get() else 0
        g = float(entry_g.get()) if entry_g.get() else 0
        h = float(entry_h.get()) if entry_h.get() else 0
        i = float(entry_i.get()) if entry_i.get() else 0
        j = float(entry_j.get()) if entry_j.get() else 0
        k = float(entry_k.get()) if entry_k.get() else 0
        l = float(entry_l.get()) if entry_l.get() else 0
        m = float(entry_m.get()) if entry_m.get() else 0
        n = float(entry_n.get()) if entry_n.get() else 0
        o = float(entry_o.get()) if entry_o.get() else 0

        # Calculando o NF e Peso
        nf = a * 0.05 + b * 0.14 + c * 0.08 + f * 0.04 + g * 0.10 + h * 57.00 + i * 195.00 + j * 19.00
        nf2 = d * 0.16 + e * 0.20 + k * 45.00 + l * 26.00 + m * 2.33 + n * 97.50 + o * 19.00
        peso = a * 0.01 + b * 0.01 + c * 0.01 + n * 6.00 + j * 6.00 + f * 0.03 + g * 0.03 + h * 6.00
        peso2 = d * 0.025 + e * 0.01 + i * 10.00 + k * 10.00 + m * 0.0035 + l * 0.5 + o * 10.00

        total_nf = nf + nf2
        total_peso = peso + peso2

        # Tamanhos das caixas (exemplo, ajustando conforme sua necessidade)
        caixa1 = (30, 30, 35)  # Exemplo de tamanho de caixa 1
        caixa2 = (30, 30, 35)  # Exemplo de tamanho de caixa 2
        caixa3 = (30, 30, 35)  # Exemplo de tamanho de caixa 3
        caixa4 = (30, 30, 35)  # Exemplo de tamanho de caixa 4
        caixa5 = (30, 30, 35)  # Exemplo de tamanho de caixa 5

        # Atualizando o resultado com NF, Peso e Tamanhos das caixas
        resultado_label.config(
            text=f"NF: R$ {total_nf:.2f}\nPeso: {total_peso:.2f} kg\n\n"
                 f"Tamanho das Caixas:\n"
                 f"Caixa 1: {caixa1[0]}x{caixa1[1]}x{caixa1[2]}\n"
                 f"Caixa 2: {caixa2[0]}x{caixa2[1]}x{caixa2[2]}\n"
                 f"Caixa 3: {caixa3[0]}x{caixa3[1]}x{caixa3[2]}\n"
                 f"Caixa 4: {caixa4[0]}x{caixa4[1]}x{caixa4[2]}\n"
                 f"Caixa 5: {caixa5[0]}x{caixa5[1]}x{caixa5[2]}"
        )

    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números!")


root = tk.Tk()
root.title("Gira Kids - Cálculo de Produtos")
root.geometry("500x600")

campos = ["1pol", "2pol", "27mm", "32mm", "45mm", "Cap 1", "Cap 2", "Square/Globinho",
          "GV Todas", "Pedestal X", "Hack", "Cuba", "Pelúcia", "Chiclete", "Pedestal Redondo"]
entries = []

for i, campo in enumerate(campos):
    tk.Label(root, text=campo).grid(row=i, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

(entry_a, entry_b, entry_c, entry_d, entry_e, entry_f, entry_g, entry_h,
 entry_i, entry_j, entry_k, entry_l, entry_m, entry_n, entry_o) = entries

botao_calcular = tk.Button(root, text="Calcular", command=calcular, bg="green", fg="white")
botao_calcular.grid(row=len(campos), column=0, columnspan=2, pady=20)

resultado_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
resultado_label.grid(row=len(campos) + 1, column=0, columnspan=2, pady=10)

root.mainloop()
