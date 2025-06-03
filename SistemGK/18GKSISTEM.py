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
        def determinar_caixa(valores):
            qtd_1pol = valores[0]
            qtd_2pol = valores[1]
            qtd_27mm = valores[2]
            qtd_32mm = valores[3]
            qtd_45mm = valores[4]
            Caps1pol = valores[5]
            Caps2pol = valores[6]
            SquareGlobinho = valores[7]
            GVTodas = valores[8]
            PedestalX = valores[9]
            Hack = valores[10]
            Cuba = valores[11]
            Pelucia = valores[12]
            Chiclete = valores[13]
            PedestalRedondo = valores[14]

            div27 = qtd_27mm / 2000
            div2pol = qtd_2pol / 1000

            total_2pol = qtd_2pol + qtd_45mm  # 45mm = mesma caixa da 2pol

            # Regras simples e compostas
            if Caps1pol != 0 or Caps2pol != 0 or SquareGlobinho != 0 or GVTodas != 0 or PedestalX != 0 or Hack != 0 or Cuba != 0 or Pelucia != 0 or Chiclete != 0 or PedestalRedondo != 0:
                return "Personalizada (peças ou pelúcias)"
            if qtd_1pol == 100 and qtd_32mm <= 700:
                return "30x30x40"
            if qtd_1pol == 100 and qtd_27mm <= 1600:
                return "30x30x35"
            if qtd_1pol == 400 and qtd_32mm == 500:
                return "30x30x35"
            if 400 >= qtd_1pol >= 300 and 600 >= qtd_32mm >= 500 and 200 >= qtd_2pol >= 100:
                return "30x60x50"
            if qtd_2pol == 100 and (400 >= qtd_1pol > 100 or 500 > qtd_27mm > 250 or 500 > qtd_32mm > 100):
                return "30x60x50"
            if qtd_2pol == 100 and (qtd_1pol == 100 or qtd_27mm == 250 or qtd_32mm == 100):
                return "40x40x40"
            if 500 >= qtd_2pol >= 300:
                return "50x60x50"
            if 1000 >= qtd_2pol >500:
                return "70x50x60"
            if 400 >= qtd_2pol >= 300 and (qtd_1pol == 100 or qtd_27mm == 250 or qtd_32mm == 100):
                return "50x60x50"
            if 1100 > qtd_27mm >= 1000 and 1100 > qtd_32mm >= 1000:
                return "30x30x35 e 30x30x35"
            if 1500 >= qtd_2pol >= 1000 and (700 >= qtd_1pol > 0 or 1000 >= qtd_32mm > 0 or 2000 >= qtd_27mm > 0):
                return "70x50x60 e 40x40x40"
            if 1500 >= qtd_2pol >= 1000 and (2000 >= qtd_1pol > 1000 or 2000 >= qtd_32mm > 1000 or 4000 >= qtd_27mm > 2000):
                return "70x50x60 e 30x60x50"
            if 1500 >= qtd_2pol >= 1000:
                return "70x50x60 e 40x40x40"
            if 2000 >= qtd_2pol >= 1500:
                return "70x50x60 e 70x50x60"
            if 2000 >= qtd_2pol >= 1500 and (2000 >= qtd_1pol > 1200):
                return "70x50x60 e 70x60x50 e 30x30x35"
            if 400 >= qtd_45mm >= 300 and (qtd_1pol == 100 or qtd_27mm == 250 or qtd_32mm == 100 or qtd_2pol == 100):
                return "50x60x50"
            if 1100 > qtd_27mm >= 1000 and 1100 > qtd_32mm >= 1000:
                return "30x30x35 e 30x30x35"
            if 1500 >= qtd_45mm >= 1000 and (700 >= qtd_1pol > 0 or 1000 >= qtd_32mm > 0 or 2000 >= qtd_27mm > 0 or 500 >= qtd_2pol > 200):
                return "70x50x60 e 40x40x40"
            if 1500 >= qtd_45mm >= 1000 and (2000 >= qtd_1pol > 1000 or 2000 >= qtd_32mm > 1000 or 4000 >= qtd_27mm > 2000):
                return "70x50x60 e 30x60x50"
            if 1500 >= qtd_45mm >= 1000:
                return "70x50x60 e 40x40x40"
            if 2000 >= qtd_45mm >= 1500:
                return "70x50x60 e 70x50x60"
            if 2000 >= qtd_45mm >= 1500 and (2000 >= qtd_1pol > 1200):
                return "70x50x60 e 70x60x50 e 30x30x35"
            if 600 > total_2pol >= 500:
                return "40x40x40"
            if 500 > qtd_45mm > 0 and (700 >= qtd_1pol > 0 or 1000 >= qtd_32mm > 0 or 2000 >= qtd_27mm > 0):
                return "30x30x35 e 30x30x35"
            if 500 > qtd_45mm > 0 and (2000 >= qtd_1pol > 1000 or 2000 >= qtd_32mm > 1000 or 4000 >= qtd_27mm > 2000):
                return "30x30x35 e 30x50x60"
            if 500 > qtd_45mm > 0 and (2000 >= qtd_1pol > 1200):
                return "30x30x35 e 70x60x50 e 30x30x35"
            if 500 > qtd_45mm > 0 and (qtd_27mm > 4000 or qtd_32mm > 2000 or qtd_1pol > 2000 or qtd_2pol > 2000):
                return "30x30x35 e Personalizada"
            if 500 > qtd_45mm > 0:
                return "30x30x35"
            

            # Regras máximas por caixa
            if total_2pol == 1000 or qtd_1pol == 3000:
                return "70x50x60"
            if total_2pol == 500 or qtd_1pol == 1500 or qtd_27mm == 3000 or qtd_32mm == 2000:
                return "30x60x50"
            if qtd_1pol == 3000 or qtd_2pol == 700:
                return "50x60x50"
            if qtd_27mm > 3000:
                return f"30x30x35 x{div27}"
            if qtd_2pol > 1000:
                return f"70x50x60 x{div2pol}"
            
            # Se nada bater
            return "Personalizada"


        tamanhos = [determinar_caixa(valores)]

        # Exibindo os resultados na interface
        resultado_texto = f"NF: R$ {total_nf:.2f}\nPeso: {total_peso:.2f} kg\n\n"
        resultado_texto = f"NF: R$ {total_nf:.2f}\nPeso: {total_peso:.2f} kg\n\n"
        resultado_texto += f"Caixa Sugerida: {tamanhos[0]}\n\n"
        resultado_texto += "Resumo dos Produtos:\n"
        for i, campo in enumerate(campos):
            if valores[i] > 0:
                resultado_texto += f"- {campo}: {valores[i]} unidades\n"

        resultado_label.config(text=resultado_texto)

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Criando a interface gráfica
root = tk.Tk()
root.title("Gira Kids - Cálculo de Produtos")
root.geometry("500x800")

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