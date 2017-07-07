main :: IO()
main = do
  n <- readLn
  print((sum [1 | x <- [0..n], 2^x < n]) + 1)
