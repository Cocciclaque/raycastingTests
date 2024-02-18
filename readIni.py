def read(file):
    with open(file, "r") as f:
        
        lines = f.readlines()
        return_dict = {}

        for line in lines:
            line = line.rstrip().split("=")
            return_dict[line[0]]=line[1]

    return return_dict