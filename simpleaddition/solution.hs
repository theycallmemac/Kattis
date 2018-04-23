
addNums :: Integer -> Integer -> Integer
addNums x y = x + y

main :: IO()
main = do
  a <- readLn
  b <- readLn
  let result = addNums a b
  print(result)
