-- recursively calculate nth fibbonacci
fib :: (Integral a) => a -> a
fib 0 = 1
fib 1 = 1
fib i = fib (i - 1) + fib (i - 2)


-- recursively calculate sequence of first n fibbonacci numbers
fibSeq :: (Integral a) => a -> [a]
fibSeq = reverse . fibSeqHelper

fibSeqHelper :: (Integral a) => a -> [a]
fibSeqHelper 0 = [1]
fibSeqHelper 1 = [1, 1]
fibSeqHelper i =
  let subSeq = fibSeqHelper (i - 1)
   in (sum (take 2 subSeq)) : subSeq

