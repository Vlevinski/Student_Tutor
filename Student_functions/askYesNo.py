def yes_no(what, wrong_answer):
    while True:
        choice = input(what).lower()
        if choice[:1] == 'y':
            return True
        elif choice[:1] == 'n':
            return False
        else:
            print(wrong_answer)


what1 = "Would you like to enter a student’s information? Type Y for Yes or N for No:"
wrong_answer = "Oops something is buggy\n"

print(yes_no(what1, wrong_answer))

