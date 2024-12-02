-- Advent of code, trying in haskell. 
-- This is day 3 task
-- Recieve lines of input
-- Split line half and fine common char in both halves
-- Translate char into int 
-- Lowercase item types a through z have priorities 1 through 26.
-- Uppercase item types A through Z have priorities 27 through 52.
-- 
-- DO this for all lines and find the sum

import qualified Data.Map as Map
import System.Environment

charMap :: Map.Map Char Int
charMap = fillCharMap Map.empty ((zip ['a'..'z'] [1..26]) ++ (zip ['A'..'Z'] [27..52]))

main :: IO ()
main = do
  content <- readFile "day3Part2Input.txt"
  putStrLn $ show $ sumLinesPart2 (lines content)

sumLinesPart2 :: [String] -> Int
sumLinesPart2 lns = sum $ map translateChar $ map commonCharThreeString (splitThrees lns)

splitThrees :: [String] -> [[String]]
splitThrees (x:y:z:xs) = [x,y,z] : splitThrees xs
splitThrees _ = []

commonCharThreeString :: [String] -> Char
commonCharThreeString [x,y,z] = commonChar ([c | c<-x, elem c y], z)

sumLines :: [String] -> Int
sumLines lns = do
  let splittedLines = map splitLine lns
  let commonChars = map commonChar splittedLines
  sum (map translateChar commonChars)


splitLine :: String -> (String, String)
splitLine s = do
  let len = fromIntegral $ div (length s) 2
  (take len s, drop len s)

translateChar :: Char -> Int
translateChar c = let Just value = Map.lookup c charMap
  in value


fillCharMap :: Map.Map Char Int -> [(Char, Int)] -> Map.Map Char Int
fillCharMap map [] = map
fillCharMap map ((c,v):xs) = do
  let newMap = Map.insert c v map
  fillCharMap newMap xs

commonChar :: (String, String) -> Char
commonChar ([], []) = 'a'
commonChar ([], (x:xs)) = x
commonChar ((x:xs), []) = x
commonChar ((x:xs), list)
  | elem x list = x
  | otherwise   = commonChar (xs, list)

