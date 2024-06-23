def swap_name(name):
    name_list = name.split(" ")
    return name_list[-1] + ", " + " ".join(name_list[:-1])

print(swap_name('Karl Oskar Henriksson Ragvals'))    # "Roberts, Joe"