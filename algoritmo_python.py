
# boxes = [100, 90, 70 ,30 ,20]

volume = 136


def algoritm(boxes,total_volume):
  used_boxes =[]
  boxes.sort(reverse=True)


  big_boxes = []
  ideal_big_box = []
  saved_total_volume = total_volume

  if boxes[0] > total_volume:
    for box in boxes:
      if box >= total_volume:
        big_boxes.append(box)
    ideal_big_box.append(big_boxes[-1])
    if boxes[-1]>total_volume:
      return ideal_big_box

  for box in boxes:
    while total_volume >= box:
      total_volume -= box
      used_boxes.append(box)


  if total_volume == 0:
    return used_boxes

  small_boxes = []

  if len(used_boxes):
    for box in boxes:
      
      if box >= (used_boxes[-1] + total_volume):
        small_boxes.append(box)
   
    if len(small_boxes):
      ideal_small_box = small_boxes[-1]
    


  if not('ideal_small_box' in locals()):
    ideal_small_box = 100000000000



  if len(ideal_big_box) and ideal_big_box[0] > 0:


    big_box_difference = ideal_big_box[0] - saved_total_volume   

    if big_box_difference <= (ideal_small_box - (used_boxes[-1] + total_volume)) and big_box_difference <= (boxes[-1]-total_volume):

      return ideal_big_box
  #essa comparação tenho q determinar qnd q da pra parar elae repetir ela
  if (ideal_small_box - (used_boxes[-1] + total_volume)) <= (boxes[-1]-total_volume):

    used_boxes.pop()
    used_boxes.append(ideal_small_box)

    boxes.sort()
    for i in boxes:
      if i == (used_boxes[-1]+used_boxes[-2]):
        used_boxes.pop()
        used_boxes.pop()
        used_boxes.append(i)
      if len(used_boxes)>= 3:
        if i == (used_boxes[-3]+used_boxes[-2]+used_boxes[-1]):
          used_boxes.pop()
          used_boxes.pop()
          used_boxes.pop()
          used_boxes.append(i)
    return used_boxes



  used_boxes.append(boxes[-1])

  list_legal = []
  list_diff = []
  boxes.sort(reverse=True)
  for b in boxes:
    if b < used_boxes[-2]:
      list_legal.append(b)
  for i in list_legal:
    if ((i+used_boxes[-1]) - (used_boxes[-2] + total_volume) ) >=0:

      if (used_boxes[-1] -total_volume) >= ((i+used_boxes[-1]) -(used_boxes[-2]+total_volume)):
        # esse if ou a lina 94 pode ta errado n quero mais pensar nisso hj
        list_diff.append((used_boxes[-2]+total_volume) - (i + boxes[-1]))
  for index,indici in enumerate(list_diff):
    if indici <= ((used_boxes[-2]+used_boxes[-1])-(used_boxes[-2]+total_volume)):

      used_boxes[-2] = list_legal[index]
      return used_boxes
      

  return used_boxes
# boxes = [20, 30, 90,100]
boxes = [10, 5, 20, 30,40, 90,100]
print(algoritm(boxes,volume))

total_volume = 186
print(algoritm(boxes,total_volume ), 186)
total_volume = 121
print(algoritm(boxes,total_volume ), 121)
total_volume = 116
print(algoritm(boxes,total_volume), 116)
total_volume = 386
print(algoritm(boxes,total_volume ), 386)
total_volume = 86
print(algoritm(boxes,total_volume ), 86)
total_volume = 56
print(algoritm(boxes,total_volume ), 56)
total_volume = 12
print(algoritm(boxes,total_volume ), 12)
total_volume = 1.2
print(algoritm(boxes,total_volume ), 1.2)


