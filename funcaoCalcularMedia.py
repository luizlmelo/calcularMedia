def calcularMedia(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

a = int(input("Digite a primeira nota: "))
b = int(input("Digite a segunda nota: "))
c = int(input("Digite a terceira nota: "))



if calcularMedia(a,b,c) >= 6:
        print("Aprovado")
else:
        print("Não aprovado")
print(f"A média total é = {calcularMedia(a, b, c):.2f}")
