def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  count=len(quotes)
  f.close()

  print(quotes[count-1])

if __name__== "__main__":
  primary()
