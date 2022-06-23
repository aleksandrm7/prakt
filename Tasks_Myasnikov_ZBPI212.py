# 7. Понятие класса и объекта. Определение класса и создание
# экземпляра класса.
#
# Task 1. Count Number of Instances
#
# Create a class named User and create a way to check
# the number of users (number of instances) that were created,
# so that the value can be accessed as a class attribute.
#
# source: https://edabit.com/challenge/rprukfcGWqnvKZR9g

class User:
    created = 0

    def __init__(self, name):
        self.name = name
        User.created += 1

def test_task1():
    user1 = User('master_lin')
    assert user1.name == 'master_lin', 'Ошибка user1.name'
    assert User.created == 1, 'Ошибка User.created (1)'
    user2 = User('andy_rex')
    assert User.created == 2, 'Ошибка User.created (2)'

# Task 2. Wait... Who Am I?
#
# Hello there, I... seem to not remember who I am, my memories is all...
# cloudy, although maybe if I could piece it together...
#
# Oh! Maybe you could help me make a class that helps me remember things.
# Maybe a method called add that would add to my memory if I would recall
# things and a remember method that would let me recall a specific memory.
#
# But you have to make add more flexible, I might recall many things in an
# instant or only one that I would forget again.
#
# source: https://edabit.com/challenge/m9zn9v3Q6oG8zBdja

class Memories:

    def __init__(self):
        self.data_to_remember = {}

    def add(self, **kwargs):
        for k, v  in kwargs.items():
            self.data_to_remember[k] = v

    def remember(self, key):
        if key in self.data_to_remember:
            return self.data_to_remember[key]
        else:
            return False

    def print_memories(self):
        for k,v in self.data_to_remember.items():
            print(k,':',v)

def test_task2():
    memories = Memories()
    memories.add(name='Alex', age='35')
    memories.add(city='Moscow')
    memories.add(wife='Angela', kids='Evgeniy, Elena')
    assert memories.remember('address') == False, 'Ошибка memories.remember (address)'
    assert memories.remember('city') == 'Moscow', 'Ошибка memories.remember (city)'
    assert memories.remember('kids') == 'Evgeniy, Elena', 'Ошибка memories.remember (kids)'

# Task 3
#
# This challenge is an English twist on the Japanese word game Shiritori.
# The basic premise is to follow two rules:
# First character of next word must match last character of previous word.
# The word must not have already been said.
#
# source: https://edabit.com/challenge/dLnZLi8FjaK6qKcvv

class Shiritori:

    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        if not self.game_over:
            if word not in self.words:
                if len(self.words) == 0:
                    self.words.append(word)
                    return self.words
                elif self.words[-1][-1] == word[0]:
                    self.words.append(word)
                    return self.words
                else:
                    self.game_over = True
                    return 'game over'
        else:
            return 'game over'

    def restart(self):
        self.words = []
        self.game_over = False
        return 'game restarted'

def test_task3():
    my_shiritori = Shiritori()

    assert my_shiritori.play("apple") == ["apple"], 'Ошибка my_shiritori.play("apple")'
    assert my_shiritori.play("ear") == ["apple", "ear"], 'Ошибка my_shitori.play("ear")'
    assert my_shiritori.play("rhino") == ["apple", "ear", "rhino"], 'Ошибка my_shitori.play("rhino")'
    assert my_shiritori.play("corn") == "game over", 'Ошибка my_shitori.play("corn")'
    assert my_shiritori.words == ["apple", "ear", "rhino"], 'Ошибка my_shitori.words (1)'
    assert my_shiritori.game_over == True, 'Ошибка my_shitori.game_over (1)'
    assert my_shiritori.restart() == 'game restarted', 'Ошибка my_shiriotri.restart()'
    assert my_shiritori.words == [], 'Ошибка my_shiriotri.words (2)'
    assert  my_shiritori.play("hostess") == ["hostess"], 'Ошибка my_shiritori.play("hostess") (1)'
    my_shiritori.play("stash") == ["hostess", "stash"], 'Ошибка my_shiritori.play("stash")'
    my_shiritori.play("hostess") == "game over", 'Ошибка my_shiritori.play("hostess") (2)'

test_task1()
test_task2()
test_task3()