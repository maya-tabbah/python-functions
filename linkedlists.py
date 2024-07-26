#write a method attack() that takes in a Pokemon object opponent and decreases opponent's hp by their self's damage amount.
#If damaging the opponent leads to the opponent having an hp of 0 or less, the function should set the opponent's hp to 0 and print out "<Opponent name> fainted>.
#Otherwise, the function should print out "<Pokemon name> dealt <damage> damage to <opponent name>".

class Pokemon():
   def  __init__(self, name, hp, damage):
     self.name = name
     self.hp = hp # hit points
     self.damage = damage # The amount of damage this pokemon does to its opponent every attack

   def attack(self, opponent):
     if opponent.hp <= 0:
       print(f"{opponent.name} fainted")
     else:
       opponent.hp -= self.damage
       print(f"{self.name} dealt {self.hp} damage to {opponent.name}")

pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 
opponent = bulbasaur
pikachu.attack(opponent)


#create two nodes:
#The first node should have value a and be stored in a variable node_one.
#The second node should have value b and be stored in a variable node_two.

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
node_one = Node("a")
node_two = Node("b")

#now we will link the nodes together
node_one.next = node_two
print(node_one.value) 
print(node_one.next.value) 
print(node_two.value)
print(node_two.next) 

#Create the list ["Mario", "Luigi", "Wario", "Toad"] as a linked list given the Node class:
lst = ["Mario", "Luigi", "Wario", "Toad"]
node_1= Node(lst[0])
node_2= Node(lst[1])
node_3= Node(lst[2])
node_4= Node(lst[3])

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)

#Write a function print_linked_list() that takes in a head node as a parameter and prints the linked list using the string " -> " to separate each node.
def print_linked_list(head):
   current = head
   while current:
     if current.next is None:
       print(f"{current.value}")
     else:
       print(f"{current.value} -> " ,end ="")
     current = current.next
print_linked_list(node_1)

#Using the provided Node class below, create the normal Python list ["Jigglypuff", "Wigglytuff"] as a linked list.
pokemon = ["Jigglypuff", "Wigglytuff"]
node_1 = Node(pokemon[0])
node_2 = Node(pokemon[1])

node_1.next = node_2

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)

