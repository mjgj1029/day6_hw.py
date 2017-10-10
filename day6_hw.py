import turtle as t

angle = 150           #트리 꼭대기 별
t.bgcolor("black")
t.color("yellow")
t.speed(20)
for x in range(50):
    t.forward(x)
    t.left(angle)

t.color("green")
t.left(10)
t.forward(30)
t.right(70)

n = 3                 #첫번째 삼각형 (나무)
t.begin_fill()
for x in range(n):
    t.forward(60)
    t.left(360/n)
t.end_fill()

t.left(30)
t.forward(30)
t.right(30)

n = 3                  #두번째 삼각형 (나무)
t.begin_fill()
for x in range(n):
    t.forward(98)
    t.left(360/n)
t.end_fill()

t.left(30)
t.forward(40)
t.right(30)

n = 3                   #세번째 삼각형 (나무)
t.begin_fill()
for x in range(n):
    t.forward(140)
    t.left(360/n)
t.end_fill()

t.left(30)
t.forward(50)
t.right(30)

n = 3                  #네번째 삼각형 (나무)
t.begin_fill()
for x in range(n):
    t.forward(180)
    t.left(360/n)
t.end_fill()

t.left(30)
t.forward(155.88)

t.right(90)
t.forward(10)
t.left(90)


t.color("brown")     #나무 줄기
n = 4
t.begin_fill()
for x in range(n):
    t.forward(20)
    t.left(360/n)
t.end_fill()

t.forward(10)

n = 4
t.begin_fill()
for x in range(n):
    t.forward(20)
    t.left(360/n)
t.end_fill()

t.color("black")
t.right(90)
t.forward(400)
t.right(90)
t.forward(500)


#merry cristmas

t.color("red")
t.pensize(10)

# M
t.forward(80)
t.right(90)
t.forward(35)
t.right(90)
t.forward(80)
t.right(180)
t.forward(80)
t.right(90)
t.forward(35)
t.right(90)
t.forward(80)

t.right(180)
t.forward(80)
t.right(90)
t.forward(9)
t.color("black")
t.forward(6)

t.color("orangered")

# E
t.forward(35)
t.right(180)
t.forward(35)
t.left(90)
t.forward(40)
t.left(90)
t.forward(35)
t.right(180)
t.forward(35)
t.left(90)
t.forward(40)
t.left(90)
t.forward(43)

t.color("black")
t.forward(7)

# R
t.left(90)
t.color("orange")
t.forward(80)
t.right(90)
t.forward(35)
t.right(90)
t.forward(40)
t.right(90)
t.forward(35)
t.left(130)
t.forward(53)

t.left(50)
t.forward(3)
t.color("black")
t.forward(12)

# R
t.left(90)
t.color("gold")
t.forward(80)
t.right(90)
t.forward(35)
t.right(90)
t.forward(40)
t.right(90)
t.forward(35)
t.left(130)
t.forward(53)

t.left(50)
t.forward(3)
t.color("black")
t.forward(37)

# Y
t.left(90)
t.color("yellow")
t.forward(40)
t.left(30)
t.forward(45)
t.right(180)
t.forward(47)
t.left(120)
t.forward(47)

t.right(60)
t.forward(7)
t.color("black")
t.forward(50)

# C
t.color("greenyellow")
t.forward(35)
t.right(180)
t.forward(35)
t.left(90)
t.forward(80)
t.left(90)
t.forward(35)

t.forward(5)
t.color("black")
t.forward(10)

# H
t.color("limegreen")
t.left(90)
t.forward(80)
t.right(180)
t.forward(40)
t.left(90)
t.forward(35)
t.left(90)
t.forward(40)
t.right(180)
t.forward(80)

t.left(90)
t.forward(7)
t.color("black")
t.forward(11)

# R
t.left(90)
t.color("green")
t.forward(80)
t.right(90)
t.forward(35)
t.right(90)
t.forward(40)
t.right(90)
t.forward(35)
t.left(130)
t.forward(53)

t.left(50)
t.forward(3)
t.color("black")
t.forward(14)

# I
t.left(90)
t.color("darkcyan")
t.forward(80)

t.right(180)
t.forward(80)
t.left(90)
t.forward(7)
t.color("black")
t.forward(9)

