def tree_count_fn(move_x,move_y):
    map_of_trajectory = []
    x, y = 0, 0
    tree_count = 0
    with open('data_day3.txt') as my_file:
        map_of_trajectory = [
            line
            for line in my_file.read().splitlines()
        ]
    print(map_of_trajectory)
    # python 2-D array as a list counts rows and then column. Translates to y and x ;-)
    x_length = len(map_of_trajectory[0])
    y_length = len(map_of_trajectory)
    print(x_length, y_length)
    while y < y_length:
        if (map_of_trajectory[y][x % x_length] == '#'):
            tree_count += 1
            print(map_of_trajectory[y][x % x_length])
            print(x%x_length,y)
        x = x + move_x
        y = y + move_y
    print(tree_count)
    return(tree_count)

print(tree_count_fn(3,1))
tree_product = 1
tree_productold = 1
x_count = 1,3,5,7,1
y_count = 1,1,1,1,2
print(len(x_count))
for i in range(len(x_count)) :
    tree_product = tree_count_fn(x_count[i],y_count[i])
    tree_product = tree_productold*tree_product
    tree_productold = tree_product
print(tree_product)