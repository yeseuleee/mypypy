class Node():
    def __init__(self, cur_node_data = None, next_node = None):
        self.node = [str(cur_node_data), str(next_node)]


class Linkedlist():
    def add_node(self, node_data, cur_list):
        if len(cur_list) == 1:
            cur_list[0][-1] = node_data

        cur_list[-1][-1] = node_data
        new_node  = Node().node
        cur_list.append(new_node)
        cur_list[-1][0] = node_data
        return cur_list

    def del_node(self, cur_list):
        del(cur_list[-1])
        cur_list[-1][-1] = None
        return cur_list


class Stack():
    def __init__(self):
        self.stack = []


    def push(self,node_data):
        if len(self.stack) == 0:
            self.stack.append(Node().node)

        if len(self.stack) >600000:
            print('스택이 꽉 찼습니다.')
        else:
            return Linkedlist().add_node(node_data,self.stack)


    def pop(self):
        if len(self.stack)== 0:
            print('스택이 비어있습니다.')
        else:
            return Linkedlist().del_node(self.stack)
            # return self.stack[-1][0]

# class Linkedlist(Node):
    # def change_node():
    # def delete_all():
    # def search_node():
    # def search_del_node():
    # def search_add_node():


    # def isStackFull(self):
    #     if len(Stack().stack)>600000:
    #     # if Stack().stack[0] == None & Stack().stack.index(Stack().stack[-1]) >600000:
    #         return 1    #모르겠...
    #     else:
    #         return 0
    #
    # def isStackEmpty(self):
    #     print(Stack(),'Stack()')
    #     print(Stack().stack,'Stack().stack')
    #     print(self.stack,'self.stack')
    #     if Stack().stack == None:
    #         print(len(self.stack),'a')
    #         return True
    #     else:
    #         print(len(self.stack),'b')
    #         return False       ->isStackEmpty랑 isStackFull짜는 법... ㅜㅜ stack그대로 받아오는법.....
