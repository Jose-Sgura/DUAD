class Head:
    def __init__(self, eyes, mouth, nose):
        self.eyes= eyes
        self.mouth= mouth
        self.nose= nose
class Torso:
    def __init__(self, heart, lungs):
        self.heart=heart
        self.lungs=lungs

class Arm:
    def __init__(self, side):
        self.side= side
class Hand:
    def __init__(self, fingers):
        self.fingers=fingers
        

class Leg:
    def __init__(self, side):
        self.side=side
    

class Feet:
    def __init__(self, toes):
        self.toes=toes
class Human:
    def __init__(self,name):
        self.name=name
        self.head=Head(eyes=2,mouth=1,nose=1)
        self.torso=Torso(heart=1, lungs=2)
        self.left_arm = Arm("left")
        self.right_arm = Arm("right")
        self.left_hand = Hand(fingers=5)
        self.right_hand = Hand(fingers=5)
        self.left_leg = Leg("left")
        self.right_leg = Leg("right")
        self.left_foot = Feet(toes=5)
        self.right_foot = Feet(toes=5)
    
    def description(self):
        print(f"Human: {self.name}")
        print(f"Head: {self.head.eyes} eyes, mouth: {self.head.mouth}, nose: {self.head.nose}")
        print(f"Torso: heart: {self.torso.heart}, lungs: {self.torso.lungs}")
        print("Arms:", self.left_arm.side, "and", self.right_arm.side)
        print("Hands with", self.left_hand.fingers, "fingers each")
        print("Legs:", self.left_leg.side, "and", self.right_leg.side)
        print("Feet with", self.left_foot.toes, "toes each")

ana=Human("Ana")
ana.description()


