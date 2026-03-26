def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    moves = []

    def state():
        return ' '.join(str(rod) for rod in rods)

    def move(disk_count, source, target, auxiliary):
        if disk_count == 0:
            return
        move(disk_count - 1, source, auxiliary, target)
        disk = rods[source].pop()
        rods[target].append(disk)
        moves.append(state())
        move(disk_count - 1, auxiliary, target, source)

    moves.append(state())
    move(n, 0, 2, 1)

    return '\n'.join(moves)