def yes_no(what, wrong_answer):
    while True:
        choice = input(what).lower()
        ans = choice.isdigit()
        if ans is True:
            return choice
        print(wrong_answer)


what2 = "Fodselsnummer :"
wrong_answer = "Oops something is buggy\n"
print(yes_no(what2, wrong_answer))
