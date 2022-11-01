import pywhatkit
import sys
class Node(object):
    # Singly linked node
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class doubly_linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append_item(self, value):
        # Append an item 
        new_item = Node(value, None, None)
        if self.head is None:
            self.head = new_item
            self.tail = self.head
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item
        self.count += 1
    
    def iter(self):
        # Iterate the list
        current = self.head
        while current:
            item_val = current.value
            current = current.next
            yield item_val

    def print_foward(self):
        for node in self.iter():
            print(node)   
    
    def add_to_list(self):
        fileadd = open("musiclist.txt","w")
        for node in self.iter():
            fileadd.write(node) 
            fileadd.write("\n") 
        fileadd.close()
    
    def displist(self):
        a_file = open("musiclist.txt","r")
        lines = a_file.readlines()
        for line in lines:
            print(line)
        a_file.close()
             
    def delete(self, value):
        # Delete a specific item
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False

        elif current.value == value:
            self.head = current.next
            self.head.prev = None
            node_deleted = True

        elif self.tail.value == value:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True

        else:
            while current:
                if current.value == value:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next

        if node_deleted:
            self.count -= 1
            

          
items = doubly_linked_list()


print("********Available Songs********")
items.append_item(' ChillBro')
items.append_item(' Valayapati')
items.append_item(' High On Love')
items.append_item(' Freak Penne')
items.append_item(' Yenti Yenti')
items.append_item(' Munbe Vaa')
items.append_item(' NewYork Nagaram')
items.append_item(' Idhu Varai Iladha ')
items.append_item(' Pogathe')
items.append_item(' Nenjukul Peidhidum')
items.append_item(' Venmegam (From YNM)')
items.append_item(' Po Nee Po')
items.append_item(' Yennai Maatrum Kaadhale')
items.append_item(' Vaseegara')
items.append_item(' Thalli Pogathey')
items.append_item(' Enna Solla Pogirai')
items.append_item(' Pookal Pookum Tharunam')
items.displist()
print("********End of List********")

def main():
     
    print("\n1. ADD SONG\n")
    print("2. DELETE SONG\n")
    print("3. DISPLAY SONG\n")
    print("4. PLAY SONG\n")
    print("5. EXIT")
    ch = int(input("Enter Your Choice: "))
    if ch == 1:
            Data = input ("Enter Song Name:")
            items.append_item(Data)
            musicc = open("musiclist.txt","a")
            musicc.write("\n")
            musicc.write(Data)
            musicc.close()
            items.displist()
            
            
    elif ch == 2:
            Bata = input ("Enter Song Name to be deleted: ")
            items.delete(Bata)  
            print("\n Updated PlayList\n ")
            items.print_foward()
    
    elif ch == 3:
            print("Availabe Playlist")
            items.displist()
    
    elif ch == 4:
        music = input("Enter Song name: ")
        pywhatkit.playonyt(music)

    elif ch == 5:
            print("Catch you Soon!!")
            sys.exit()
    else:
            print("Enter Correct Details")

while True:
    main()
