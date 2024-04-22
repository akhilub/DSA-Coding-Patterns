class Solution(self,s):
    seen_letter = []
    for ch in s:
        if ch in seen_letter:
            return ch
        else:
            seen_letter.append(ch)


#Follow Up Question

#Q) Should you use a hashset 
#A) No because it does not matter since we have a constraint that we have only lowercase letter so our look up would be
#O(26) =O(1)

#Q) does it make a difference if we use a dictionary vs a set or a list?
# https://stackoverflow.com/questions/3489071/in-python-when-to-use-a-dictionary-list-or-set