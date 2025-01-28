# #Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each 
# command will be of the  types listed above. Iterate through each command in order and 
# perform the corresponding operation on your list.

if __name__ == '__main__':
    N = int(input()) 
    lst = []  

    for _ in range(N):  
        command = input().split() 
        
      
        if command[0] == 'insert':
            
            i = int(command[1])
            e = int(command[2])
            lst.insert(i, e)
        elif command[0] == 'print':
          
            print(lst)
        elif command[0] == 'remove':
          
            e = int(command[1])
            lst.remove(e)
        elif command[0] == 'append':
          
            e = int(command[1])
            lst.append(e)
        elif command[0] == 'sort':
           
            lst.sort()
        elif command[0] == 'pop':
            
            lst.pop()
        elif command[0] == 'reverse':
            lst.reverse()
