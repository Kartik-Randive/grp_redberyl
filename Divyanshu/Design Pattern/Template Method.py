from abc import ABC, abstractmethod

# Abstract Class with Template Method
class AbstractClassTemplate(ABC):
    def template_method(self):
        self.step_one()
        self.step_two()
        self.step_three()

    @abstractmethod
    def step_one(self):
        pass

    @abstractmethod
    def step_two(self):
        pass

    @abstractmethod
    def step_three(self):
        pass

# Concrete Class implementing the Template Method
class ConcreteClassA(AbstractClassTemplate):
    def step_one(self):
        print("ConcreteClassA: Step One")

    def step_two(self):
        print("ConcreteClassA: Step Two")

    def step_three(self):
        print("ConcreteClassA: Step Three")

# Concrete Class implementing the Template Method
class ConcreteClassB(AbstractClassTemplate):
    def step_one(self):
        print("ConcreteClassB: Step One")

    def step_two(self):
        print("ConcreteClassB: Step Two")

    def step_three(self):
        print("ConcreteClassB: Step Three")

# Client code
if __name__ == "__main__":
    # Using ConcreteClassA
    print("Using ConcreteClassA:")
    concrete_a = ConcreteClassA()
    concrete_a.template_method()

    # Using ConcreteClassB
    print("\nUsing ConcreteClassB:")
    concrete_b = ConcreteClassB()
    concrete_b.template_method()
