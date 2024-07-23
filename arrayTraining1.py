class Main:
    def __init__(self):
        pass

    def run(self):
        pass
        # Add your code here

    def reverse_array(self, arr):
        return arr[::-1]

if __name__ == "__main__":
    main = Main()
    main.run()
    my_array = [1, 2, 3, 4, 5]
    reversed_array = main.reverse_array(my_array)
    print(reversed_array)