def get_value(data):
    return data[1]

def order_by_value(data):
    sorted_data = sorted(data.items(), key=get_value)
    print(sorted_data)

print(order_by_value({'p': 8, 'q': 2, 'r': 6}))
# ['q', 'r', 'p']