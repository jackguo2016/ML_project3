# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    pxy1 = normpdf(xTe, 0, 1)
    pxxy1 = pxy1[:, 0] * pxy1[:, 1]
    pxy2 = normpdf(xTe, OFFSET, 1)
    pxxy2 = pxy2[:, 0] * pxy2[:, 1]

    pxx = pxxy1 * 0.5 + pxxy2 * 0.5

    py1xx = pxxy1 * 0.5 / pxx
    py2xx = pxxy2 * 0.5 / pxx

    ybar = py1xx + 2 * py2xx

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
