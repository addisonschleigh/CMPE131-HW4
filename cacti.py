def cacti_number(plot):
    if not plot or not all(isinstance(row, list) and len(row) == len(plot[0]) for row in plot):
        return 0  # Handle bad input

    rows = len(plot)
    columns = len(plot[0])
    count = 0

    for i in range(rows):
        for j in range(columns):
            if plot[i][j] == 0:
                can_place = True
                #check up
                if i > 0 and plot[i-1][j] == 1:
                    can_place = False
                #check down
                if i < rows-1 and plot[i+1][j] == 1:
                    can_place = False
                #check left
                if j > 0 and plot[i][j-1] == 1:
                    can_place = False
                #check right
                if j < columns -1 and plot[i][j+1] == 1:
                    can_place = False
                if can_place:
                    plot[i][j] = 1
                    count+= 1
    return count