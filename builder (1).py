class ComputerBuilder:
    def set_processor(self, processor):
        pass

    def set_memory(self, memory):
        pass

    def set_hard_drive(self, hard_drive):
        pass

    def set_video_card(self, video_card):
        pass

    def get_computer(self):
        pass

class ConcreteComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def set_processor(self, processor):
        self.computer.processor = processor

    def set_memory(self, memory):
        self.computer.memory = memory

    def set_hard_drive(self, hard_drive):
        self.computer.hard_drive = hard_drive

    def set_video_card(self, video_card):
        self.computer.video_card = video_card

    def get_computer(self):
        return self.computer
    
class Director:
    def __init__(self, builder):
        self.builder = builder

    def build_computer(self):
        self.builder.set_processor("Intel Core i7")
        self.builder.set_memory("16 GB")
        self.builder.set_hard_drive("1 TB")
        self.builder.set_video_card("Nvidia GeForce GTX 1080")

    def get_computer(self):
        return self.builder.get_computer()

class Computer:
    def __init__(self):
        self.processor = None
        self.memory = None
        self.hard_drive = None
        self.video_card = None

    def __str__(self):
        return f"Processor: {self.processor}, Memory: {self.memory}, Hard Drive: {self.hard_drive}, Video Card: {self.video_card}"
    
builder = ConcreteComputerBuilder()
director = Director(builder)
director.build_computer()
computer = director.get_computer()
print(computer)