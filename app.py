import requests
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/extract', methods=['GET'])
def extract():
    carts = requests.get("https://dummyjson.com/carts/").json()
    users = requests.get("https://dummyjson.com/users/").json()

    extractCartsList = [cart["userId"] for cart in carts["carts"]]
    extractUsersList = [user["id"] for user in users["users"]]

    combinedUsers = list(set(extractCartsList).intersection(extractUsersList))

    totalList = [carts["carts"][i]["total"] for i in combinedUsers if i < carts["limit"]]
    usersList = [i for i in combinedUsers if i < carts["limit"]]

    finalList = pd.DataFrame(
        {'UserId': usersList,
         'Total': totalList
         }).sort_values(by='Total', ascending=False)

    return render_template('table.html', data=finalList.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=14484)