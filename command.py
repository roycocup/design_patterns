class Button():
    def __init__(self, command):
        self.command = command

    def execute(self):
        self.command.execute()

class Command():
    def execute(self):
        pass

class SayHello(Command):
    def execute(self):
        print("hello")

class SayNotAgain(Command):
    def execute(self):
        print("Not again!")



if __name__ == "__main__":
    b1 = Button(SayHello())
    b2 = Button(SayNotAgain())
    b1.execute()
    b2.execute()
