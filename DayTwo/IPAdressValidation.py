#Match 1 to 9 then 100 to 199 then 200 to 249 then 250 to 254
# Logic is first match for 1-9, or [1-9]0-9] or 1[0-9][0-9] or 2[0-4][0-9] or 25[0-4]
# Replace [1-9] with \d  [1-9] | [1-9]\d   | 1\d{2}       |   2[0-4]\d   |  25[0-4]

