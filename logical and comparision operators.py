
is_hot = False
day = "Monday"

if is_hot and day == "Monday":
    print("Monday is hot" )

if is_hot or day == "Monday":
    print("Monday is hot" )


if not is_hot and day == "Monday":
    print("Monday is cold" )

tempe = 10
                            # == equal , > greater than, < less than, != not equal, <= less than and equal to
                            # >= greater than and equal to
if tempe > 35:
    print("Weather is hot")
elif tempe < 35 and tempe > 20:
    print("Weahter is pleasent")
else:
    print("Weather is cold")