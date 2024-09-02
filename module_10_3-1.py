import threading
import random
import time


class Bank:

    def __init__(self):
        self.balance = 0
        self.locker = threading.Lock()

    def deposit(self):
        for _ in range(10):
            money = random.randint(50, 500)
            
            self.locker.acquire()

            self.balance += money
            print(f"Пополнение: {money}. Баланс: {self.balance}")

            self.locker.release()
            time.sleep(0.1)

    def take(self):
        for _ in range(10):
            money = random.randint(50, 500)
            print(f"Запрос на {money}")
            
            self.locker.acquire()

            if money <= self.balance:
                self.balance -= money
                print(f"Снятие: {money}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")

            self.locker.release() 
            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
