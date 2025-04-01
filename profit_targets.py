def stockPairs(stocksProfit, target):
    count = 0
    seen = set() 
    pair = set() 
    
    for i in stocksProfit: 
        if i in seen:
            if i * 2 == target:
                if i not in pair:
                    pair.add(i)
                    count+=1
                else:
                    continue 
        else:
            if (target - i) in seen:
                count += 1
            seen.add(i)
    return count

def test_stockPairs():
    assert stockPairs([5, 7, 9, 13, 11, 6, 6, 3, 3], 12) == 3
    
if __name__ == "__main__":
    test_stockPairs()
    print("All test cases passed!")