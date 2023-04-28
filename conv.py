def path_convert():
    while True:
        st = str(input("PATH :\n"))
        print("CONVERTED:\n", "-"*80)
        print(st.replace("\\", "/"), "\n\n")
        if st == "exit":
            quit()


if __name__ == "__main__":
    path_convert()
