#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
  i = 0
  count = 0
 #   index = 0
  #  for i in my_list:
   #     if index < x:
    #        try:
             #   print("{:d}".format(i), end="")
            #except ValueError:
           #     index += 1
          #      continue
         #   except TypeError:
        #        index += 1
       #         continue
      #  else:
     #       print("")
    #        return count
   #     index += 1
  #      count += 1
 #   print("")
#    return count
  while True:
    if i == x:
        print("")
        return count
    try:
      print("{:d}".format(my_list[i]), end="")
    except TypeError:
      i += 1
      continue
    except ValueError:
      i += 1
      continue
    i += 1
    count += 1
    #except IndexError:
