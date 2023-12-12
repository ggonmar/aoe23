def read(file, separator):
    elems = []
    if separator == "LINES":
        with open(file) as file_in:
            for line in file_in:
                elems.append(line.strip())
    else:
        with open(file) as file_in:
            elems = file_in.read().split(separator)        
    return elems