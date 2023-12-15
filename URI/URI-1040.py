a, b, c, d = map(float, input().split())

weighted_avg = ((a * 2) + (b * 3) + (c * 4) + (d * 1)) / 10

print("Media: %.1f" % weighted_avg)

if weighted_avg >= 7.0:
    print("Aluno aprovado.")

elif weighted_avg < 5.0:
    print("Aluno reprovado.")

elif weighted_avg >= 5 and weighted_avg <= 6.9:
    print("Aluno em exame.")
    n = float(input())
    print("Nota do exame: %.1f" % n)
    final_avg = (weighted_avg + n) / 2
    if final_avg >= 5.0:
        print("Aluno aprovado.")

    elif final_avg <= 4.9:
        print("Aluno reprovado.")

    print("Media final: %.1f" % final_avg)

