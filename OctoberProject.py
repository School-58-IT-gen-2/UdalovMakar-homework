#ПРОЕКТ ЕЩЁ В РАЗРАБОТКЕ!

import random as rand
import time
#import telebot as tbot


all_weapons = {'кулак':['кулак', 7, 3, 0, 'ближнее'], 'когти':['когти', 9, 3, 0, 'ближнее'], 'ПМ':['ПМ', 10, 4, 600, 'дальнее']}
all_simple_items = {'аптечка':['аптечка', 'health', 30, 12], 'бинты':['бинты', 'health', 10, 5], 'антирадин':['антирадин', 'infection', -15, 10]}
#stalker_names = ['Виталий', 'Принц', 'Цуцик']
#bot = tbot.TeleBot('6712575033:AAFi3-Juz0w3dlOSBNU4AAZDtYxwOAqrRTA')


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.infection = 0
        self.weapons = [all_weapons['ПМ'], all_weapons['кулак']]
        self.inventory = [['аптечка', 'health', 30, 12]]
        self.money = 50
    def death(self, progress):
        print(50 - progress, '[СМЕРТЬ] - В глазах темнеет... Кажется это конец...')
        input('Новая игра - enter')
        game()


class Enemy:
    def __init__(self, position, name, health, weapons, money, aggressive = False):
        self.name = name
        self.health = health
        self.weapons = weapons
        self.money = money
        self.aggressive = aggressive
    def fight(self, player):
        global all_weapons
        enemy_weapon = self.weapons[0]
        player_weapon = player.weapons[0]
        turn = True
        health = self.health
        print('--------БОЙ--------')
        time.sleep(1)
        print(f'{self.name} готовит {enemy_weapon[0]} для атаки...')
        while health > 0:
            if turn:
                choice = input(f'\nЧто собираешься делать? \n атака({player.weapons[0][0]}) - enter\n')
                if choice == '':
                    damage = [int(player_weapon[1] * (0.5 + rand.random())) for _ in range(player_weapon[2])]
                    health -= sum(damage)
                    print(f'нанесено {' + '.join(map(str, damage))} урона')
                    print(f'{self.name} имеет {max(0, health)} здоровья')
            else:
                time.sleep(1)
                print(f'\n{self.name} атакует!')
                damage = [int(enemy_weapon[1] * (0.5 + rand.random())) for _ in range(enemy_weapon[2])]
                print(f'нанесено {' + '.join(map(str, damage))} урона')
                player.health -= sum(damage)
                if player.health > 0:
                    print('ваше здоровье -', player.health)
                else:
                    print('ваше здоровье -', 0)
                    player.death()
            turn = not turn
        else:
            time.sleep(1)
            print(self.name, f'погибает, вы получаете {round(self.money * (0.5 + rand.random()), 2)}$')


class Person:
    def __init__(self, position, name, money, products):
        self.position = position
        self.name = name
        self.money = money
        self.products = products
    def meeting(self, player):
        print(f'[ВСТРЕЧА] - кажется это {self.name}')
        choice = None
        while choice != '':
            choice = input('Что собираешься делать?\n enter - уйти\n t -  торговаться')
            if choice == '':
                print('Ты сделал вид что не заметил его')
                break
            elif choice == 't':
                self.trade(player)
    def trade(self, player):
        products = self.products
        print(f'{self.name} показывает свои товары')
        product = None
        while len(self.products) != 0:
            for index in range(len(products)):
                print(f'{str(index + 1)} {products[index][0]} - {products[index][-1]}$')
            product = input(' введите номер товара\n enter - конец торговли\n')
            if product == '':
                break
            elif products[int(product) - 1][-1] <= player.money:
                player.money -= products[int(product) - 1][-1]
                player.inventory.append(products[int(product) - 1])
                print(f'Вы купили {products.pop(int(product) - 1)[0]}')
                print(f'Ваш баланс: {player.money}')


items_pos = {1:['аптечка', 'бинты', 'антирадин']}
zlovred = Enemy(1, 'зловред', 80, [all_weapons['когти']], 3.0, True)
trader = Person(1, 'Торговец', (0.5 + rand.random())*700, [all_simple_items[rand.choice(items_pos[1])] for _ in range(rand.randint(3, 6))])
enemies_pos = {1:[zlovred]}
persons_pos = {1:[trader]}


class Stage:
    def __init__(self, player):
        self.player = player
        self.seed = ['nothing']*50
        for position in range(1, 7):
            self.seed.insert(position*6 + rand.randint(-2, 2), 'enemy')
        self.seed.insert(15, 'person')
        self.seed.insert(27, 'person')
        self.seed.insert(39, 'person')
        self.pos = self.seed[0]
        self.progress = 0
        self.location = 'desert'
        self.stage = 1
        print('PyZone Отчет:')
        print(f'50км [НАЧАЛО] - {player.name}, вы лежите посреди железной дороги. Вы не знаете что было ранее, единственное что понятно, надо идти вперёд...')
    def check(self, pos, location, player):
        if location == 'desert':
            choice = input('Что собираешься делать?\n идти - enter\n посмотреть инвентарь - i\n использовать предмет - u\n')
            if choice == '':
                if self.progress < 50:
                    self.progress += 1
                    self.pos = self.seed[self.progress]
                    eval(f'self.{pos}(self.player, self.location, self.seed, self.progress, self.stage)')
                    self.check(self.pos, self.location, player)
                else:
                    self.final()
            elif choice == 'i':
                print('Ваш инвентарь:')
                print(' '.join([' ' + item[0] + '\n' for item in player.inventory]))
                self.check(self.pos, self.location, player)
            elif choice == 'u':
                print('Ваш инвентарь:')
                print(''.join([' ' + item[0] + '\n' for item in player.inventory]))
                for index in range(len(player.inventory)):
                    print(index + 1, player.inventory[index])
                choice = int(input('Введите номер предмета который хотите использовать')) - 1
                eval(f'player.{player.inventory[choice][1]} += {player.inventory[choice][2]}')
                self.check(self.pos, self.location, player)
    def nothing(self, player, location, seed, progress, stage):
        print(f'{50 - progress}км [ПУСТО]')
    def enemy(self, player, location, seed, progress, stage):
        global enemies_pos
        global clear
        enemy = rand.choice(enemies_pos[stage])
        print(f'{50 - progress}км [ВРАГ] - это {enemy.name}!')
        time.sleep(1)
        enemy.fight(player)
    def person(self, player, location, seed, progress, stage):
        global persons_pos
        person = rand.choice(persons_pos[stage])
        person.meeting(player)
    def final(self):
        print('Вот ты и дошел до ворот города, но что будет дальше?')
        print('Продолжение следует...(в разработке)')


def game():
    hero = Player(input('Как нам вас называть?(ни на что никогда не повлияет)\n'))
    stage = Stage(hero)
    stage.check(stage.pos, stage.location, hero)
game()
#bot.polling(non_stop=True)