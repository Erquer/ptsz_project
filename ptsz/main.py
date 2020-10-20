# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def genetareTestFile(size):
    file = open("testFiles/126828_{0}.in".format(size), "w")
    file.write('0\n')
    for i in range(size):
        file.write('{0} '.format(i))
    file.close()
    print("Test file generated!")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(50, 501, 50):
        genetareTestFile(i)



