def main():
    print("Welcome to the email slicer ")
    print("")

    email_input = input("input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)


main()