import statistics
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    return 

def get_user_input():
    x = input()
    list = x.split(",") #spliting the inputs into list 
    for i in range (len(list)): #for i in range of length of list eg i=0,1,2,3,4
       list[i]=float(list[i]) 
    return list

def sort_temp(list):
    list.sort()
    return list
    

def calc_average_temperature(list):
    return sum(list)/len(list)

def calc_min_max_temperature(list):
    return min(list),max(list)

def calc_median_temperature(list):
    return statistics.median(list)

def median_calc(list):
   list=sort_temp(list)
   num = len(list)
   if num%2 == 1:
        numi = num//2 
        return list[numi]
   else:
        numi = num/2 
        total = list[numi] + list[numi-1]
        return total/2


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()        
    x = get_user_input()                        #if want to run get_user_input before print must make it variable 
    print(calc_average_temperature(x))  #get_user_input does not need to be called before this as by order of operations get_user_input will run before avg temp
    print(calc_min_max_temperature(x))
    print(sort_temp(x))
    print(calc_median_temperature(x))
    print(median_calc(x))
if __name__ == "__main__":
 main()




