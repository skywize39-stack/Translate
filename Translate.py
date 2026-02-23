import time

from deep_translator import GoogleTranslator

while True:
    print("1 -> Translate")
    print("2 -> Exit")
    choose_action = (input("Enter your action >> ")).strip()
    if choose_action == "1":
        choose_language = input(
            "Enter target language -- 1.ru 2.en 3.de 4.fr 5.es 6.ja 7.it >> "
        )
        translat = GoogleTranslator(source="auto", target=choose_language)
        text = input("Enter your text >> ")
        print(f"Your translated text -> {translat.translate(text)}")
        input("Press any key...")
    elif choose_action == "2":
        print("Your action is Exit, Bye!")
        time.sleep(2)
        break
    else:
        print("You chose the wrong action!")

