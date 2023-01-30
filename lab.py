# strings

str1="VishnuA Parvatikar"
print




import pandas as pd


class Node(object):
    def __init__(self, x) -> None:
        self.data = x


class LinkedList(object):
    def __init__(self):
        self.hnode = None


List1 = LinkedList()
n1 = Node(1)
n2 = Node(5)
List1.hnode = n1
ptr = List1.hnode
ptr.next = n2
# print(List1.hnode.data, List1.hnode.next.data)

d = {"name": ["ram", "sam"], "rno": [1, 2]}

df1 = pd.DataFrame(d)
# print(df1)

# execute left join , inner join , right join , outer join for 2 dataframes
