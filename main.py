try: # checks if googlesearch is installed in pip
    from googlesearch import search
except ImportError:
    print("import error 'googlesearch'")
    print("Run: pip3 install googlesearch") 

def main():
    # search string
    q = input("What do you want to search up?: ")

    # For the search history file, opens and writes the results
    with open("google_search_history.txt", "w") as google_results:
        for x in search(q, num=20, pause= 2):
            print(x)
            google_results.write(x + "\n")


if __name__ == '__main__':
    main()
