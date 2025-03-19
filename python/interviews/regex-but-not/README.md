# re-implement regex

exercise on string comparisons and logic

write a function `ismatch` to determine if the input string `s` matches the pattern `p`

patterns consist of letters and 0 or more numbers. each number repeats the previous letter N times.
d3dog, for example, matches ddddog. pattern character classes '[a-zA-Z0-9]'

Strings consist of letters only, '[a-zA-Z]'



examples:

| pattern | string | match |
| ------- | ------ | ----- |
| datadog | datadog | True |
| Datadog | datadog | False |
| spl2unk | spllunk | True |
| "" | foo | True |
| "" | "" | True |
| foo | "" | False |
| 0 | foo | False |
