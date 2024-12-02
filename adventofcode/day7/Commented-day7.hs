
-- main function which reads the file and prints out the sum of the values
main = do
    content <- readFile("day7TestInput.txt")  -- read the file
    putStrLn $ show $ sumUp $ lines content  -- print the sum of the values

-- function to calculate the sum of the values
sumUp :: [String] -> Int
sumUp [] = 0  -- base case
sumUp (('$':' ':'c':'d':' ':'.':rest):lines) = sumUp lines  -- ignore the commands starting with '$ cd .'
sumUp (('$':' ':'c':'d':' ':dir):lines) = let size = commandos lines  -- get the size of the commandos
  in if size > 100000 then 0 + sumUp lines else size + sumUp lines  -- if size is greater than 100000, ignore it
sumUp (_:lines) = sumUp lines  -- ignore other lines

-- function to calculate the size of the commandos
commandos :: [String] -> Int
commandos [] = 0  -- base case
commandos (('$':' ':'c':'d':' ':'.':'.':_):lines) = 0  -- ignore the commands starting with '$ cd ..'
commandos (('$':' ':'l':'s':_):lines) = commandos lines  -- ignore the commands starting with '$ ls'
commandos (('$':' ':'c':'d':' ':dir):lines) = commandos lines  -- ignore the commands starting with '$ cd'
commandos (('d':'i':rest):lines) = commandos lines  -- ignore the commands starting with 'di'
commandos (line:lines) = let (num:_) = words line  -- get the size from the line
  in read num + commandos lines  -- add the size to the total size
