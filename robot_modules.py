import geometry

def main():
    rect_area = geometry.rectangle_area(5, 3)
    circ_area = geometry.circle_area(7)
    print(f'Area of the rectangle: {rect_area}')
    print(f'Area of the circle: {circ_area}')

if __name__ == '__main__':
    main()