# read the book
with open("books/frankenstein.txt") as f:
    file_content = f.read()
    # print(file_content)

    # count no of words
    total_word = len(file_content.split())

    # count characters
    file_content_lowered = file_content.lower()
    char_dict = {}
    for c in file_content_lowered:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    
    # final report
    print("--- Begin report of books/frankenstein.txt ---")
    print(total_word)
    print()
    # convert to list of dictionaries
    named_list = []
    for key,value in char_dict.items():
        data = {
            "char": key,
            "count": value 
        }
        named_list.append(data)

    named_list.sort(reverse=True,key=lambda d: d["count"])

    for item in named_list:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['count']} times")

    print("--- End report ---")