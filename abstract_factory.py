class AbstractFactory:
    def create_product_a(self):
        pass
    
    def create_product_b(self):
        pass
    
class AbstractProductA:
    def do_something(self):
        pass
    
class AbstractProductB:
    def do_something_else(self):
        pass


class ConcreteProductA1(AbstractProductA):
    def do_something(self):
        return "Product A1"
    
class ConcreteProductA2(AbstractProductA):
    def do_something(self):
        return "Product A2"
    
class ConcreteProductB1(AbstractProductB):
    def do_something_else(self):
        return "Product B1"
    
class ConcreteProductB2(AbstractProductB):
    def do_something_else(self):
        return "Product B2"


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()
    
    def create_product_b(self):
        return ConcreteProductB1()
    
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()
    
    def create_product_b(self):
        return ConcreteProductB2()


def client_code(factory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    
    print(product_a.do_something())
    print(product_b.do_something_else())


factory1 = ConcreteFactory1()
client_code(factory1)

factory2 = ConcreteFactory2()
client_code(factory2)