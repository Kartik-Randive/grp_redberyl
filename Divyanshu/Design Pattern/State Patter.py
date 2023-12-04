from abc import ABC, abstractmethod

# Context
class Context:
    def __init__(self, state):
        self._state = state

    def request(self):
        self._state.handle()

    def set_state(self, state):
        self._state = state

# State Interface
class State(ABC):
    @abstractmethod
    def handle(self):
        pass

# Concrete States
class ConcreteStateA(State):
    def handle(self):
        print("Handling request in State A")
        # Optionally, change the state of the context
        # context.set_state(ConcreteStateB())

class ConcreteStateB(State):
    def handle(self):
        print("Handling request in State B")
        # Optionally, change the state of the context
        # context.set_state(ConcreteStateA())

# Client code
if __name__ == "__main__":
    # Creating instances
    state_a = ConcreteStateA()
    state_b = ConcreteStateB()
    context = Context(state_a)

    # Using the context with State A
    context.request()

    # Changing the state to State B
    context.set_state(state_b)

    # Using the context with State B
    context.request()
