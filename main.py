
try:
    from googlesearch import search
except ImportError:
    print("import error google search")

def main():
    q = input("What do you want to search up?: ")

    with open("google_search_history.txt", "w") as google_results:
        for x in search(q, num=20, pause= 2):
            print(x)
            google_results.write(x + "\n")
            

if __name__ == '__main__':
    main()
