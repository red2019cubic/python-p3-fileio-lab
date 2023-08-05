def write_file(file_name, file_content):
    text_file = open(f"{file_name}.txt", mode='w', encoding='utf-8')
    text_file.write(file_content)
    return text_file

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode='a', encoding='utf-8') as text_file:
        text_file.write(f"{append_content}")
    return text_file

def read_file(file_name="lib/test_file"):
    with open(f"{file_name}.txt", encoding='utf-8') as text_file:
        return text_file.read()
    
