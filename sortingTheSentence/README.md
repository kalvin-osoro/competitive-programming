# list.insert(position, element)

puts the element exactly at position, shifting any later elements to the right.

So as the loop runs:

1. "this2" → position 2-1 = 1 → insert "this" at index 1 → ["this"]

2. "is1" → position 1-1 = 0 → insert "is" at index 0 → ["is", "this"]

3. "code3" → position 3-1 = 2 → insert "code" at index 2 → ["is", "this", "code"]