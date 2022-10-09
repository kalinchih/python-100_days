# python-100_days

## Materials
- Udemy Course: https://www.udemy.com/course/100-days-of-code/ 
- Official Website: https://100daysofpython.dev/
- Replit Online Editor: https://replit.com/@appbrewery/
- Coding Rooms: https://app.codingrooms.com/management/courses/join-by-code/4J6slZE6


## Notes
### (Day 2) [浮點數運算：問題與限制](https://docs.python.org/zh-tw/3/tutorial/floatingpoint.html)
- print(150 * 1.12) -> 168.00000000000003
- print((.1 + .1 + .1) == .3) -> False


### (Day 3) 使用 ''' for 多行字串

print('''

           __  _
       .-.'  `; `-._  __  _
      (_,         .-:'  `; `-._
    ,'o"(        (_,           )
   (__,-'      ,'o"(            )>
      (       (__,-'            )
       `-'._.--._(             )
          |||  |||`-'._.--._.-'
                     |||  |||

Artist:  Bob Allison

https://ascii.co.uk/art

''')

### (Day 4) [0 的英文唸法](https://asoenglishschool.com/%E3%80%8C%E9%9B%B6%E3%80%8D%E5%85%B6%E4%BB%96%E8%8B%B1%E6%96%87%E8%AA%AA%E6%B3%95-%E8%8B%B1%E6%96%87%E5%B0%8F%E6%95%B80-001%E6%80%8E%E9%BA%BC%E8%AA%AA-%E6%AF%94%E6%95%B810-%E5%8F%AA%E8%83%BD/)


### (Day 6) [Built-in Functions](https://docs.python.org/3/library/functions.html)

### (Day 6) [Style Guide for Python Code](https://peps.python.org/pep-0008/)

### (Day 6) [Reeborg's world - interesting game to practice functions](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)

#### Hurdle 4
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    else:
        if not wall_in_front():
            move()
        else:
            turn_left()
 
```

#### Maze
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
 
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    else:
        if front_is_clear():
            move()
        else:
            turn_left()
    
print("Finish!")
```


### (Day 12) Local scope variable 只在 def() 內，不包含 while、if、for 之類有：的判斷式內，下面範例:
```
enemies = 1

def increase_enemies():
    # global enemies
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
```

Output:
```
enemies inside function: 2
enemies outside function: 1
```