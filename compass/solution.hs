

shortestDistance :: Integer -> Integer -> Integer
shortestDistance x y = (mod (y - x + 720) 360)


shortestDistanceByMinusOne:: Integer -> Integer -> Integer
shortestDistanceByMinusOne x y =  (-1*(mod (x - y + 720) 360))


absoluteValue :: Integer -> Integer
absoluteValue n
  | n >= 0    = n
  | otherwise = -n


getAnswer :: Integer -> Integer -> Integer
getAnswer x y
  | absoluteValue (x) == 180 = 180
  | absoluteValue (x) < absoluteValue (y) = x
  | otherwise = y


main :: IO()
main = do

    currentDir <- readLn
    correctDir <- readLn
    
    let change1 = shortestDistance currentDir correctDir
    let change2 = shortestDistanceByMinusOne currentDir correctDir

    let answer = getAnswer change1 change2
    print(answer)
