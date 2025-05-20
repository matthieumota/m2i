# Calculer le prix d'un billet avec réduction
is_senior = input('Est-ce que vous avez plus de 60 ans ? (o/n) ').lower() == 'o'
is_student = input('Est-ce que vous etes etudiant ? (o/n) ').lower() == 'o'

price = 50
student_discount = 20
senior_discount = 30

if is_student and not is_senior:
    price = price * ((100 - student_discount) / 100)
    print(f'Le prix du train est de {price} euros')
elif is_senior:
    discount = price * senior_discount / 100
    price = price - discount
    print(f'Le prix du train est de {price} euros avec une remise de {discount}')
else:
    print(f'Le prix du train est de {price} euros')
