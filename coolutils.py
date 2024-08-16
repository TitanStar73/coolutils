import requests
import json

#Send notification to phone via ntfy.sh | Delay can be either 30m,9am formats | Action: [(label, url),(label,url)]
def notify(route, msg = "",title="<>", private = False,priority = 3, action = None, delay=None, markdown_enabled = True):
    cache = "yes"
    if private:
        cache = "no"
    data = {
        "topic": route,
        "message": msg,
        "title": title,
        "priority": priority,
        "markdown":markdown_enabled,
    }

    if delay is not None:
        data["delay"] = delay
    if action is not None:
        #[{ "action": "view", "label": "Google", "url": "https://www.google.com/" }]
        data["actions"] = [{ "action": "view", "label": label, "url": f"https://{url}"} for label,url in action]
    requests.post(f"https://ntfy.sh/",
    data=json.dumps(data),
    headers={"Cache": cache })
    return True

ntfy = notify

oprint = print
RED = 91
GREEN = 92
YELLOW = 93
BLUE = 94
MAGENTA = 95
CYAN = 96
color_codes = {}
START_OF_LINE = "\033[F\r\033[K"

def print(text, end = "\n", color = None,move_cursor = ""):
    color_codes = {None:"\033[0m", 91: '\033[91m', 92: '\033[92m', 93: '\033[93m', 94: '\033[94m', 95: '\033[95m', 96: '\033[96m'}
    oprint(move_cursor,end = color_codes[color])
    oprint(text, end = end)
    oprint(color_codes[None],end = "")
