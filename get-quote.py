import random
def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  count=len(quotes)
  f.close()
  rnd = random.randint(0, count)
  print(quotes[rnd])

if __name__== "__main__":
  primary()
