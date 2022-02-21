# função que permite calcular o MDC


def MDC(a, b):
  while(b != 0):
    resto = a % b
    a = b
    b = resto
 
  return a

# função principal do programa
def main():
  print("Este programa permite calcular o MDC\n")
  x = int(input("Informe o primeiro valor: "))
  y = int(input("Informe o segundo valor: "))
  print(f'O MDC É {MDC(x, y)}')

main()