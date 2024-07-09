arn = "arn:aws:iam:123:user/gouse"
userName = arn.split("/")
print(userName)
print("user name is:" ,userName[1])
