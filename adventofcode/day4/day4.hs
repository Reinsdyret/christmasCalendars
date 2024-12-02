main = do
  content <- readFile "day4Input.txt"
  let tupleRanges = parseInput (lines content)
  putStrLn $ show $ countOverlaps tupleRanges

countOverlaps :: [(Int,Int,Int,Int)] -> Int
countOverlaps [] = 0
countOverlaps ((x,y,x1,y1):rest) = (overlap x y x1 y1) + countOverlaps rest

overlap :: Int -> Int -> Int -> Int -> Int
overlap x y x1 y1
  | x >= x1 && y <= y1 = 1
  | x <= x1 && y >= y1 = 1
  | otherwise = 0


parseInput :: [String] -> [(Int,Int,Int,Int)]
parseInput ("":_) = []
parseInput ((x:'-':y:',':x1:'-':y1):rest) = (read x, read y,read x1,read y1) : parseInput rest
