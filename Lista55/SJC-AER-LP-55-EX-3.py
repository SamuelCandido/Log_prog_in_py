nota=float(input("Digite uma nota: "))
def conceito(nota):
    if nota >= 0.0 and nota <= 4.9:
        print("A nota:", nota,"Recebe o conceito 'D'.")
    elif nota >= 5.0 and nota <= 6.9:
        print("A nota:", nota,"Recebe o conceito 'C'.")
    elif nota >= 7.0 and nota <= 8.9:
        print("A nota:", nota,"Recebe o conceito 'B'.")
    elif nota >= 9.0 and nota <= 10.0:
        print("A nota:", nota,"Recebe o conceito 'A'.")
conceito(nota)
