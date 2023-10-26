def encode(user_pw):
    key = {
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 0,
        11: 1,
        12: 2
    }
    global encoded_str_pw
    for i in range(8):
        encoded_user_pw.append(key[(int(user_pw[i]) + 3)])
        encoded_digit = str(encoded_user_pw[i])
        encoded_str_pw = encoded_str_pw + encoded_digit
    return encoded_str_pw

encoded_user_pw = []
encoded_str_pw = ''
if __name__ == '__main__':

    menu_run = True

    while menu_run:
        print('Menu\n-------------')
        print('1. Encode\n2. Decode\n3. Quit')
        print('')
        user_selection = int(input('Please enter an option:'))
        if user_selection == 1:
            user_pw = (input('Please enter your password to encode: '))
            print('Your password has been encoded and stored!')
            print()
            new_encoded_pw = encode(user_pw)
        if user_selection == 2:
            print(f'The encoded password is {new_encoded_pw}, and the original password is {user_pw}.')
        if user_selection == 3:
            menu_run = False
