#!/usr/bin/env python3

# 0x09. Python generated all mandatory tasks 0 to 28

answers = [
    "type",
    "id",
    "No",
    "Yes",
    "Yes",
    "No",
    "True",
    "True",
    "True",
    "True",
    "True",
    "False",
    "True",
    "True",
    "[1, 2, 3, 4]",
    "[1, 2, 3]",
    "1",
    "[1, 2, 3, 4]",
    "[1, 2, 3]",
    "Yes",
    "Yes",
    "No",
    "Yes",
    "True",
    "False",
    "True",
    "No",
    "Yes",
    ""
    
]

new_answer_files = [
    "0-answer.txt", "1-answer.txt", "2-answer.txt", "3-answer.txt", "4-answer.txt",
    "5-answer.txt", "6-answer.txt", "7-answer.txt", "8-answer.txt", "9-answer.txt",
    "10-answer.txt", "11-answer.txt", "12-answer.txt", "13-answer.txt", "14-answer.txt",
    "15-answer.txt", "16-answer.txt", "17-answer.txt", "18-answer.txt", "20-answer.txt",
    "21-answer.txt", "22-answer.txt", "23-answer.txt", "24-answer.txt", "25-answer.txt",
    "26-answer.txt", "27-answer.txt", "28-answer.txt", "19-copy_list.py"
]

for file_name, answer in zip(new_answer_files, answers):
    with open(file_name, "w") as f:
        if file_name == "19-copy_list.py":
            f.write("#!/usr/bin/env python3\n")
            f.write("def copy_list(list_):\n")
            f.write("    return list_[:]\n")
        else:
            f.write(answer + "\n")
