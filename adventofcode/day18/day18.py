
# Get lines from input
lines = []

with open("day18Input.txt", 'r') as f:
    lines = f.readlines()


# Make 3D list, a 0 will represent empty and 1 is block
N = 100        # Limit for coords
grid = [[[0 for col in range(N)]
        for col in range(N)]
        for row in range(N)]

# Fill grid
for line in lines:
    x, y, z = [int(a) for a in line.split(",")]
    grid[x][y][z] = 1


# Calculate surface area by checking for neighbours
surface_area = 0
for x in range(N):
    for y in range(N):
        for z in range(N):
            edges = 6
            block = grid[x][y][z]
            if (block == 0):
                continue
            print(f"{x=}, {y=}, {z=}")
            blockAbove = grid[x][y+1][z] if (y < (N-1)) else 0
            blockUnder = grid[x][y-1][z] if (y > 0) else 0

            blockLeft = grid[x-1][y][z] if (x > 0) else 0
            blockRight = grid[x+1][y][z] if (x < (N-1)) else 0

            blockFront = grid[x][y][z-1] if (z > 0) else 0
            blockBehind = grid[x][y][z+1] if (z < (N-1)) else 0

            blockSurface = edges - (blockAbove + blockUnder + blockLeft +
                                    blockRight + blockFront + blockBehind)

            surface_area += blockSurface
            print(f"{blockSurface = }\n")

print(f"{surface_area = }")
