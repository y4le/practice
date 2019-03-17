-- first haskell practice
-- super simple funcitons and re-implementations of built ins

doubleMe x = x + x

doubledAdd x y = doubleMe x + doubleMe y

doubleSmall x = if x < 100
                  then x * 2
                  else x

doubleSmallSucc x = doubleSmall x + 1

reTake :: Int -> [a] -> a
reTake i l = l !! i

secondEl :: [a] -> a
-- secondEl l = head (tail l)
secondEl l = l !! 1

withoutFirstTwo :: [a] -> [a]
-- withoutFirstTwo l = tail (tail l)
withoutFirstTwo l = drop 2 l

firstTwo :: [a] -> [a]
-- firstTwo l = [head l, secondEl l]
firstTwo l = take 2 l

pythag :: (Integral a) => a -> [(a, a, a)]
pythag perim = [(x, y, z) | x <- [1..10], y <- [1..x], z <- [1..y], y^2 + z^2 == x^2, x + y + z == perim]

onlyLower :: String -> String
onlyLower s = [c | c <- s, c `elem` ['a'..'z']]

onlyUpper :: String -> String
onlyUpper s = [c | c <- s, c `elem` ['A'..'Z']]

factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial i = i * factorial (i - 1)

addVectors :: (Num a) => (a, a) -> (a, a) -> (a, a)
addVectors (xx, xy) (yx, yy) = (xx + yx, xy + yy)

recursiveLength :: (Num b) => [a] -> b
recursiveLength [] = 0
recursiveLength (_:xs) = 1 + recursiveLength xs

recursiveSum :: (Num a) => [a] -> a
recursiveSum [] = 0
recursiveSum (x:xs) = x + recursiveSum xs

bmiTell :: (Ord a, Fractional a) => a -> a -> String
bmiTell weight height
  | bmi <= skinny = "insect"
  | bmi <= norm = "monkey"
  | bmi <= fat = "elephant"
  | otherwise   = "whale"
  where bmi = head (calcBmis [(weight, height)])
        (skinny, norm, fat) = (18.5, 25.0, 30.0)

calcBmis :: (Ord a, Fractional a) => [(a, a)] -> [a]
calcBmis xs = [bmi | (w, h) <- xs, let bmi = w / h ^ 2]

myTake :: (Num a, Ord a) => a -> [a] -> [a]
myTake 0 _ = []
myTake _ [] = []
myTake i (x:xs) = x : myTake (i - 1) xs

myReplicate :: (Integral a) => a -> b -> [b]
myReplicate i x
  | i <= 0 = []
  | otherwise = x : myReplicate (i - 1) x
-- myReplicate 0 _ = []
-- myReplicate i x = x : myReplicate (i - 1) x

myReverse :: [a] -> [a]
myReverse [] = []
myReverse l = (last l) : myReverse (init l)

myRepeat :: a -> [a]
myRepeat x = x : myRepeat x

myZip :: [a] -> [b] -> [(a, b)]
myZip _ [] = []
myZip [] _ = []
myZip (ha:ta) (hb:tb) = (ha, hb) : myZip ta tb

myElem :: (Eq a) => a -> [a] -> Bool
myElem _ [] = False
myElem i (x:xs)
  | i == x = True
  | otherwise = i `myElem` xs

quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) =
  let smallsort = quicksort (filter (<= x) xs)
      bigsort = quicksort  (filter (> x) xs)
  -- let smallsort = quicksort [i | i <- xs, i <= x]
  --     bigsort = quicksort [i | i <- xs, i > x]
   in smallsort ++ [x] ++ bigsort

mySquare :: (Num a) => a -> a
mySquare i = i ^ 2

doubleApply :: (a -> a) -> a -> a
-- doubleApply f x = f (f x)
doubleApply f x = applyN 2 f x

myFourth :: (Num a) => a -> a
myFourth i = doubleApply mySquare i

applyN :: (Integral b) => b -> (a -> a) -> a -> a
applyN 0 _ x = x
applyN n f x = f (applyN (n - 1) f x)

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith _ _ [] = []
myZipWith _ [] _ = []
myZipWith f (a:xa) (b:xb) = f a b : myZipWith f xa xb

myFlip :: (a -> b -> c) -> b -> a -> c
myFlip f a b = f b a

myMap :: (a -> b) -> [a] -> [b]
myMap _ [] = []
myMap f (x:xs) = f x : myMap f xs

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter _ [] = []
myFilter f (x:xs)
  | f x = x : myFilter f xs
  | otherwise = myFilter f xs

-- largest num under 100000 divisible by 3829
largestNumUnderDivisible :: (Num a, Eq a, Enum a, Integral a) => a -> a -> a
largestNumUnderDivisible divisor cutoff = head [i | i <- (reverse [1..cutoff]), i `mod` divisor == 0]

largestNumUnder100000DivisibleBy3829 :: Integer
largestNumUnder100000DivisibleBy3829 = largestNumUnderDivisible 3829 100000

collatz :: (Integral a) => a -> [a]
collatz 1 = [1]
collatz i
  | even i = i : collatz (i `div` 2)
  | odd i = i : collatz (i * 3 + 1)

countCollatzBeneath :: (Integral a) => Int -> a -> Int
-- countCollatzBeneath cutoff i = length (filter (> cutoff) (map (\x -> length (collatz x)) [1..i]))
countCollatzBeneath cutoff i = length . filter (> cutoff) $ map (length . collatz) [1..i]

-- for all starting numbers between 1 and 100, how many chains have a length greater than 15
-- countCollatzBeneath 15 100

foldlSum :: (Num a) => [a] -> a
foldlSum xs = foldl (\acc i -> acc + i) 0 xs

foldlSum' :: (Num a) => [a] -> a
foldlSum' = foldl (+) 0

foldlElem :: (Eq a) => a -> [a] -> Bool
foldlElem i = foldl (\acc n -> acc || i == n) False

foldrSum :: (Num a) => [a] -> a
foldrSum xs = foldr (+) 0 xs

foldrMax :: (Ord a) => [a] -> a
foldrMax xs = foldr1 (\acc x -> if x > acc then x else acc) xs

foldrMap :: (a -> b) -> [a] -> [b]
foldrMap f xs = foldr (\x acc -> (f x) : acc) [] xs

foldrFilter :: (a -> Bool) -> [a] -> [a]
foldrFilter f xs = foldr (\x acc -> if f x then x : acc else acc) [] xs

foldReverse :: [a] -> [a]
foldReverse xs = foldl (flip (:)) [] xs

-- How many elements does it take for the sum of the roots of all natural numbers to exceed 1000
numRootSumBelow :: (Ord a, Floating a, Enum a) => a -> Int
-- numRootSumBelow i = length (takeWhile (<i) (scanl (+) 0 (map sqrt [1..])))
numRootSumBelow i = length $ takeWhile (<i) $ scanl (+) 0 $ map sqrt [1..]
-- numRootSumBelow 1000 + 1

