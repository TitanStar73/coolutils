# Installation

`pip install utilscool`

Then import with: `from coolutils import coolutils`

# Cool one-liners to show its power!:
```
coolutils.plot(
    [1.01**x for x in range(0,365)], 
    plt_title = "Daily 1% improvement", 
    x_labels = "Days", 
    y_labels = "Improvement")
```
This simple line, outputs:

![image](https://github.com/user-attachments/assets/29dfd9c0-f0c6-4b15-94ba-2fe32c12ecc0)

# notify

> This uses ntfy.sh
> Read their docs on ntfy.sh
> To receive notifcations you must download the ntfy.sh app and select a 'route' id

Parameters

route
> Route id

msg = ""
> msg content

title="<>"
> title

private = False
> Only sends the notifcation once when enabled, if the phone is not connected to the internet it will not receive it

priority = 3
> priority, only affects the app based on the settings chosen.
> Can be any integer from 1-5

action = None
> Used to create buttons linking to a url
```action = [("Google", "google.com"),("Example","example.com")] # [(label,url)] ```

delay=None
> Creates a delay

markdown_enabled = True
> Enables/Disables markdown

# pretty print
This replaces the print function when imported.
The new syntax is:
`print("Hello",end = " ",color=RED, move_cursor = START_OF_LINE)`

# plot
Just throw some values into it and it will plot them :)
`plot([1,2,4,8])`

# Database

First initialize a new database

`columns = [("name",str),("id",int),("score", float)]`

`data = Database("filename.db", columns)`

Now data can be used as a list of dictionaries :)

`data.append(("NAME1", 1, 1.1))`

`data[0]["id"] #-> 1`

# Retry

Decorator for use in debugging or web-requests
```
@retry(retries = 3, delay = 1, exponential_delay = True)
def myfunc():
    pass
```

# Timer

`start_timer()` - Stars/resets timer

`get_timer()` - Gets timer value as a `datetime` object
