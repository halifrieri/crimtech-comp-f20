def sum(lst, n):
	for i in range(len(lst)):
		for j in range(len(lst)):
			if (i != j and lst[i-1] + lst[j-1] == n):
				return True
	return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()