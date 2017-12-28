def print_status(file, tekst):
    with open(file, "a") as my_file:
        my_file.write(tekst)