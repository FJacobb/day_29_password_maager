import random

ALPHABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
NUMBER = ["0","1","2","3","4","5","6","7","8","9"]
SYMBOL = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', '<', '>', ',', '.', '/', '?']
class PassGenerate:
    def __init__(self):
        self.password_length = 0
        self.password_list = []
        pass

    def computer_selection(self):
        self.password_length = random.randint(8, 15)
        self.password_lenght_black()
        random.shuffle(self.password_list)
        password = "".join(self.password_list)
        self.password_list.clear()
        return password

    def password_lenght_black(self):
        ap = 1
        num = 1
        sym = 1
        while ap+num+sym != self.password_length:
            ap = random.randint(1,self.password_length)
            num = random.randint(1,self.password_length)
            sym = random.randint(1,self.password_length)
            if ap+num+sym == self.password_length:
                for x in range(ap):
                    if random.randint(1,2) == 1:
                        self.password_list.append(random.choice(ALPHABET).upper())
                    else:
                        self.password_list.append(random.choice(ALPHABET))
                for x in range(num):
                    self.password_list.append(random.choice(NUMBER))
                for x in range(sym):
                    self.password_list.append(random.choice(SYMBOL))
                break

