
main = do
  contents <- readFile "day2Input.txt"
  putStrLn $ show $ calculateResultSum $ createChoices (lines contents)

calculateResultSum :: [String] -> Int
calculateResultSum []     = 0
calculateResultSum (x:xs) = let [p1,p2] = words x
  in (roundScore p1 p2) + (calculateResultSum xs)

shapeScore :: String -> Int
shapeScore "X" = 1
shapeScore "Y" = 2
shapeScore "Z" = 3

roundScore :: String -> String -> Int
roundScore "A" "Y" = 8
roundScore "B" "Z" = 9
roundScore "C" "X" = 7
roundScore "A" "X" = 4
roundScore "B" "Y" = 5
roundScore "C" "Z" = 6
roundScore _ c     = shapeScore c

createChoices :: [String] -> [String]
createChoices []      = []
createChoices (x:xs)  = do
  let [p1, choice] = words x
  case choice of
    "X" -> (p1 ++ " " ++ (losingChoice p1)) : createChoices xs
    "Y" -> (p1 ++ " " ++ (drawingChoice p1)) : createChoices xs
    "Z" -> (p1 ++ " " ++ (winningChoice p1)) : createChoices xs

winningChoice :: String -> String
winningChoice "A" = "Y"
winningChoice "B" = "Z"
winningChoice "C" = "X"

drawingChoice :: String -> String
drawingChoice "A" = "X"
drawingChoice "B" = "Y"
drawingChoice "C" = "Z"

losingChoice :: String -> String
losingChoice  "A" = "Z"
losingChoice  "B" = "X"
losingChoice  "C" = "Y"

