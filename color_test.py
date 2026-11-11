from colorama import Fore
color = input("What is your favourite color? ").lower()

match color:
    case "red":
        print(Fore.RED +"You are energetic and confident.")
    case "blue":
        print(Fore.BLUE + "You are calm and thoughtful.")
    case "green":
        print(Fore.GREEN + "You are balanced and patient.")
    case "yellow":
        print(Fore.YELLOW +"You are optimistic and creative.")
    case _:
        print(Fore.MAGENTA +"You are a magical unicorn.")