
def find_index(words, target):
  return words.index(target)

if __name__ == '__main__':
  assert find_index(["apple", "banana", "cherry", "peach", "watermelon"], "cherry") == 2
  print(find_index(["apple", "banana", "cherry", "peach", "watermelon"], "cherry"))