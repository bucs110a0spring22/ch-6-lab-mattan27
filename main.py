import turtle

def seq3np1(n):
  count = 0
  while(n != 1):
    if(n % 2) == 0:
      n = n // 2
    else:
      n = n * 3 + 1
    count = count + 1
  return(count)
  
def drawGraph(max):
  t = turtle.Turtle()
  turtle.Screen()
  t.shape("turtle")
  t.goto(0,0)
  t2 = turtle.Turtle()
  t2.shape("turtle")
  t2.color("red")
  turtle.setworldcoordinates(0, 0, 10, 10)
  max_so_far = 0
  for i in range(1, max+1):
    result = seq3np1(i)
    if result > max_so_far:
      max_so_far = result
    t2.clear()
    t2.goto(0,max_so_far)
    label = "Maximum so far:", i, max_so_far
    t2.write(label)
    turtle.setworldcoordinates(0, 0, i+10, max_so_far+10)
    t.pendown()
    t.goto(i,max_so_far)
    
def main():
  x = input("Value:")
  x = int(x)
  if x > 0:
    print("x > 0")
  else:
    quit()
  for start in range(1, x+1):
    n = seq3np1(start)
    print(start, n)
  drawGraph(x)
main()