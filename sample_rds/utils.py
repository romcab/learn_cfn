def write_to_file(filename:str, data:str):
    with open(filename, 'w') as out:
        out.write(data)