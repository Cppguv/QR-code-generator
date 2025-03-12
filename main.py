# Здесь видео по созданию QR-кодов
# https://realpython.com/lessons/generating-qr-codes/

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import segno


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'\033[1;32;40mHi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_hi('PyCharm')

    qrcode = segno.make_qr("Hello, world!")
    # qrcode.save("basic_qrcode.png")
    qrcode.save(
            "basic_qrcode.png",
                 scale = 5,
                 border = 5,
                 )
