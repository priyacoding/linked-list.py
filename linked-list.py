class node:
  def __init__(self,data):
    self.data=data
    self.next=None
class link_list:
   def remove(self,data):
    if self.head.data==data:
      self.head=self.head.next
    else :
       temp=self.head
       while temp  is not None:
         if temp.data ==data:
            break
         prenode=temp
         temp=temp.next
       if temp:
         prenode.next=temp.next
       else:
         print(" no such data")
   def inserthead(self,newdata):
    tempnode=node(newdata)
    tempnode.next=self.head
    self.head=tempnode
   def insertmid(self,middle,newdata):
     tempnode=node(newdata)
     tempnode.next=middle.next
     middle.next=tempnode
   def insertlast(self,newdata):
      newnode=node(newdata)
      temp=self.head
      while temp.next is not None:
        temp=temp.next
      temp.next=newnode

   def __init__(self):
    self.head=None
   def show(self):
     temp=self.head
     while temp is not None:
       print(temp.data)
       temp=temp.next



n1=link_list()
n1.head=node("abisha")
n2=node("basith")
n3=node("sri")
n4=node("pradeep")
n5=node("pandi")

n1.head.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n1.show()
print("------(before insert)------")
n1.insertmid(n3,"sabari")
n1.show()
print("--------(before insertfront)------")
n1.inserthead("sofia")
n1.show()
print("------(before insert end)-----")
n1.insertlast("dinesh")
n1.show()
print("-----(before remove)----")
n1.remove("sri")
n1.show()
print("---------------")
n1.remove("sofia")
n1.show()
print("-------------------")
n1.remove("sandeep")
n1.show()
