#Time : O(N)
# Space : O(N)
# Linkedlist
# https://practice.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1/#
def removeDuplicates(self, head):
        # code here
        # return head after editing list
        s = set()
        cur = head
        s.add(cur.data)
        while(cur.next!=None):
            if cur.next.data in s:
                cur.next = cur.next.next
            else:
                s.add(cur.next.data)
                cur = cur.next
        return head
