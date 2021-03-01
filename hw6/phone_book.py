def main():
    with open("phone_book.txt") as f_in:
        with open("edited_phone_book.txt", "a") as f_out:
            count = 1
            for line in f_in.readlines():
                name = "".join(char for char in line if char.isalpha()).lower()
                if name.startswith("m") or name.endswith("a"):
                    phone = "".join(char for char in line if char.isdigit())
                    phone = "+380" + phone[-9:]
                    print(f"{count}. {phone} - {name.title()}", file=f_out)
                    count += 1


if __name__ == "__main__":
    main()
