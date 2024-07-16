def swapList(newList):
    size = len(newList)
    
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    
    return newList
    
newList = [12, 35, 9, 56, 24]

print(swapList(newList))

output :-
![Screenshot 2024-07-17 012432](https://github.com/user-attachments/assets/50a30dd9-7369-4aac-b3c3-cf78b9d0a28b)
