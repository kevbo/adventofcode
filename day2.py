
def get_boxes():

    with open('day2_input.txt') as f:
        data = f.readlines()
    boxes = []
    for box in data:
        l, w, h = box.strip().split('x')
        boxes.append((int(l), int(w), int(h)))
    return boxes


def p1():
    boxes = get_boxes()
    total_surface_area = 0
    for box in boxes:
        l, w, h = box
        surface_area = 2*l*w + 2*w*h + 2*h*l
        smallest_side_area = sorted(box)[0] * sorted(box)[1]
        total_surface_area += (surface_area + smallest_side_area)

    print total_surface_area


def p2():
    total_ribbon_required = 0
    boxes = get_boxes()
    for box in boxes:
        smallest_perimeter = (sorted(box)[0] * 2) + (sorted(box)[1] * 2)
        volume = box[0] * box[1] * box[2]
        ribbon_required = smallest_perimeter + volume
        total_ribbon_required += ribbon_required

    print total_ribbon_required

if __name__ == '__main__':
    p1()
    p2()
