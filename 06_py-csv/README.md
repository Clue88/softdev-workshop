# K06 -- Weighted Random Occupation Picker

Pasta Noodles - Christopher Liu, Tami Takada, Tina Nguyen </br>
SoftDev </br>
2021-09-29

### File I/O

For the input, we used the CSV reader to go through each line and
added the row contents to a dictionary. The CSV module is useful
because we don't have to worry about edge cases like if there is
a comma inside one of the values.

```
with open(filename, newline="") as csvfile:
    reader = csv.reader(csvfile)
```

The CSV reader returns an object that we can loop over to get the
row contents in the form of a list. Note that we have to access the
reader items in order.

To skip a line, we used `next(reader)`, which we did to skip the
row with the column headers. `next()` returns the next unread row.
Thus, when we looped over the reader, we didn't get the first line.

### Dictionaries

A dictionary is an unordered list of key-value pairs. Keys and values
can be any type, and we use these unique keys to find corresponding
values.

Dictionaries are particularly effective at lookup tasks, as they can
retrieve a value given a key (like a real dictionary) very quickly
without the need for list indexes.

We used dictionaries to store the contents of our CSV file, setting
the Job Classes as the keys and the Percentages as the values. In
the example below, we access the corresponding percentage given a
job class (the key).

```
print(occupations["Management"])
# prints 6.1 to the terminal
```

We can use `.keys()` and `.values()` to return an object containing
the keys and values of a dictionary, respectively. We can then loop
over that object to get the keys and values.

### Lists

A list is another Python data structure. It is convenient for
accessing specific items at a given index.

The `list()` method converts an iterable, i.e., something that
you can loop over, into a list.

```
list(occupations.keys())
# converts the set of keys in the dictionary to a list
```

### GitHub Flavored Markdown


### Weighted Randomized Selection


### Other
