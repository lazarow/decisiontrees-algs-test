def findDecision(obj): #obj[0]: 0, obj[1]: 1, obj[2]: 2, obj[3]: 3, obj[4]: 4, obj[5]: 5
   # {"feature": "5", "instances": 691, "metric_value": 1.2247, "depth": 1}
   if obj[5] == 'med':
      # {"feature": "3", "instances": 250, "metric_value": 1.1812, "depth": 2}
      if obj[3] == '4':
         # {"feature": "0", "instances": 90, "metric_value": 1.3689, "depth": 3}
         if obj[0] == 'med':
            # {"feature": "1", "instances": 24, "metric_value": 1.3965, "depth": 4}
            if obj[1] == 'low':
               # {"feature": "4", "instances": 8, "metric_value": 0.9544, "depth": 5}
               if obj[4] == 'big':
                  return 'good'
               elif obj[4] == 'small':
                  return 'acc'
               elif obj[4] == 'med':
                  return 'good'
               else:
                  return 'good'
            elif obj[1] == 'med':
               return 'acc'
            elif obj[1] == 'vhigh':
               # {"feature": "4", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[4] == 'med':
                  return 'unacc'
               elif obj[4] == 'big':
                  return 'acc'
               elif obj[4] == 'small':
                  return 'unacc'
               else:
                  return 'unacc'
            elif obj[1] == 'high':
               # {"feature": "2", "instances": 4, "metric_value": 1.0, "depth": 5}
               if obj[2] == '2':
                  return 'unacc'
               elif obj[2] == '5more':
                  return 'acc'
               elif obj[2] == '4':
                  return 'acc'
               else:
                  return 'acc'
            else:
               return 'unacc'
         elif obj[0] == 'vhigh':
            # {"feature": "1", "instances": 24, "metric_value": 0.7383, "depth": 4}
            if obj[1] == 'vhigh':
               return 'unacc'
            elif obj[1] == 'high':
               return 'unacc'
            elif obj[1] == 'med':
               # {"feature": "2", "instances": 6, "metric_value": 1.0, "depth": 5}
               if obj[2] == '4':
                  # {"feature": "4", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[4] == 'big':
                     return 'acc'
                  elif obj[4] == 'small':
                     return 'unacc'
                  else:
                     return 'unacc'
               elif obj[2] == '5more':
                  return 'acc'
               elif obj[2] == '3':
                  return 'unacc'
               else:
                  return 'unacc'
            elif obj[1] == 'low':
               # {"feature": "4", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[4] == 'small':
                  return 'unacc'
               elif obj[4] == 'big':
                  return 'acc'
               else:
                  return 'acc'
            else:
               return 'unacc'
         elif obj[0] == 'high':
            # {"feature": "4", "instances": 23, "metric_value": 0.9656, "depth": 4}
            if obj[4] == 'med':
               # {"feature": "2", "instances": 11, "metric_value": 0.994, "depth": 5}
               if obj[2] == '4':
                  # {"feature": "1", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[1] == 'high':
                     return 'acc'
                  elif obj[1] == 'vhigh':
                     return 'unacc'
                  elif obj[1] == 'med':
                     return 'acc'
                  elif obj[1] == 'low':
                     return 'acc'
                  else:
                     return 'acc'
               elif obj[2] == '5more':
                  # {"feature": "1", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[1] == 'vhigh':
                     return 'unacc'
                  elif obj[1] == 'high':
                     return 'acc'
                  elif obj[1] == 'low':
                     return 'acc'
                  else:
                     return 'acc'
               elif obj[2] == '2':
                  return 'unacc'
               elif obj[2] == '3':
                  return 'unacc'
               else:
                  return 'unacc'
            elif obj[4] == 'small':
               return 'unacc'
            elif obj[4] == 'big':
               # {"feature": "1", "instances": 5, "metric_value": 0.7219, "depth": 5}
               if obj[1] == 'high':
                  return 'acc'
               elif obj[1] == 'vhigh':
                  return 'unacc'
               elif obj[1] == 'med':
                  return 'acc'
               elif obj[1] == 'low':
                  return 'acc'
               else:
                  return 'acc'
            else:
               return 'acc'
         elif obj[0] == 'low':
            # {"feature": "1", "instances": 19, "metric_value": 1.1897, "depth": 4}
            if obj[1] == 'med':
               # {"feature": "4", "instances": 6, "metric_value": 0.9183, "depth": 5}
               if obj[4] == 'small':
                  return 'acc'
               elif obj[4] == 'med':
                  # {"feature": "2", "instances": 2, "metric_value": 1.0, "depth": 6}
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
            elif obj[1] == 'vhigh':
               # {"feature": "4", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[4] == 'small':
                  return 'unacc'
               elif obj[4] == 'big':
                  return 'acc'
               elif obj[4] == 'med':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[1] == 'low':
               # {"feature": "2", "instances": 4, "metric_value": 1.0, "depth": 5}
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
            elif obj[1] == 'high':
               return 'acc'
            else:
               return 'acc'
         else:
            return 'acc'
      elif obj[3] == '2':
         return 'unacc'
      elif obj[3] == 'more':
         # {"feature": "0", "instances": 74, "metric_value": 1.3557, "depth": 3}
         if obj[0] == 'low':
            # {"feature": "1", "instances": 23, "metric_value": 1.2143, "depth": 4}
            if obj[1] == 'low':
               # {"feature": "4", "instances": 7, "metric_value": 0.9852, "depth": 5}
               if obj[4] == 'med':
                  # {"feature": "2", "instances": 3, "metric_value": 0.9183, "depth": 6}
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
            elif obj[1] == 'vhigh':
               # {"feature": "4", "instances": 7, "metric_value": 0.8631, "depth": 5}
               if obj[4] == 'big':
                  return 'acc'
               elif obj[4] == 'med':
                  # {"feature": "2", "instances": 3, "metric_value": 0.9183, "depth": 6}
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
            elif obj[1] == 'high':
               return 'acc'
            elif obj[1] == 'med':
               # {"feature": "4", "instances": 3, "metric_value": 0.9183, "depth": 5}
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
         elif obj[0] == 'vhigh':
            # {"feature": "1", "instances": 20, "metric_value": 0.8813, "depth": 4}
            if obj[1] == 'low':
               # {"feature": "4", "instances": 6, "metric_value": 0.9183, "depth": 5}
               if obj[4] == 'med':
                  return 'acc'
               elif obj[4] == 'small':
                  return 'unacc'
               elif obj[4] == 'big':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[1] == 'high':
               return 'unacc'
            elif obj[1] == 'med':
               # {"feature": "4", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[4] == 'small':
                  return 'unacc'
               elif obj[4] == 'med':
                  # {"feature": "2", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[2] == '2':
                     return 'unacc'
                  elif obj[2] == '4':
                     return 'acc'
                  else:
                     return 'acc'
               elif obj[4] == 'big':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[1] == 'vhigh':
               return 'unacc'
            else:
               return 'unacc'
         elif obj[0] == 'high':
            # {"feature": "4", "instances": 17, "metric_value": 0.7871, "depth": 4}
            if obj[4] == 'small':
               return 'unacc'
            elif obj[4] == 'med':
               # {"feature": "2", "instances": 6, "metric_value": 0.9183, "depth": 5}
               if obj[2] == '4':
                  # {"feature": "1", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[1] == 'med':
                     return 'acc'
                  elif obj[1] == 'vhigh':
                     return 'unacc'
                  else:
                     return 'unacc'
               elif obj[2] == '2':
                  return 'unacc'
               elif obj[2] == '5more':
                  return 'acc'
               elif obj[2] == '3':
                  return 'unacc'
               else:
                  return 'unacc'
            elif obj[4] == 'big':
               return 'acc'
            else:
               return 'acc'
         elif obj[0] == 'med':
            # {"feature": "2", "instances": 14, "metric_value": 1.2958, "depth": 4}
            if obj[2] == '2':
               return 'unacc'
            elif obj[2] == '4':
               # {"feature": "1", "instances": 4, "metric_value": 1.5, "depth": 5}
               if obj[1] == 'low':
                  # {"feature": "4", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[4] == 'med':
                     return 'good'
                  elif obj[4] == 'small':
                     return 'acc'
                  else:
                     return 'acc'
               elif obj[1] == 'vhigh':
                  return 'unacc'
               elif obj[1] == 'high':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[2] == '3':
               # {"feature": "1", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[1] == 'vhigh':
                  return 'acc'
               elif obj[1] == 'high':
                  return 'unacc'
               elif obj[1] == 'low':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[2] == '5more':
               return 'acc'
            else:
               return 'acc'
         else:
            return 'acc'
      else:
         return 'unacc'
   elif obj[5] == 'high':
      # {"feature": "3", "instances": 234, "metric_value": 1.6219, "depth": 2}
      if obj[3] == '4':
         # {"feature": "0", "instances": 79, "metric_value": 1.6349, "depth": 3}
         if obj[0] == 'low':
            # {"feature": "1", "instances": 23, "metric_value": 1.5204, "depth": 4}
            if obj[1] == 'vhigh':
               return 'acc'
            elif obj[1] == 'high':
               # {"feature": "4", "instances": 6, "metric_value": 1.0, "depth": 5}
               if obj[4] == 'big':
                  return 'vgood'
               elif obj[4] == 'med':
                  return 'acc'
               elif obj[4] == 'small':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[1] == 'med':
               # {"feature": "4", "instances": 6, "metric_value": 0.9183, "depth": 5}
               if obj[4] == 'small':
                  return 'good'
               elif obj[4] == 'big':
                  return 'vgood'
               elif obj[4] == 'med':
                  return 'good'
               else:
                  return 'good'
            elif obj[1] == 'low':
               # {"feature": "2", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[2] == '5more':
                  return 'good'
               elif obj[2] == '2':
                  return 'good'
               elif obj[2] == '3':
                  return 'vgood'
               else:
                  return 'vgood'
            else:
               return 'good'
         elif obj[0] == 'high':
            # {"feature": "1", "instances": 22, "metric_value": 0.9024, "depth": 4}
            if obj[1] == 'vhigh':
               return 'unacc'
            elif obj[1] == 'high':
               return 'acc'
            elif obj[1] == 'low':
               return 'acc'
            elif obj[1] == 'med':
               return 'acc'
            else:
               return 'acc'
         elif obj[0] == 'med':
            # {"feature": "1", "instances": 19, "metric_value": 1.105, "depth": 4}
            if obj[1] == 'med':
               # {"feature": "4", "instances": 6, "metric_value": 1.0, "depth": 5}
               if obj[4] == 'small':
                  return 'acc'
               elif obj[4] == 'med':
                  # {"feature": "2", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[2] == '2':
                     return 'acc'
                  elif obj[2] == '4':
                     return 'vgood'
                  else:
                     return 'vgood'
               elif obj[4] == 'big':
                  return 'vgood'
               else:
                  return 'vgood'
            elif obj[1] == 'high':
               return 'acc'
            elif obj[1] == 'vhigh':
               return 'acc'
            elif obj[1] == 'low':
               # {"feature": "2", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[2] == '5more':
                  return 'vgood'
               elif obj[2] == '3':
                  return 'vgood'
               elif obj[2] == '2':
                  return 'good'
               else:
                  return 'good'
            else:
               return 'vgood'
         elif obj[0] == 'vhigh':
            # {"feature": "1", "instances": 15, "metric_value": 0.971, "depth": 4}
            if obj[1] == 'high':
               return 'unacc'
            elif obj[1] == 'vhigh':
               return 'unacc'
            elif obj[1] == 'med':
               return 'acc'
            elif obj[1] == 'low':
               return 'acc'
            else:
               return 'acc'
         else:
            return 'unacc'
      elif obj[3] == 'more':
         # {"feature": "0", "instances": 79, "metric_value": 1.7019, "depth": 3}
         if obj[0] == 'med':
            # {"feature": "1", "instances": 24, "metric_value": 1.6403, "depth": 4}
            if obj[1] == 'med':
               # {"feature": "4", "instances": 7, "metric_value": 1.4488, "depth": 5}
               if obj[4] == 'small':
                  # {"feature": "2", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[2] == '2':
                     return 'unacc'
                  elif obj[2] == '4':
                     return 'acc'
                  elif obj[2] == '5more':
                     return 'acc'
                  else:
                     return 'acc'
               elif obj[4] == 'med':
                  # {"feature": "2", "instances": 3, "metric_value": 0.9183, "depth": 6}
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
            elif obj[1] == 'vhigh':
               # {"feature": "4", "instances": 7, "metric_value": 0.5917, "depth": 5}
               if obj[4] == 'big':
                  return 'acc'
               elif obj[4] == 'med':
                  return 'acc'
               elif obj[4] == 'small':
                  # {"feature": "2", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[2] == '2':
                     return 'unacc'
                  elif obj[2] == '5more':
                     return 'acc'
                  else:
                     return 'acc'
               else:
                  return 'unacc'
            elif obj[1] == 'low':
               # {"feature": "4", "instances": 6, "metric_value": 1.2516, "depth": 5}
               if obj[4] == 'med':
                  # {"feature": "2", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[2] == '3':
                     return 'vgood'
                  elif obj[2] == '5more':
                     return 'vgood'
                  elif obj[2] == '4':
                     return 'vgood'
                  elif obj[2] == '2':
                     return 'good'
                  else:
                     return 'good'
               elif obj[4] == 'small':
                  return 'unacc'
               elif obj[4] == 'big':
                  return 'vgood'
               else:
                  return 'vgood'
            elif obj[1] == 'high':
               # {"feature": "2", "instances": 4, "metric_value": 0.8113, "depth": 5}
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
         elif obj[0] == 'low':
            # {"feature": "1", "instances": 22, "metric_value": 1.5022, "depth": 4}
            if obj[1] == 'med':
               # {"feature": "4", "instances": 7, "metric_value": 0.8631, "depth": 5}
               if obj[4] == 'med':
                  return 'vgood'
               elif obj[4] == 'big':
                  return 'vgood'
               elif obj[4] == 'small':
                  return 'good'
               else:
                  return 'good'
            elif obj[1] == 'vhigh':
               return 'acc'
            elif obj[1] == 'high':
               # {"feature": "4", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[4] == 'med':
                  return 'vgood'
               elif obj[4] == 'small':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[1] == 'low':
               # {"feature": "2", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[2] == '3':
                  return 'good'
               elif obj[2] == '5more':
                  return 'good'
               elif obj[2] == '2':
                  return 'vgood'
               else:
                  return 'vgood'
            else:
               return 'good'
         elif obj[0] == 'vhigh':
            # {"feature": "1", "instances": 19, "metric_value": 0.9495, "depth": 4}
            if obj[1] == 'low':
               return 'acc'
            elif obj[1] == 'med':
               return 'acc'
            elif obj[1] == 'vhigh':
               return 'unacc'
            elif obj[1] == 'high':
               return 'unacc'
            else:
               return 'unacc'
         elif obj[0] == 'high':
            # {"feature": "1", "instances": 14, "metric_value": 1.0, "depth": 4}
            if obj[1] == 'vhigh':
               return 'unacc'
            elif obj[1] == 'high':
               return 'acc'
            elif obj[1] == 'low':
               # {"feature": "2", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[2] == '2':
                  # {"feature": "4", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[4] == 'big':
                     return 'acc'
                  elif obj[4] == 'small':
                     return 'unacc'
                  else:
                     return 'unacc'
               elif obj[2] == '4':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[1] == 'med':
               return 'acc'
            else:
               return 'acc'
         else:
            return 'acc'
      elif obj[3] == '2':
         return 'unacc'
      else:
         return 'unacc'
   elif obj[5] == 'low':
      return 'unacc'
   else:
      return 'unacc'
