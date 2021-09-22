def findDecision(obj): #obj[0]: 0, obj[1]: 1, obj[2]: 2, obj[3]: 3, obj[4]: 4, obj[5]: 5
   # {"feature": "0", "instances": 691, "metric_value": 95.3382, "depth": 1}
   if obj[0] == 'vhigh':
      # {"feature": "1", "instances": 186, "metric_value": 26.7721, "depth": 2}
      if obj[1] == 'low':
         # {"feature": "3", "instances": 50, "metric_value": 10.0066, "depth": 3}
         if obj[3] == '2':
            return 'unacc'
         elif obj[3] == 'more':
            # {"feature": "5", "instances": 16, "metric_value": 7.4472, "depth": 4}
            if obj[5] == 'high':
               return 'acc'
            elif obj[5] == 'med':
               # {"feature": "4", "instances": 6, "metric_value": 5.8637, "depth": 5}
               if obj[4] == 'med':
                  return 'acc'
               elif obj[4] == 'small':
                  return 'unacc'
               elif obj[4] == 'big':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[5] == 'low':
               return 'unacc'
            else:
               return 'unacc'
         elif obj[3] == '4':
            # {"feature": "5", "instances": 14, "metric_value": 6.3741, "depth": 4}
            if obj[5] == 'low':
               return 'unacc'
            elif obj[5] == 'med':
               # {"feature": "4", "instances": 5, "metric_value": 4.4495, "depth": 5}
               if obj[4] == 'small':
                  return 'unacc'
               elif obj[4] == 'big':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[5] == 'high':
               return 'acc'
            else:
               return 'acc'
         else:
            return 'unacc'
      elif obj[1] == 'med':
         # {"feature": "5", "instances": 47, "metric_value": 8.8968, "depth": 3}
         if obj[5] == 'low':
            return 'unacc'
         elif obj[5] == 'high':
            # {"feature": "3", "instances": 16, "metric_value": 9.7566, "depth": 4}
            if obj[3] == '2':
               return 'unacc'
            elif obj[3] == 'more':
               return 'acc'
            elif obj[3] == '4':
               return 'acc'
            else:
               return 'acc'
         elif obj[5] == 'med':
            # {"feature": "4", "instances": 15, "metric_value": 7.0683, "depth": 4}
            if obj[4] == 'small':
               return 'unacc'
            elif obj[4] == 'med':
               # {"feature": "2", "instances": 6, "metric_value": 4.8284, "depth": 5}
               if obj[2] == '3':
                  return 'unacc'
               elif obj[2] == '4':
                  # {"feature": "3", "instances": 2, "metric_value": 2.8284, "depth": 6}
                  if obj[3] == '2':
                     return 'unacc'
                  elif obj[3] == 'more':
                     return 'acc'
                  else:
                     return 'acc'
               elif obj[2] == '2':
                  return 'unacc'
               elif obj[2] == '5more':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[4] == 'big':
               return 'acc'
            else:
               return 'acc'
         else:
            return 'unacc'
      elif obj[1] == 'high':
         return 'unacc'
      elif obj[1] == 'vhigh':
         return 'unacc'
      else:
         return 'unacc'
   elif obj[0] == 'low':
      # {"feature": "1", "instances": 176, "metric_value": 38.5003, "depth": 2}
      if obj[1] == 'vhigh':
         # {"feature": "5", "instances": 53, "metric_value": 8.7356, "depth": 3}
         if obj[5] == 'high':
            # {"feature": "3", "instances": 21, "metric_value": 11.2058, "depth": 4}
            if obj[3] == '4':
               return 'acc'
            elif obj[3] == 'more':
               return 'acc'
            elif obj[3] == '2':
               return 'unacc'
            else:
               return 'unacc'
         elif obj[5] == 'med':
            # {"feature": "3", "instances": 18, "metric_value": 5.7001, "depth": 4}
            if obj[3] == 'more':
               # {"feature": "4", "instances": 7, "metric_value": 4.6802, "depth": 5}
               if obj[4] == 'big':
                  return 'acc'
               elif obj[4] == 'med':
                  # {"feature": "2", "instances": 3, "metric_value": 4.2426, "depth": 6}
                  if obj[2] == '2':
                     return 'unacc'
                  elif obj[2] == '4':
                     return 'acc'
                  elif obj[2] == '5more':
                     return 'acc'
                  else:
                     return 'acc'
               elif obj[4] == 'small':
                  return 'unacc'
               else:
                  return 'unacc'
            elif obj[3] == '2':
               return 'unacc'
            elif obj[3] == '4':
               # {"feature": "4", "instances": 5, "metric_value": 5.4142, "depth": 5}
               if obj[4] == 'small':
                  return 'unacc'
               elif obj[4] == 'big':
                  return 'acc'
               elif obj[4] == 'med':
                  return 'acc'
               else:
                  return 'acc'
            else:
               return 'acc'
         elif obj[5] == 'low':
            return 'unacc'
         else:
            return 'unacc'
      elif obj[1] == 'med':
         # {"feature": "5", "instances": 47, "metric_value": 19.5834, "depth": 3}
         if obj[5] == 'high':
            # {"feature": "3", "instances": 19, "metric_value": 11.9768, "depth": 4}
            if obj[3] == 'more':
               # {"feature": "4", "instances": 7, "metric_value": 6.4495, "depth": 5}
               if obj[4] == 'med':
                  return 'vgood'
               elif obj[4] == 'big':
                  return 'vgood'
               elif obj[4] == 'small':
                  return 'good'
               else:
                  return 'good'
            elif obj[3] == '2':
               return 'unacc'
            elif obj[3] == '4':
               # {"feature": "4", "instances": 6, "metric_value": 5.8637, "depth": 5}
               if obj[4] == 'small':
                  return 'good'
               elif obj[4] == 'big':
                  return 'vgood'
               elif obj[4] == 'med':
                  return 'good'
               else:
                  return 'good'
            else:
               return 'good'
         elif obj[5] == 'low':
            return 'unacc'
         elif obj[5] == 'med':
            # {"feature": "3", "instances": 13, "metric_value": 9.4472, "depth": 4}
            if obj[3] == '4':
               # {"feature": "4", "instances": 6, "metric_value": 3.8637, "depth": 5}
               if obj[4] == 'small':
                  return 'acc'
               elif obj[4] == 'med':
                  # {"feature": "2", "instances": 2, "metric_value": 2.8284, "depth": 6}
                  if obj[2] == '4':
                     return 'good'
                  elif obj[2] == '3':
                     return 'acc'
                  else:
                     return 'acc'
               elif obj[4] == 'big':
                  return 'good'
               else:
                  return 'good'
            elif obj[3] == '2':
               return 'unacc'
            elif obj[3] == 'more':
               # {"feature": "4", "instances": 3, "metric_value": 4.2426, "depth": 5}
               if obj[4] == 'med':
                  return 'good'
               elif obj[4] == 'small':
                  return 'acc'
               elif obj[4] == 'big':
                  return 'good'
               else:
                  return 'good'
            else:
               return 'good'
         else:
            return 'acc'
      elif obj[1] == 'high':
         # {"feature": "3", "instances": 39, "metric_value": 13.6481, "depth": 3}
         if obj[3] == 'more':
            # {"feature": "5", "instances": 14, "metric_value": 12.2388, "depth": 4}
            if obj[5] == 'med':
               return 'acc'
            elif obj[5] == 'high':
               # {"feature": "4", "instances": 5, "metric_value": 4.4495, "depth": 5}
               if obj[4] == 'med':
                  return 'vgood'
               elif obj[4] == 'small':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[5] == 'low':
               return 'unacc'
            else:
               return 'unacc'
         elif obj[3] == '4':
            # {"feature": "5", "instances": 13, "metric_value": 11.4472, "depth": 4}
            if obj[5] == 'high':
               # {"feature": "4", "instances": 6, "metric_value": 5.8637, "depth": 5}
               if obj[4] == 'big':
                  return 'vgood'
               elif obj[4] == 'med':
                  return 'acc'
               elif obj[4] == 'small':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[5] == 'med':
               return 'acc'
            elif obj[5] == 'low':
               return 'unacc'
            else:
               return 'unacc'
         elif obj[3] == '2':
            return 'unacc'
         else:
            return 'unacc'
      elif obj[1] == 'low':
         # {"feature": "5", "instances": 37, "metric_value": 17.7256, "depth": 3}
         if obj[5] == 'med':
            # {"feature": "3", "instances": 16, "metric_value": 10.5284, "depth": 4}
            if obj[3] == 'more':
               # {"feature": "4", "instances": 7, "metric_value": 4.8165, "depth": 5}
               if obj[4] == 'med':
                  # {"feature": "2", "instances": 3, "metric_value": 4.2426, "depth": 6}
                  if obj[2] == '3':
                     return 'good'
                  elif obj[2] == '5more':
                     return 'good'
                  elif obj[2] == '2':
                     return 'acc'
                  else:
                     return 'acc'
               elif obj[4] == 'small':
                  return 'acc'
               elif obj[4] == 'big':
                  return 'good'
               else:
                  return 'good'
            elif obj[3] == '2':
               return 'unacc'
            elif obj[3] == '4':
               # {"feature": "2", "instances": 4, "metric_value": 5.6569, "depth": 5}
               if obj[2] == '5more':
                  return 'good'
               elif obj[2] == '3':
                  return 'acc'
               elif obj[2] == '4':
                  return 'good'
               elif obj[2] == '2':
                  return 'acc'
               else:
                  return 'acc'
            else:
               return 'good'
         elif obj[5] == 'low':
            return 'unacc'
         elif obj[5] == 'high':
            # {"feature": "4", "instances": 9, "metric_value": 9.2376, "depth": 4}
            if obj[4] == 'small':
               return 'good'
            elif obj[4] == 'big':
               # {"feature": "3", "instances": 4, "metric_value": 4.8284, "depth": 5}
               if obj[3] == '2':
                  return 'unacc'
               elif obj[3] == '4':
                  return 'vgood'
               elif obj[3] == 'more':
                  return 'vgood'
               else:
                  return 'vgood'
            elif obj[4] == 'med':
               return 'unacc'
            else:
               return 'unacc'
         else:
            return 'good'
      else:
         return 'unacc'
   elif obj[0] == 'med':
      # {"feature": "1", "instances": 165, "metric_value": 41.3604, "depth": 2}
      if obj[1] == 'med':
         # {"feature": "3", "instances": 45, "metric_value": 15.1471, "depth": 3}
         if obj[3] == '4':
            # {"feature": "5", "instances": 17, "metric_value": 13.5573, "depth": 4}
            if obj[5] == 'med':
               return 'acc'
            elif obj[5] == 'high':
               # {"feature": "2", "instances": 6, "metric_value": 4.2307, "depth": 5}
               if obj[2] == '4':
                  # {"feature": "4", "instances": 3, "metric_value": 4.2426, "depth": 6}
                  if obj[4] == 'small':
                     return 'acc'
                  elif obj[4] == 'big':
                     return 'vgood'
                  elif obj[4] == 'med':
                     return 'vgood'
                  else:
                     return 'vgood'
               elif obj[2] == '2':
                  return 'acc'
               elif obj[2] == '5more':
                  return 'vgood'
               else:
                  return 'vgood'
            elif obj[5] == 'low':
               return 'unacc'
            else:
               return 'unacc'
         elif obj[3] == '2':
            return 'unacc'
         elif obj[3] == 'more':
            # {"feature": "5", "instances": 13, "metric_value": 7.4026, "depth": 4}
            if obj[5] == 'high':
               # {"feature": "4", "instances": 7, "metric_value": 6.3094, "depth": 5}
               if obj[4] == 'small':
                  # {"feature": "2", "instances": 3, "metric_value": 4.2426, "depth": 6}
                  if obj[2] == '2':
                     return 'unacc'
                  elif obj[2] == '4':
                     return 'acc'
                  elif obj[2] == '5more':
                     return 'acc'
                  else:
                     return 'acc'
               elif obj[4] == 'med':
                  # {"feature": "2", "instances": 3, "metric_value": 4.2426, "depth": 6}
                  if obj[2] == '2':
                     return 'acc'
                  elif obj[2] == '3':
                     return 'vgood'
                  elif obj[2] == '5more':
                     return 'vgood'
                  else:
                     return 'vgood'
               elif obj[4] == 'big':
                  return 'vgood'
               else:
                  return 'vgood'
            elif obj[5] == 'low':
               return 'unacc'
            else:
               return 'unacc'
         else:
            return 'unacc'
      elif obj[1] == 'vhigh':
         # {"feature": "5", "instances": 42, "metric_value": 8.4744, "depth": 3}
         if obj[5] == 'high':
            # {"feature": "3", "instances": 16, "metric_value": 8.6633, "depth": 4}
            if obj[3] == 'more':
               # {"feature": "2", "instances": 7, "metric_value": 4.8165, "depth": 5}
               if obj[2] == '2':
                  # {"feature": "4", "instances": 3, "metric_value": 4.2426, "depth": 6}
                  if obj[4] == 'big':
                     return 'acc'
                  elif obj[4] == 'med':
                     return 'acc'
                  elif obj[4] == 'small':
                     return 'unacc'
                  else:
                     return 'unacc'
               elif obj[2] == '5more':
                  return 'acc'
               elif obj[2] == '4':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[3] == '2':
               return 'unacc'
            elif obj[3] == '4':
               return 'acc'
            else:
               return 'acc'
         elif obj[5] == 'low':
            return 'unacc'
         elif obj[5] == 'med':
            # {"feature": "2", "instances": 13, "metric_value": 8.4283, "depth": 4}
            if obj[2] == '2':
               return 'unacc'
            elif obj[2] == '4':
               return 'unacc'
            elif obj[2] == '3':
               # {"feature": "4", "instances": 3, "metric_value": 3.4142, "depth": 5}
               if obj[4] == 'big':
                  return 'acc'
               elif obj[4] == 'med':
                  return 'unacc'
               else:
                  return 'unacc'
            elif obj[2] == '5more':
               return 'acc'
            else:
               return 'acc'
         else:
            return 'unacc'
      elif obj[1] == 'high':
         # {"feature": "5", "instances": 41, "metric_value": 6.4114, "depth": 3}
         if obj[5] == 'high':
            # {"feature": "3", "instances": 17, "metric_value": 8.62, "depth": 4}
            if obj[3] == '2':
               return 'unacc'
            elif obj[3] == '4':
               return 'acc'
            elif obj[3] == 'more':
               # {"feature": "2", "instances": 4, "metric_value": 4.8284, "depth": 5}
               if obj[2] == '3':
                  return 'acc'
               elif obj[2] == '2':
                  return 'unacc'
               elif obj[2] == '5more':
                  return 'acc'
               else:
                  return 'acc'
            else:
               return 'acc'
         elif obj[5] == 'med':
            # {"feature": "2", "instances": 15, "metric_value": 5.4609, "depth": 4}
            if obj[2] == '5more':
               # {"feature": "3", "instances": 5, "metric_value": 5.4142, "depth": 5}
               if obj[3] == 'more':
                  return 'acc'
               elif obj[3] == '2':
                  return 'unacc'
               elif obj[3] == '4':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[2] == '2':
               return 'unacc'
            elif obj[2] == '4':
               # {"feature": "3", "instances": 4, "metric_value": 4.8284, "depth": 5}
               if obj[3] == '2':
                  return 'unacc'
               elif obj[3] == 'more':
                  return 'acc'
               elif obj[3] == '4':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[2] == '3':
               return 'unacc'
            else:
               return 'unacc'
         elif obj[5] == 'low':
            return 'unacc'
         else:
            return 'unacc'
      elif obj[1] == 'low':
         # {"feature": "5", "instances": 37, "metric_value": 16.9491, "depth": 3}
         if obj[5] == 'med':
            # {"feature": "3", "instances": 18, "metric_value": 10.0775, "depth": 4}
            if obj[3] == '4':
               # {"feature": "4", "instances": 8, "metric_value": 6.6921, "depth": 5}
               if obj[4] == 'big':
                  return 'good'
               elif obj[4] == 'small':
                  return 'acc'
               elif obj[4] == 'med':
                  return 'good'
               else:
                  return 'good'
            elif obj[3] == '2':
               return 'unacc'
            elif obj[3] == 'more':
               # {"feature": "2", "instances": 4, "metric_value": 6.2518, "depth": 5}
               if obj[2] == '4':
                  # {"feature": "4", "instances": 2, "metric_value": 2.8284, "depth": 6}
                  if obj[4] == 'med':
                     return 'good'
                  elif obj[4] == 'small':
                     return 'acc'
                  else:
                     return 'acc'
               elif obj[2] == '2':
                  return 'unacc'
               elif obj[2] == '3':
                  return 'acc'
               else:
                  return 'acc'
            else:
               return 'acc'
         elif obj[5] == 'high':
            # {"feature": "2", "instances": 11, "metric_value": 9.1978, "depth": 4}
            if obj[2] == '2':
               # {"feature": "4", "instances": 5, "metric_value": 5.5754, "depth": 5}
               if obj[4] == 'med':
                  # {"feature": "3", "instances": 2, "metric_value": 2.8284, "depth": 6}
                  if obj[3] == '2':
                     return 'unacc'
                  elif obj[3] == 'more':
                     return 'good'
                  else:
                     return 'good'
               elif obj[4] == 'small':
                  # {"feature": "3", "instances": 2, "metric_value": 2.8284, "depth": 6}
                  if obj[3] == 'more':
                     return 'unacc'
                  elif obj[3] == '4':
                     return 'good'
                  else:
                     return 'good'
               elif obj[4] == 'big':
                  return 'vgood'
               else:
                  return 'vgood'
            elif obj[2] == '3':
               return 'vgood'
            elif obj[2] == '5more':
               return 'vgood'
            elif obj[2] == '4':
               # {"feature": "3", "instances": 2, "metric_value": 2.8284, "depth": 5}
               if obj[3] == 'more':
                  return 'vgood'
               elif obj[3] == '2':
                  return 'unacc'
               else:
                  return 'unacc'
            else:
               return 'vgood'
         elif obj[5] == 'low':
            return 'unacc'
         else:
            return 'unacc'
      else:
         return 'unacc'
   elif obj[0] == 'high':
      # {"feature": "2", "instances": 164, "metric_value": 20.6623, "depth": 2}
      if obj[2] == '5more':
         # {"feature": "1", "instances": 44, "metric_value": 10.5786, "depth": 3}
         if obj[1] == 'vhigh':
            return 'unacc'
         elif obj[1] == 'high':
            # {"feature": "3", "instances": 9, "metric_value": 5.6449, "depth": 4}
            if obj[3] == '2':
               return 'unacc'
            elif obj[3] == 'more':
               # {"feature": "5", "instances": 3, "metric_value": 4.2426, "depth": 5}
               if obj[5] == 'high':
                  return 'acc'
               elif obj[5] == 'med':
                  return 'unacc'
               elif obj[5] == 'low':
                  return 'unacc'
               else:
                  return 'unacc'
            elif obj[3] == '4':
               return 'acc'
            else:
               return 'acc'
         elif obj[1] == 'med':
            # {"feature": "5", "instances": 8, "metric_value": 5.4142, "depth": 4}
            if obj[5] == 'med':
               # {"feature": "3", "instances": 4, "metric_value": 2.0, "depth": 5}
               if obj[3] == 'more':
                  # {"feature": "4", "instances": 2, "metric_value": 2.8284, "depth": 6}
                  if obj[4] == 'med':
                     return 'acc'
                  elif obj[4] == 'small':
                     return 'unacc'
                  else:
                     return 'unacc'
               elif obj[3] == '2':
                  return 'unacc'
               else:
                  return 'unacc'
            elif obj[5] == 'high':
               return 'acc'
            elif obj[5] == 'low':
               return 'unacc'
            else:
               return 'unacc'
         elif obj[1] == 'low':
            # {"feature": "5", "instances": 8, "metric_value": 5.266, "depth": 4}
            if obj[5] == 'low':
               return 'unacc'
            elif obj[5] == 'med':
               # {"feature": "4", "instances": 3, "metric_value": 4.2426, "depth": 5}
               if obj[4] == 'big':
                  return 'acc'
               elif obj[4] == 'med':
                  return 'acc'
               elif obj[4] == 'small':
                  return 'unacc'
               else:
                  return 'unacc'
            elif obj[5] == 'high':
               return 'unacc'
            else:
               return 'unacc'
         else:
            return 'unacc'
      elif obj[2] == '4':
         # {"feature": "1", "instances": 43, "metric_value": 10.235, "depth": 3}
         if obj[1] == 'vhigh':
            return 'unacc'
         elif obj[1] == 'low':
            # {"feature": "4", "instances": 10, "metric_value": 4.6802, "depth": 4}
            if obj[4] == 'med':
               # {"feature": "3", "instances": 4, "metric_value": 4.8284, "depth": 5}
               if obj[3] == '2':
                  return 'unacc'
               elif obj[3] == 'more':
                  return 'unacc'
               elif obj[3] == '4':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[4] == 'big':
               return 'unacc'
            elif obj[4] == 'small':
               # {"feature": "3", "instances": 3, "metric_value": 1.4142, "depth": 5}
               if obj[3] == 'more':
                  # {"feature": "5", "instances": 2, "metric_value": 2.8284, "depth": 6}
                  if obj[5] == 'med':
                     return 'unacc'
                  elif obj[5] == 'high':
                     return 'acc'
                  else:
                     return 'acc'
               elif obj[3] == '2':
                  return 'unacc'
               else:
                  return 'unacc'
            else:
               return 'unacc'
         elif obj[1] == 'med':
            # {"feature": "3", "instances": 10, "metric_value": 5.6948, "depth": 4}
            if obj[3] == '2':
               return 'unacc'
            elif obj[3] == '4':
               # {"feature": "4", "instances": 3, "metric_value": 1.4142, "depth": 5}
               if obj[4] == 'small':
                  # {"feature": "5", "instances": 2, "metric_value": 2.8284, "depth": 6}
                  if obj[5] == 'high':
                     return 'acc'
                  elif obj[5] == 'med':
                     return 'unacc'
                  else:
                     return 'unacc'
               elif obj[4] == 'med':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[3] == 'more':
               return 'acc'
            else:
               return 'acc'
         elif obj[1] == 'high':
            # {"feature": "5", "instances": 9, "metric_value": 4.6325, "depth": 4}
            if obj[5] == 'med':
               # {"feature": "3", "instances": 5, "metric_value": 5.4142, "depth": 5}
               if obj[3] == '2':
                  return 'unacc'
               elif obj[3] == '4':
                  return 'acc'
               elif obj[3] == 'more':
                  return 'unacc'
               else:
                  return 'unacc'
            elif obj[5] == 'high':
               return 'acc'
            elif obj[5] == 'low':
               return 'unacc'
            else:
               return 'unacc'
         else:
            return 'unacc'
      elif obj[2] == '2':
         # {"feature": "5", "instances": 42, "metric_value": 11.1895, "depth": 3}
         if obj[5] == 'low':
            return 'unacc'
         elif obj[5] == 'med':
            # {"feature": "1", "instances": 14, "metric_value": 9.1416, "depth": 4}
            if obj[1] == 'med':
               # {"feature": "4", "instances": 4, "metric_value": 4.8284, "depth": 5}
               if obj[4] == 'med':
                  return 'unacc'
               elif obj[4] == 'small':
                  return 'unacc'
               elif obj[4] == 'big':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[1] == 'high':
               return 'unacc'
            elif obj[1] == 'vhigh':
               return 'unacc'
            elif obj[1] == 'low':
               return 'unacc'
            else:
               return 'unacc'
         elif obj[5] == 'high':
            # {"feature": "3", "instances": 13, "metric_value": 6.5701, "depth": 4}
            if obj[3] == '4':
               return 'acc'
            elif obj[3] == '2':
               return 'unacc'
            elif obj[3] == 'more':
               # {"feature": "4", "instances": 2, "metric_value": 2.8284, "depth": 5}
               if obj[4] == 'big':
                  return 'acc'
               elif obj[4] == 'small':
                  return 'unacc'
               else:
                  return 'unacc'
            else:
               return 'acc'
         else:
            return 'acc'
      elif obj[2] == '3':
         # {"feature": "1", "instances": 35, "metric_value": 8.978, "depth": 3}
         if obj[1] == 'high':
            # {"feature": "5", "instances": 13, "metric_value": 7.5542, "depth": 4}
            if obj[5] == 'med':
               # {"feature": "4", "instances": 5, "metric_value": 5.4142, "depth": 5}
               if obj[4] == 'small':
                  return 'unacc'
               elif obj[4] == 'med':
                  return 'unacc'
               elif obj[4] == 'big':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[5] == 'high':
               return 'acc'
            elif obj[5] == 'low':
               return 'unacc'
            else:
               return 'unacc'
         elif obj[1] == 'low':
            # {"feature": "5", "instances": 11, "metric_value": 6.4734, "depth": 4}
            if obj[5] == 'low':
               return 'unacc'
            elif obj[5] == 'med':
               return 'unacc'
            elif obj[5] == 'high':
               # {"feature": "3", "instances": 3, "metric_value": 3.4142, "depth": 5}
               if obj[3] == '4':
                  return 'acc'
               elif obj[3] == '2':
                  return 'unacc'
               else:
                  return 'unacc'
            else:
               return 'acc'
         elif obj[1] == 'vhigh':
            return 'unacc'
         elif obj[1] == 'med':
            # {"feature": "5", "instances": 3, "metric_value": 3.4142, "depth": 4}
            if obj[5] == 'med':
               return 'acc'
            elif obj[5] == 'low':
               return 'unacc'
            else:
               return 'unacc'
         else:
            return 'acc'
      else:
         return 'unacc'
   else:
      return 'unacc'
