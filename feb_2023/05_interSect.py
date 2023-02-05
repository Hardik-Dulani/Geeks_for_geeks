# Given two singly linked lists of size N and M, write a program to get the point where two linked lists intersect each other.

def intersetPoint(self,head1,head2):
        a = head1
        b = head2 
        no_intersection = 0
        while a!=b and no_intersection!=2:
            if a.next == None:
                no_intersection+=1
                a = head2
            if b.next == None:
                b = head1
            a = a.next
            b = b.next
            # print(a.data,b.data)
        if no_intersection == 2:return -1
        return a.data
