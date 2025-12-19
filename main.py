class Hero:
    def __init__(self, name: str):
        self.name = name
        self.hp = 100
        self.inventory: list[str] = []
        self.is_alive = True

    def take_damage(self, amount: int):
        if not self.is_alive:
            print(f"{self.name} уже повержен")
            return
        self.hp -=amount
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
            print(f"{self.name} теперь повержен")
        else:
            print(f"{self.name} получил {amount} урона")
    
    def heal(self, amount):
        if not self.is_alive:
            print(f"{self.name} уже повержен")
            return
        self.hp = min(self.hp + amount, 100)
        print(f"{self.name} восстановил {amount} НР. Текущие НР {self.hp}")

    def add_item(self, item: str):
        self.inventory.append(item)
        print(f"{self.name} получил предмет {item}")

    def show_status(self):
        status = "Жив" if self.is_alive else "Повержен"
        print(f"{self.name} - НР: {self.hp} - Инвентарь: {self.inventory} [{status}]")

hero = Hero("Вася")
hero.add_item("Меч")
hero.show_status()
hero.take_damage(30)
hero.take_damage(60)
hero.heal(50)
hero.show_status()