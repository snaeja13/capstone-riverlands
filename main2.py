import requests
import re
import pandas as pd

URL = "https://eschome.net/databaseoutput434.php"
REGEX_GET_TABLE = r"(?s)<table id='tabelle1'.*?>(.*?)<\/table>"
REGEX_GROUPS = r"<td align='.*'>\s*(.*?)\s*<\/td>"

response = requests.get(URL)
text = response.text
table_match = re.search(REGEX_GET_TABLE, text)
table_str = table_match.group(1)

groups = re.findall(REGEX_GROUPS, table_str)

values = []
OFFSET = 10
for i in range(0, len(groups), OFFSET):
    val = groups[i:i + OFFSET]
    values.append(val)


df = pd.DataFrame(values)
df.to_csv('lengdogvote.csv', index=None, header=["Ár", "Borg", "Show", "Lög", "Skemmtiatriði", "Voting", "Fyrstalag", "Seinastalag", "Fyrstavote", "Seinastavote"])



