def hanoi_solver(n):
    # Initialize the three rods
    A = list(range(n, 0, -1))
    B = []
    C = []

    # List to store all moves as strings
    moves = [f"{A} {B} {C}"]

    def move(num_disks, source, auxiliary, target):
        if num_disks <= 0:
            return

        # Move n-1 disks from source to auxiliary, so they are out of the way
        move(num_disks - 1, source, target, auxiliary)

        # Move the nth disk from source to target
        target.append(source.pop())

        # Record the move
        moves.append(f"{A} {B} {C}")

        # Move the n-1 disks that we left on auxiliary onto target
        move(num_disks - 1, auxiliary, source, target)

    # Start the recursive process
    move(n, A, B, C)

    return '\n'.join(moves)