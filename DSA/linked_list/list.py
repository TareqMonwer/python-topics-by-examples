class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        data_list = list()
        node_data = self.head
        while node_data is not None:
            data_list.append(node_data.data)
            node_data = node_data.next
        return str(data_list)

    def append(self, data) -> None:
        ...

    def prepend(self, data) -> None:
        ...
    
    def insert(self, data, new_data):
        ...
    
    def search(self, data):
        ...
    
    def delete(self, data):
        ...

if __name__ == "__main__":
    weekdays_list = LinkedList()
    
    weekdays_list.head = Node("Saturday")
    
    sunday_node = Node("Sunday")
    weekdays_list.head.next = sunday_node

    monday_node = Node("Monday")
    sunday_node.next = monday_node

    tue_node = Node("Tuesday")
    monday_node.next = tue_node

    wed_node = Node("Wednesday")
    tue_node.next = wed_node

    thu_node = Node("Thursday")
    wed_node.next = thu_node

    fri_node = Node("Friday")
    thu_node.next = fri_node

    print(weekdays_list)
