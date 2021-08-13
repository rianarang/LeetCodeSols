
// Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        //empty list
        if (head == nullptr)
            return head;
        //list with one element
        if (head->next == nullptr)
            return head;
        ListNode *temp = head->next;
        //list with 2+ and 2
        if (temp->next != nullptr)
        {
            //list longer than 2
            ListNode *temp2 = temp->next;
            head->next = nullptr;
            temp->next = head;
            head = temp;
            while (temp2->next != nullptr)
            {
                temp = temp2;
                temp2 = temp->next;
                temp->next = head;
                head = temp;
            }
            temp2->next = head;
            head = temp2;
        }
        else
        {
            //list of length 2
            head->next = nullptr;
            temp->next = head;
            head = temp;
        }
        return head;
    }
};