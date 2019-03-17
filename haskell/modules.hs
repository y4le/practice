import Data.List
import Data.Char
import Data.Function

-- MODULES

numUniques :: (Eq a) => [a] -> Int
numUniques = length . nub

-- sum of third powers less than 10000

listPowers :: (Num a, Ord a, Integral a, Enum a) => a -> a -> [a]
listPowers pwr cutoff = takeWhile (< cutoff) $ map (^ pwr) [1..]

sumPowers :: (Integral a) => a -> a -> a
sumPowers pwr cutoff = sum $ listPowers pwr cutoff

thirdPowersLessThan10000 :: Integer
thirdPowersLessThan10000 = sumPowers 3 10000

filteredPowers :: (Num a, Integral a) => (a -> Bool) -> a -> a -> [a]
filteredPowers f pwr cutoff = filter f $ listPowers pwr cutoff

sumFilteredPowers :: (Integral a) => (a -> Bool) -> a -> a -> a
sumFilteredPowers f pwr = sum . filteredPowers f pwr

countFilteredPowers :: (Integral a) => (a -> Bool) -> a -> a -> Int
countFilteredPowers f pwr = length . filteredPowers f pwr

sumOddThirdsLessThan10000 :: Integer
sumOddThirdsLessThan10000 = sumFilteredPowers odd 3 10000
-- sumOddSquaresLessThan10000 = sum . filter odd . takeWhile (<10000) . map (^2) $ [1..]
-- sumOddSquaresLessThan10000 = sum (filter odd (takeWhile (<10000) (map (^2) [1..])))
-- sumOddSquaresLessThan10000 = sum [i | i <- (takeWhile (<10000) [j^2 | j <- [1..]]), odd i]

allOdd :: (Integral a) => [a] -> Bool
allOdd = all odd

infixer :: (Eq a) => [a] -> [a] -> Bool
infixer = isInfixOf
-- infixer needle haystack =
--   let needlelen = length needle
--    in foldl (\acc tl -> acc || take needlelen tl == needle) False $ tails haystack

myWords :: String -> [String]
myWords str = filter (not . any isSpace) $ groupBy ((==) `on` isSpace) str

iterCollatz :: (Integral a) => a -> [a]
iterCollatz = takeWhile (>1) . iterate (\x -> if even x then x `div` 2 else x * 3 + 1)

