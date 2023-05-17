class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.lt = Point(x1, y1)  # 좌측 상단 꼭짓점
        self.rb = Point(x2, y2)  # 우측 하단 꼭짓점

    def show(self):
        print(f"좌측 상단 꼭지점이 ({self.lt.x}, {self.lt.y})이고 우측 하단 꼭지점이 ({self.rb.x}, {self.rb.y})인 사각형입니다.")

    def getWidth(self):
        return self.rb.x - self.lt.x

    def getHeight(self):
        return self.rb.y - self.lt.y

    def getArea(self):
        width = self.getWidth()
        height = self.getHeight()
        return width * height

    def getPerimeter(self):
        width = self.getWidth()
        height = self.getHeight()
        return 2 * (width + height)

# 주 프로그램부
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
