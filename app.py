from urllib.request import urlopen
import json
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/extract', methods=['GET'])
def extract():
    carts = urlopen("https://dummyjson.com/carts/")
    users = urlopen("https://dummyjson.com/users/")
    carts_data = json.loads(carts.read())
    users_data = json.loads(users.read())

    extractCartsList = []
    extractUsersList = []

    for i in range(carts_data["limit"]):
        extractCarts = carts_data["carts"][i]["userId"]
        extractCartsList.append(extractCarts)

    for j in range(users_data["limit"]):
        extractUsers = users_data["users"][j]["id"]
        extractUsersList.append(extractUsers)

    combinedUsers = list(set(extractCartsList).intersection(extractUsersList))

    totalList = []
    usersList = []

    for i in combinedUsers:
        if i < carts_data["limit"]:
            total = carts_data["carts"][i]["total"]
            totalList.append(total)
            usersList.append(i)

    finalList = pd.DataFrame(
        {'UserId': usersList,
         'Total': totalList
         }).sort_values(by='Total', ascending=False)

    return render_template('table.html', data=finalList.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=14484)