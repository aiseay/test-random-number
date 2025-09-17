import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Pilih angka dari 1 sampai {x} ngab: '))
        if guess < random_number:
            print('Yah kekecilan, masukkin lagi coba.')
        elif guess > random_number:
            print('Kegedean ngab, masukkin lagi')

    print(f'Anjay bener dong {random_number}. Apakah kamu seorang dukun sakti? Nih permen buat lu 🍬')

guess(10)