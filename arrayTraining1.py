class Main:
    def __init__(self):
        pass

    def run(self):
        pass
        # Add your code here

    def reverse_array(self, arr):
        return arr[::-1]
    
    def filter_even_numbers(self, arr):
        return [num for num in arr if num % 2 == 0]
    
#array practice 
if __name__ == "__main__":
    main = Main()
    main.run()
    my_array = [1, 2, 3, 4, 5]
    even_numbers = main.filter_even_numbers(my_array)
    print(even_numbers)
    reversed_array = main.reverse_array(my_array)
    print(reversed_array)
    