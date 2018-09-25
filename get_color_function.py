def get_color(color):
  color_int=0
  for i in range(3): 
    color_str=input("Pls enter an interger of the "+color+" color from 0 to 255:")
    try:
      color_int=int(color_str)
      if not 0<=color_int<=255:
        print("You can not input an integer that is not in the range of 0-255;try again.")
        continue
      return color_int
      
    except:
      print("not a integer.Try again.")
      continue
  return 0 