# S
t.color("steelblue")
t.forward(35)
t.left(90)
t.forward(40)
t.left(90)
t.forward(35)
t.right(90)
t.forward(40)
t.right(90)
t.forward(35)

t.forward(5)
t.color("black")
t.forward(9)

# T
t.color("blue")
t.forward(56)
t.right(180)
t.forward(28)
t.left(90)
t.forward(80)

t.left(90)
t.forward(5)
t.color("black")
t.forward(37)

# M
t.left(90)
t.color("navy")
t.forward(80)
t.right(90)
t.forward(35)
t.right(90)
t.forward(80)
t.right(180)
t.forward(80)
t.right(90)
t.forward(35)
t.right(90)
t.forward(80)

t.left(90)
t.forward(6)
t.color("black")
t.forward(10)

# A
t.left(90)
t.color("darkviolet")
t.forward(80)
t.right(90)
t.forward(35)
t.right(90)
t.forward(40)
t.right(90)
t.forward(35)
t.right(180)
t.forward(35)
t.right(90)
t.forward(40)

t.left(90)
t.forward(6)
t.color("black")
t.forward(9)

# S
t.color("magenta")
t.forward(35)
t.left(90)
t.forward(40)
t.left(90)
t.forward(35)
t.right(90)
t.forward(40)
t.right(90)
t.forward(35)

t.forward(5)
t.color("black")
t.pensize(1)
t.forward(10)
t.right(90)
t.forward(300)
t.left(90)

t.begin_fill()          # 핑크하트1
t.color("pink")
t.pensize(3)
t.left(45)
t.forward(50)
t.right(45)
t.forward(20)
t.right(45)
t.forward(50)
t.right(45)
t.forward(35)
t.right(45)
t.forward(128.25)
t.right(90)
t.forward(128.25)
t.right(45)
t.forward(35)
t.right(45)
t.forward(50)
t.right(45)
t.forward(20)
t.right(45)
t.forward(50)
t.end_fill()

t.right(90)
t.pensize(1)
t.color("black")
t.forward(200)

t.left(135)


t.color("pink")       # 핑크하트2
t.pensize(3)
t.left(45)
t.forward(50)
t.right(45)
t.forward(20)
t.right(45)
t.forward(50)
t.right(45)
t.forward(35)
t.right(45)
t.forward(128.25)
t.right(90)
t.forward(128.25)
t.right(45)
t.forward(35)
t.right(45)
t.forward(50)
t.right(45)
t.forward(20)
t.right(45)
t.forward(50)


t.right(180)
t.color("black")
t.pensize(1)
t.forward(440)
t.left(90)
t.forward(230)

t.right(225)


t.color("pink")      # 핑크하트3
t.pensize(3) 
t.left(45)
t.forward(50)
t.right(45)
t.forward(20)
t.right(45)
t.forward(50)
t.right(45)
t.forward(35)
t.right(45)
t.forward(128.25)
t.right(90)
t.forward(128.25)
t.right(45)
t.forward(35)
t.right(45)
t.forward(50)
t.right(45)
t.forward(20)
t.right(45)
t.forward(50)


t.right(90)
t.pensize(1)
t.color("black")
t.forward(200)

t.left(135)



t.begin_fill()         # 핑크하트4
t.color("pink")
t.pensize(3)
t.left(45)
t.forward(50)
t.right(45)
t.forward(20)
t.right(45)
t.forward(50)
t.right(45)
t.forward(35)
t.right(45)
t.forward(128.25)
t.right(90)
t.forward(128.25)
t.right(45)
t.forward(35)
t.right(45)
t.forward(50)
t.right(45)
t.forward(20)
t.right(45)
t.forward(50)
t.end_fill()


t.left(150)
t.pensize(1)
t.color("black")
t.forward(240)

t.right(105)


t.begin_fill()          # 핑크하트5
t.color("pink")
t.pensize(3)
t.left(45)
t.forward(50)
t.right(45)
t.forward(20)
t.right(45)
t.forward(50)
t.right(45)
t.forward(35)
t.right(45)
t.forward(128.25)
t.right(90)
t.forward(128.25)
t.right(45)
t.forward(35)
t.right(45)
t.forward(50)
t.right(45)
t.forward(20)
t.right(45)
t.forward(50)
t.end_fill()




