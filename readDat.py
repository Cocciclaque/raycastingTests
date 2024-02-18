def read(file):

    with open(file, "r") as f:
        lines = f.readlines()
        return_results = []
        return_results.append(lines[0].rstrip().split(","))
        map=[]
        for line in lines[1:]:
            map.append(line.rstrip().split(','))

        return_results.append(map)

    return return_results


print(read("levels\laby-01.dat"))