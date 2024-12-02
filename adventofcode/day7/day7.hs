
main = do
    content <- readFile("day7TestInput.txt")
    putStrLn $ show $ sumUp $ lines content

sumUp :: [String] -> Int
sumUp [] = 0
sumUp (('$':' ':'c':'d':' ':'.':rest):lines) = sumUp lines
sumUp (('$':' ':'c':'d':' ':dir):lines) = let size = commandos lines
  in if size > 100000 then 0 + sumUp lines else size + sumUp lines
sumUp (_:lines) = sumUp lines

commandos :: [String] -> Int
commandos [] = 0
commandos (('$':' ':'c':'d':' ':'.':'.':_):lines) = 0
commandos (('$':' ':'l':'s':_):lines) = commandos lines
commandos (('$':' ':'c':'d':' ':dir):lines) = commandos lines
commandos (('d':'i':rest):lines) = commandos lines
commandos (line:lines) = let (num:_) = words line 
  in read num + commandos lines

