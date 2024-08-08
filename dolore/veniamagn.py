def combine_boxes(box1, box2):
    x1 = min(box1[0], box2[0])
    y1 = min(box1[1], box2[1])
    x2 = max(box1[2], box2[2])
    y2 = max(box1[3], box2[3])
    return (x1, y1, x2, y2)

box1 = (10, 10, 20, 20)
box2 = (15, 15, 25, 25)

combined_box = combine_boxes(box1, box2)
print(combined_box)  # Output: (10, 10, 25, 25)
