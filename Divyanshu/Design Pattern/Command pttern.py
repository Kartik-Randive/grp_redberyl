from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete Command
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

# Receiver
class Light:
    def turn_on(self):
        print("Light is ON")

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

# Client code
if __name__ == "__main__":
    # Creating instances
    light = Light()
    light_on = LightOnCommand(light)
    remote = RemoteControl()

    # Setting the command
    remote.set_command(light_on)

    # Pressing the button
    remote.press_button()
