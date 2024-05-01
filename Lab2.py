import statistics

def display_main_menu():
    print("display_main_menu")
    
def get_user_input():
    print("\nEnter temperatures separated by commas (e.g. 5, 67, 32)")
    x = input()
    num_list = x.split(", ")
    print (num_list)
    num_list = [float(x) for x in num_list]
    return num_list

def calc_average(num_list):
    print ("\nFinding average temperature")
    average = sum(num_list)/float(len(num_list))
    print ("Average temperature is " + str(average))
    return average

def find_min_max(num_list): 
    print ("\nFinding minimum and maximum temperature")
    max_temp = min_temp = num_list[0]
    for x in num_list: 
        if x < min_temp:
            min_temp = x
        elif x > max_temp:
            max_temp = x
    print ("The minimum temperature is " + str(min_temp), "and the maximum temperature is " + str(max_temp))
    return (min_temp, max_temp)

def sort_temperature (num_list):
    print ("\nSorting temperatures in ascending order")
    Sorted = sorted(num_list)
    print ("The temperature in ascending order is " + str(Sorted))
    return Sorted

def calc_median_temperature(num_list):
    print ("\nCalcuating median temperature")
    Median = statistics.median(num_list)
    print ("Median value is " + str(Median))
    return Median

def main():
    print ("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    numlist = get_user_input()
    average = calc_average(numlist)
    min_max = find_min_max(numlist)
    Sorted = sort_temperature (numlist)
    Median = calc_median_temperature(numlist)

if __name__=="__main__":
    main()