import random
class Ant:
    def __init__(self, x_coord, y_coord, object_list, board_length):
        self.x = x_coord
        self.y = y_coord
        self.obj = object_list
        self.length = board_length
        self.movelist = [(self.x, self.y)]
        self.imagedata = '''R0lGODlhDgAOAHAAACH5BAEAAPwALAAAAAAOAA4AhwAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwAr
ZgArmQArzAAr/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCq
mQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMA
zDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA
/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YA
AGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaA
M2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/
Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplV
mZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnV
zJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr
/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zV
AMzVM8zVZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8r
M/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+q
Zv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAA
AAh3APcJFJNJoMBMYgwqEzgpobKFBAUqi1FwHxo0AACgSbgvU4x9FPcRy5hx4aQbBsXEIEkyxo16
BqERg7YiY4yHBnPuu2FTJ8ufP3NmYlkxp7JJxAzYJJZpocB6NzD+FHPDaQxi+8SwTEjsIwCn+1gq
BKAzLFmdAQEAOw=='''

    def valid_move(self, new_x, new_y):
        if new_x == -1 or new_y == -1 or new_x == self.length or new_y == self.length:
            return False
        if self.obj[new_x][new_y] == 1:
            return False

        return True

    """def valid_move(self, new_x, new_y):
        if new_x == -1 or new_y == -1 or new_x == length or new_y == length:
            return False
        for thing in self.obj:
            foo, bar = thing.x, thing.y
            if new_x == foo or new_y == bar:
                return False
        return True"""

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def make_rand_move(self):
        foo = random.randint(0, 3)
        if foo == 0:
            new_x = self.x+1
            if self.valid_move(new_x, self.y):
                self.x = new_x
            else:
                self.make_rand_move()
        if foo == 1:
            new_x = self.x-1
            if self.valid_move(new_x, self.y):
                self.x = new_x
            else:
                self.make_rand_move()
        if foo == 2:
            new_y = self.y+1
            if self.valid_move(self.x, new_y):
                self.y = new_y
            else:
                self.make_rand_move()
        if foo == 3:
            new_y = self.y-1
            if self.valid_move(self.x, new_y):
                self.y = new_y
            else:
                self.make_rand_move()

        newc = (self.x, self.y)
        self.movelist.append(newc)
        return newc

    def get_movelist(self):
        return self.movelist
