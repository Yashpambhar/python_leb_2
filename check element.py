def check_element_in_list(lst, element):
    if element in lst:
        return True
    else:
        return False

my_list = [1, 2, 3, 4, 5]
element_to_check = 3

if check_element_in_list(my_list, element_to_check):
    print(f"{element_to_check} exists in the list.")
else:
    print(f"{element_to_check} does not exist in the list.")
    
  output :-
![Screenshot 2024-07-17 014121](https://github.com/user-attachments/assets/9d1c9483-178a-427d-acec-c2c90b9ca020)
