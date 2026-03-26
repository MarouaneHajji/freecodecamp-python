def hanoi_solver(n):
    # Initialize the three rods as lists.
    # Rod 0 (source) starts with all disks in descending order:
    #   e.g. for n=3 -> [3, 2, 1] (largest disk at index 0, smallest at index -1 / top)
    # Rod 1 (auxiliary) and Rod 2 (target) start empty.
    rods = [list(range(n, 0, -1)), [], []]

    # This list will accumulate every snapshot of the board state as a string,
    # starting with the initial arrangement and including one entry after each move.
    moves = []

    def state():
        # Build a human-readable snapshot of all three rods, each formatted as a
        # Python list literal (e.g. "[3, 2]"), joined by a single space.
        # str(rod) on a Python list already produces the "[a, b, c]" format we need.
        return ' '.join(str(rod) for rod in rods)

    def move(disk_count, source, target, auxiliary):
        # Base case: nothing to move if there are 0 disks.
        if disk_count == 0:
            return

        # Step 1 – Recursively move the top (disk_count - 1) disks from
        # 'source' to 'auxiliary', using 'target' as the temporary buffer.
        # This clears the way for the largest disk currently on 'source'.
        move(disk_count - 1, source, auxiliary, target)

        # Step 2 – Move the single largest disk (now exposed on top of 'source')
        # directly to 'target'.
        # pop() removes and returns the last element of the list, which represents
        # the top-most disk on the rod.
        disk = rods[source].pop()

        # append() places that disk on top of the target rod.
        rods[target].append(disk)

        # Record the board state immediately after this move.
        moves.append(state())

        # Step 3 – Recursively move the (disk_count - 1) disks that were parked on
        # 'auxiliary' to 'target', using 'source' (now empty of the large disk) as
        # the temporary buffer.
        move(disk_count - 1, auxiliary, target, source)

    # Capture the initial arrangement before any moves are made.
    moves.append(state())

    # Kick off the recursion: move all n disks from rod 0 (source)
    # to rod 2 (target), using rod 1 (auxiliary) as the buffer.
    move(n, 0, 2, 1)

    # Join every recorded state with a newline and return the full solution string.
    return '\n'.join(moves)