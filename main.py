import requests
import re
import pandas as pd

URL = "https://eschome.net/databaseoutput410.php"
REGEX_GET_TABLE = r"(?s)<table id='tabelle1'.*?>(.*?)<\/table>"
REGEX_GROUPS = r"<td align='left'>\s*(.*?)\s*<\/td>"

response = requests.get(URL)
text = response.text

table_match = re.search(REGEX_GET_TABLE, text)
table_str = table_match.group(1)

groups = re.findall(REGEX_GROUPS, table_str)

values = []
for i in range(0, len(groups), 7):
    val = groups[i:i + 7]
    val.pop(1)

    values.append(val)


df = pd.DataFrame(values)
df.to_csv('keppnihaldin.csv', index=None, header=["Ár", "Land", "Borg", "Staðsetning", "Broadcast", "Dagsetning"])



