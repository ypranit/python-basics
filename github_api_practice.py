try:
    response = requests.get(
        "https://api.github.com/users/ypranit"
    )

    data = response.json()

    print(data["followers"])

except Exception as e:
    print(e)