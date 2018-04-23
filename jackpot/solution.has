import Control.Monad


getLines :: IO [Integer]
getLines = do
  _ <- getLine
  line <- getLine
  return (getInt line)


getInt :: String -> [Integer]
getInt = map read.words


jackpot :: Integer -> String
jackpot n
  | n <= 1000000000 = show n
  | otherwise = "More than a billion."


count :: [Integer] -> Integer
count = foldr1 lcm


main :: IO ()
main = do
  n <- readLn
  cases <- replicateM n getLines
  putStrLn(unlines(map (jackpot.count) cases))

