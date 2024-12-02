
multiList = Int | [] | [multiList]

main = do 
  content <- readFile "day13Input.txt"
  let inputList = formatInputToList $ lines content


indexSummer :: [Bool] -> Int -> Int
indexSummer (x:xs) index = if x then index + (indexSummer xs (index -1) else indexSummer xs (index - 1)


formatInputToList :: [String] -> [(multiList,multiList)]
formatInputToList [] = []
formatInputToList (x:y:_:xs) = (read x, read y) : formatInputToList xs

compare :: multiList -> multiList -> Bool
compare [] [] = true
compare (Int a) (Int b) = a <= b
compare [] [(multiList b):rest] = true
compare [(multiList b):rest] [] = false
compare [(multiList m):rest] [(multiList m2):rest2] = compare m m2 && compare rest rest2

