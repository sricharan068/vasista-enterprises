# Function to join given strings
def combo_string(a, b):

    # your code here
    if len(a)>len(b):
        short=b
        longer=a
    else:
        short=a
```        longer=b
    return short + longer + short
a=str(input())
b=str(input())
print(combo_string(a, b))
