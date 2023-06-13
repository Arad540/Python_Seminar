def print_operation_table(operation, num_row = 6, num_columns = 6):
    print(' '.join([str(i) for i in range(1, num_columns+1)]))
    for i in range(2, num_row + 1):
        print (i, end = '\t')
        for j in range (2, num_columns + 1):
            print(operation(i,j), end ='\t')
        print()
        
print_operation_table(lambda x, y: x*y )            