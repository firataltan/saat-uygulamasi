# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/24

saat=int(input("saati giriniz:"))
dakika=int(input("dakikayı giriniz:"))
ekleme=int(input("eklenecek dakikayı giriniz:"))
saat=(saat%24)
dakika=(dakika%60)
yeni_saat=(saat+ekleme//60)%24
yeni_dakika=(dakika+ekleme%60)%60 and dakika+ekleme


print(f"{(saat+ekleme//60)%24}:{(dakika+ekleme%60)%60}")

