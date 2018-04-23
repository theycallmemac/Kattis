main :: IO()
main = do
  n <- readLn
  print(div (n*(n-1)*(n-2)*(n-3)) 24)
