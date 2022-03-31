def intersection(set1, set2)
  set3 = set();
  for number in set1:
    if number in set2:
      set3.add(number)
  return set3
