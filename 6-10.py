"""6-10

1.每个人都能有多个喜欢的数字，然后打印出来
"""
favorite_number = {
	"Tom": [5,45,11,57],
	"Jay": [34,23,24],
	"Mike": [13],
	"Halen": [54,75,26,11,74,87],
	"Paul": [40,233,722,46,22],
}

for person, number in favorite_number.items():
	if len(number) == 1:
		print(person + "'s favorite number is : " +
                    ",".join(str(num) for num in number) + ".")
	elif len(number) > 1:
		print(person + "'s favorite number are : " +
                    ",".join(str(num) for num in number) + ".")
