import Data.Char

-- ceaser cipher

kaisar :: String -> String
kaisar = map generalKaisarLetter
-- kaisar = map kaisarLetter

-- explicit character maps for reversable ceaser ciphers
kaisarLetter :: Char -> Char
kaisarLetter c
  | c `elem` ['A'..'Z'] = chr $ (ord c - ord 'A' + 13) `mod` 26 + ord 'A'
  | c `elem` ['a'..'z'] = chr $ (ord c - ord 'a' + 13) `mod` 26 + ord 'a'
  | c `elem` ['0'..'9'] = chr $ (ord c - ord '0' + 5) `mod` 10 + ord '0'
  | otherwise = c

generalKaisarLetter :: Char -> Char
generalKaisarLetter c = foldl (\acc l -> generalKaisar l acc) c [['A'..'Z'], ['a'..'z'], ['0'..'9']]

generalKaisar :: [Char] -> Char -> Char
generalKaisar charSet c
  | c >= hChar && c <= lChar = chr $ (ord c - ord hChar + numChars `div` 2) `mod` numChars + ord hChar
  | otherwise = c
  where hChar = head charSet
        lChar = last charSet
        numChars = length charSet

shiftCode :: Int -> String -> String
shiftCode shift = map (\c -> chr $ ord c + shift)

shiftDecode :: Int -> String -> String
shiftDecode shift = shiftCode (negate shift)
