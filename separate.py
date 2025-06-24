str = "Robert000Smith000123"
k = str.split("000")
ans ={'first_name': k[0], 'last_name': k[1], 'id': k[2] }
print(ans)