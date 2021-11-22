
try:
    from googlesearch import search
except ImportError:
    print("import error google search")

def main():
    q = input("What do you want to search up?: ")

    for x in search(q, num=20, pause= 2):
        print(x)




if __name__ == '__main__':
    main()
