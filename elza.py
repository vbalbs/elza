# Worked with luisa Ribeiro Bezerra
def calculaValor(v, candidato, T):
    final = 0;
    for elemv in v:
        if elemv <= candidato:
            final += candidato*T
        elif elemv <= 1.05*candidato:
            final += elemv*T
        else:
            final += T*(candidato + (elemv - candidato)*2)
    return final


v = []
T = float(input("Digite a tarifa: "))
for i in range(12):
    print("Digite o gasto do mês " + str(i+1) + ": ")
    v.append(float(input()))
candidate = min(v)
end = max(v)
avg = float(sum(v)/len(v))
opt = calculaValor(v, candidate, T)
cand_opt = candidate
while (candidate <= end):
    candidate += 0.1
    localtest = calculaValor(v, candidate, T)
    if (localtest < opt):
        opt = localtest
        cand_opt = candidate

print("O valor minimo de pagamento eh: " + str(round(opt, ndigits=2)))
print("A taxa otima eh:" + str(round(cand_opt, ndigits=2)))
print("A media dos valores eh:" + str(round(avg, ndigits=2)))
