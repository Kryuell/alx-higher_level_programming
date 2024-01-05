for i in range(0, 29):
    file_name = f"{i}-answer.txt"
    with open(file_name, 'w') as file:
        file.write(" \n".format(i))
    print(f"Created {file_name}")
