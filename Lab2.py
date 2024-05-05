import math

def display_main_menu(): 	      
    print("Enter some numbers separated by commas (e.g. 5, 67, 32): ") 
          
def calc_average_temperature(y): #Float  
    temp=sum(y)/len(y)
    return temp



def get_user_input(): #List of Floats 
    x = input()
    num_list=x.split(",")
    num_list=[float(x) for x in num_list]
    return num_list

def find_min_max_temperature(y): #List of Floats in the format [min_temp, max_temp] 
    min_temp = float('inf')
    for num1 in y:
        if (num1 < min_temp):
            min_temp = int(num1)
    max_temp = float('-inf')
    for num2 in y:
        if (num2 > max_temp):
            max_temp = int(num2)
    print("Min Temperature is:", min_temp, "Max Temperature is:", max_temp)
    test_result=[min_temp,max_temp]
    return test_result
    
SORT_ASCENDING = 0
def sort_temperature(arr,sorting_order): #List of Floats sorted in ascending order 
    
    # Copy input list to results list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)
    
        # Traverse through all array elements
    for i in range(n - 1):
            # range(n) also work but outer loop will
            # repeat one time more than needed.

            # Last i elements are already in place
        for j in range(0, n - i - 1):
                
            if arr_result[j] > arr_result[j + 1]:
                arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

    return arr_result



def calc_median_temperature(z): #Float 
    median=(len(z)-1)/2
    if isinstance(median,int):
        print("The median temperature is: ",z[median])
        
    else:
        med_avg=(z[median]+z[median+1])/2
        print("The median temperature is: ",med_avg)
        
    
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    y=get_user_input()
    print("List is:", y)
    print("Average is:", calc_average_temperature(y))
    find_min_max_temperature(y)
    z=sort_temperature(y,0)
    calc_median_temperature(z)

if __name__ == "__main__":
    main()





