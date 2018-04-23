module Main where

getRetirementAge :: [Int] -> Int
getRetirementAge [b,br,bs,a,as] = ((bs * (br - b)) `quot` as) + (a + 1)
getRetirementAge _ = 0

getInputs :: String -> [Int]
getInpust = (map read).words

main :: IO()
main = interact $ show.getRetirementAge.getInputs
