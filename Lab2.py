
def display_main_menu(): 	      
    print("Enter some numbers separated by commas (e.g. 5, 67, 32): ") 
          
def calc_average_temperature(): #Float  
    temp=sum(y)/len(y)
    return temp



def get_user_input(): #List of Floats 
    x = input()
    num_list=x.split(",")
    num_list=[float(x) for x in num_list]
    return num_list

def find_min_max_temperature(): #List of Floats in the format [min_temp, max_temp] 
    min_temp = float('inf')
    for num1 in y:
        if (num1 < min_temp):
            min_temp = int(num1)
    max_temp = float('-inf')
    for num2 in y:
        if (num2 > max_temp):
            max_temp = int(num2)
    print("Min Temperature is:", min_temp, "Max Temperature is:", max_temp)
    

def sort_temperature(): #List of Floats sorted in ascending order 
    print(sort_temperature)

def calc_median_temperature(): #Float 
    print(calc_median_temperature)

print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
display_main_menu()
y=get_user_input()
print("List is:", y)
calc_average_temperature()
print("Average is:", calc_average_temperature())
find_min_max_temperature()




