# K06 -- Weighted Random Occupation Picker

Pasta Noodles - Christopher Liu, Tami Takada, Tina Nguyen </br>
SoftDev </br>
2021-09-29

### File I/O
For the input, we used the CSV reader to go through each line and added the row
contents to a dictionary. The CSV module is useful because we don't have to
worry about edge cases like if there is a comma inside one of the values.

```
with open(filename, newline="") as csvfile:
    reader = csv.reader(csvfile)
```

The CSV reader returns an object that we can loop over to get the row contents
in the form of a list. Note that we have to access the reader items in order.

To skip a line, we used `next(reader)`, which we did to skip the row with the
column headers. `next()` returns the next unread row. Thus, when we looped over
the reader, we didn't get the first line.

### Dictionaries
A dictionary is an unordered list of key-value pairs. Keys and values can be
any type, and we use these unique keys to find corresponding values.

Dictionaries are particularly effective at lookup tasks, as they can retrieve a
value given a key (like a real dictionary) very quickly without the need for
list indexes.

We used dictionaries to store the contents of our CSV file, setting the Job
Classes as the keys and the Percentages as the values. In the example below, we
access the corresponding percentage given a job class (the key).

```
print(occupations["Management"])
# prints 6.1 to the terminal
```

We can use `.keys()` and `.values()` to return an object containing the keys
and values of a dictionary, respectively. We can then loop over that object to
get the keys and values.

### Lists
A list is another Python data structure. It is convenient for accessing
specific items at a given index.

The `list()` method converts an iterable, i.e., something that you can loop
over, into a list.

```
list(occupations.keys())
# converts the set of keys in the dictionary to a list
```

### Weighted Randomized Selection


### Other



### GitHub Flavored Markdown
Markdown is an easy way to indicate formatting and styling in plaintext. GitHub
supports Markdown styling, allowing us to make things look pretty. GitHub
Flavored Markdown (GFM) is a variant of Markdown that incorporates
Github-specific features like mentioning another user. The following is a list
of common markdown format examples that are useful for writing documentation.

---

# Header 1 (similar to `<h1>`)
## Header 2
### It keeps going after this (header 3)
#### Subheadings and subheadings (header 4)
##### You get the idea (header 5)

`This is a code snippet`
```
This is also a code snippet, but with
many
lines.
These are helpful for including code because
they have a fixed-width font.
```

- [ ] A checkbox
- [x] A checked box

| Table Header 1 | Table Header 2 |
| --- | --- |
| Row content | Row content |

1. A list
2. It's ordered
   1. You can have sub items and they'll format as expected

* An unordered list
* We get bullets
    * Same as ordered lists
* You can also combine them
    1. Hi there

**Bold** and *italics* and ~~strikethrough~~
