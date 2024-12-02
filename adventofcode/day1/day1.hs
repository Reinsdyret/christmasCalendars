
main :: IO ()
main = do
  content <- readFile "day1Input.txt"
  putStrLn $ show $ maximum $ getCalorieSums (lines content)

getCalorieSums :: [String] -> [Int]
getCalorieSums [] = []
getCalorieSums lns = let values = takeWhile (/="") lns
  in (sum $ map read values) : getCalorieSums (drop (fromIntegral (1 + (length values))) lns)


quicksort1 :: (Ord a) => [a] -> [a]
quicksort1 [] = []
quicksort1 (x:xs) =
  let smallerSorted = quicksort1 [a | a <- xs, a <= x]
      biggerSorted = quicksort1 [a | a <- xs, a > x]
  in  biggerSorted ++ [x] ++ smallerSorted

