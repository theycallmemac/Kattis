import Control.Monad

simonSays :: [String] -> [String]
simonSays = filter (\s -> head (words s) == "Simon" && words s !! 1 == "says")

main :: IO ()
main = do

  n <- getLine
  line <- replicateM (read n) getLine
  mapM_ (putStrLn.unwords.drop 2.words) (simonSays line)
