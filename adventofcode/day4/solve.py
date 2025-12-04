class ToiletPaper:
    removed = False

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []

    def numberOfNeighbors(self):
        count = 0
        for neigh in self.neighbors:
            if not neigh.removed:
                count += 1
        return count

    def remove(self):
        self.removed = True


papers = []
papersMap = {}

with open("input.txt", 'r') as f:
    grid = []
    for line in f.readlines():
        grid.append(line.strip())


    for y, row in enumerate(grid):
        for x in range(len(row)):
            if grid[y][x] == ".":
                continue
            toiletPaper = ToiletPaper(x, y)
            papers.append(toiletPaper)
            papersMap[(x,y)] = toiletPaper
            

neighbors_offsets = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0)          , (1, 0),
        (-1, 1) , (0, 1) , (1, 1)
]

rows = len(grid)
cols = len(grid[0])

# Build graph
for paper in papers:
    x = paper.x
    y = paper.y
    for dx, dy in neighbors_offsets:
        nx, ny = x + dx, y + dy

        if 0 <= nx < cols and 0 <= ny < rows:
            if grid[ny][nx] == ".": continue

            neighbor = papersMap[(nx, ny)]
            paper.neighbors.append(neighbor)

# calculate part 1
partOneResult = 0
for paper in papers:
    if paper.numberOfNeighbors() < 4:
        partOneResult += 1
print(f"Part 1: {partOneResult}")

# Part 2

def recursiveRemoveToiletPapers(papers):
    removedAny = False
    for paper in papers:
        if paper.removed: continue
        if paper.numberOfNeighbors() < 4:
            removedAny = True
            paper.remove()
    
    if removedAny:
        recursiveRemoveToiletPapers(papers)

recursiveRemoveToiletPapers(papers)

partTwoResult = 0
for paper in papers:
    if paper.removed:
        partTwoResult += 1

print(f"Part 2: {partTwoResult}")
