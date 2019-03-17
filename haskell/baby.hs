import Data.List
import Data.Function
import qualified Data.Map as Map


-- maps
myFindKey :: (Eq k) => k -> [(k, v)] -> Maybe v
myFindKey key [] = Nothing
myFindKey key ((k, v):xs) = if key == k
                               then Just v
                               else myFindKey key xs

myFindKeyFold :: (Eq k) => k -> [(k, v)] -> Maybe v
myFindKeyFold key xs = foldl (\acc (k, v) -> if k == key then Just v else acc) Nothing xs


