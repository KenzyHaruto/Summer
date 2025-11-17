import os
import time
import tkinter as tk

a = [
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "a", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "a", "a", "a", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", "a", "a", "a", "a", "a", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", "a", "a", "a", "a", "a", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", "a", "a", "a", "a", "a", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", "a", "a", "a", "a", "a", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", "a", "a", "a", "a", "a", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"]]
for b in range(10):
    for c in range(26):
        print(a[b][c], end=" ")
    print()

def kntl(event):
    if a[len(a) - 1][1] != "a":
        for b in range(10):
            for c in range(26):
                if a[b][c] == "a":
                    a[b][c-1] = "a"
                    a[b][c] = " "
        os.system("cls")
        for b in range(10):
            for c in range(26):
                print(a[b][c], end=" ")
            print()

def kntl2(event):
    if a[len(a)-1][24] != "a":
        for b in range(len(a)):
            cek = ""
            for c in range(len(a[b])):
                if (a[b][c] == "a" or cek == "a") and c < len(a[b]) - 1:
                    if cek == "":
                        cek = "a"
                        a[b][c] = " "
                    elif cek == "a" and a[b][c] == " ":
                        cek = ""
                        a[b][c] = "a"
                    elif cek == "a" and a[b][c] == "a":
                        cek = "a"
                        a[b][c] = "a"
        os.system("cls")
        for b in range(len(a)):
            for c in range(len(a[b])):
                print(a[b][c], end=" ")
            print()

root = tk.Tk()
root.withdraw()
root.bind("<a>", kntl)  # huruf kecil a
root.bind("<b>", kntl2)  # huruf besar A jika pakai Shift
root.mainloop()