from random import randint

print("_____X and O_____")

G_MAP = ["", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]", "[]"]


class X_and_O:
    def START(self):
        print(G_MAP[1], G_MAP[2], G_MAP[3])
        print(G_MAP[4], G_MAP[5], G_MAP[6])
        print(G_MAP[7], G_MAP[8], G_MAP[9])

    def RUN(self):
        tries = 0
        symbol = ""
        bot_s = ""
        a = input("X or O")
        if a == "X" or a == "O":
            symbol = a
            if a == "X":
                bot_s = "O"
            else:
                bot_s = "X"
        else:
            print("Please run again and enter X or O")
        run = True
        bot_tries = []

        while run:
            bot = randint(1, 9)
            if bot not in bot_tries:

                G_MAP[bot] = f"[{bot_s}]"
                bot_tries += [bot]
            else:
                continue

            hod = int(input("Where symbol?"))
            G_MAP[hod] = f"[{symbol}]"
            print(G_MAP[1], G_MAP[2], G_MAP[3])
            print(G_MAP[4], G_MAP[5], G_MAP[6])
            print(G_MAP[7], G_MAP[8], G_MAP[9])

            if G_MAP[2] == f"[{bot_s}]" and G_MAP[5] == f"[{bot_s}]" and G_MAP[8] == f"[{bot_s}]":
                print("YOU LOSE")
                run = False
                print(tries)
            elif G_MAP[2] == f"[{symbol}]" and G_MAP[5] == f"[{symbol}]" and G_MAP[8] == f"[{symbol}]":
                print("YOU WIN")
                run = False
                print(tries)

            if G_MAP[3] == f"[{bot_s}]" and G_MAP[5] == f"[{bot_s}]" and G_MAP[7] == f"[{bot_s}]":
                print("YOU LOSE")
                run = False
                print(tries)
            elif G_MAP[3] == f"[{symbol}]" and G_MAP[5] == f"[{symbol}]" and G_MAP[7] == f"[{symbol}]":
                print("YOU WIN")
                run = False
                print(tries)

            if G_MAP[1] == f"[{bot_s}]" and G_MAP[5] == f"[{bot_s}]" and G_MAP[9] == f"[{bot_s}]":
                print("YOU LOSE")
                run = False
                print(tries)
            elif G_MAP[1] == f"[{symbol}]" and G_MAP[5] == f"[{symbol}]" and G_MAP[9] == f"[{symbol}]":
                print("YOU WIN")
                run = False
                print(tries)

            if G_MAP[4] == f"[{bot_s}]" and G_MAP[5] == f"[{bot_s}]" and G_MAP[6] == f"[{bot_s}]":
                print("YOU LOSE")
                run = False
                print(tries)
            elif G_MAP[4] == f"[{symbol}]" and G_MAP[5] == f"[{symbol}]" and G_MAP[6] == f"[{symbol}]":
                print("YOU WIN")
                run = False
                print(tries)


# tries += 1
G = X_and_O()
G.START()
G.RUN()
