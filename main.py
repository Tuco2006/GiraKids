a = 0 # 1pol
b = 100 # 2pol
c = 250 # 27mm
d = 500 # 32mm
e = 0 # 45mm
f = 0 # cap 1 vazia
g = 0 # cap 2 vazia
h = 0 # square ou globinho
i = 0 # gv todas
j = 0 # pedestal x
k = 3 # hack
l = 0 # cuba
m = 0 # pelúcia
n = 2 # chiclete
o = 1 # pedestal redondo

nf = a * 0.05 + b * 0.14 + c * 0.08 + f * 0.04 + g * 0.10 + h * 57.00 + i * 195.00 + j * 19.00
nf2 = d * 0.16 + e * 0.20 + k * 45.00 + l * 26.00 + m * 2.33 + n * 97.50 + o * 19.00
peso = a * 0.01 + b * 0.01 + c * 0.01 + n * 6.00 + j * 6.00 + f * 0.03 + g * 0.03 + h * 6.00
peso2 = d * 0.025 + e * 0.01 + i * 10.00 + k * 10.00 + m * 0.0035 + l * 0.5 + o * 10.00

if a <= 1000:
    caixa1 = '30x30x35'
else:
    caixa1 = '40x40x40'

    if a <= 1500:
        caixa1 = '40x40x40'
    else:
        caixa1 = '50x60x50'

        if a < 2000:
            caixa1 = '50x60x50'
        else:
            caixa1 = '70x50x60'
if b <= 100:
    caixa2 = '30x30x35'
else:
    caixa2 = '40x40x40'

    if b <= 400:
        caixa2 = '40x40x40'
    else:
        caixa2 = '50x60x50'

        if b < 1000:
            caixa2 = '50x60x50'
        else:
            caixa2 = '70x50x60'
if c <= 1000:
    caixa3 = '30x30x35'
else:
    caixa3 = '40x40x40'

    if c <= 1500:
        caixa3 = '40x40x40'
    else:
        caixa3 = '50x60x50'

        if c <= 2000:
            caixa3 = '50x60x50'
        else:
            caixa3 = '70x50x60'
if d <= 800:
    caixa4 = '30x30x35'
else:
    caixa4 = '40x40x40'

    if d <= 1200:
        caixa4 = '40x40x40'
    else:
        caixa4 = '50x60x50'

        if d <= 1700:
            caixa4 = '50x60x50'
        else:
            caixa4 = '70x50x60'
if e <= 500:
    caixa5 = '30x30x35'
else:
    caixa5 = '40x40x40'

    if e <= 700:
        caixa5 = '40x40x40'
    else:
        caixa5 = '50x60x50'

        if e <= 1200:
            caixa5 = '50x60x50'
        else:
            caixa5 = '70x50x60'

print('nf', nf + nf2)
print('peso', peso + peso2)
print('caixa1', caixa1)
print('caixa2', caixa2)
print('caixa3', caixa3)
print('caixa4', caixa4)
print('caixa5', caixa5)