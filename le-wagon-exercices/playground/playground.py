age= 4print(age)age=age+1print(age)radius=6print(radius)Pi=3.14print(Pi)perimeter= radius * Piprint(perimeter)Pisquare=Pi**2area= Pisquare*radiusprint(area)def circle_math(radius):    perimeter = 2 * Pi * radius    area = Pi * radius * radius    return [ perimeter, area ] # perimeter and area are called **local variables**print(circle_math(3))# TODO: it's a playground, let's write some code (no unit tests to run here)