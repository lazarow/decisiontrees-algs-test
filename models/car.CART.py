def findDecision(obj): #obj[0]: 0, obj[1]: 1, obj[2]: 2, obj[3]: 3, obj[4]: 4, obj[5]: 5
   # {"feature": "3", "instances": 691, "metric_value": 0.3883, "depth": 1}
   if obj[3] == '4':
      # {"feature": "5", "instances": 243, "metric_value": 0.4141, "depth": 2}
      if obj[5] == 'med':
         # {"feature": "0", "instances": 90, "metric_value": 0.4631, "depth": 3}
         if obj[0] == 'med':
            # {"feature": "1", "instances": 24, "metric_value": 0.3396, "depth": 4}
            if obj[1] == 'low':
               # {"feature": "4", "instances": 8, "metric_value": 0.0, "depth": 5}
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
               # {"feature": "4", "instances": 5, "metric_value": 0.0, "depth": 5}
               if obj[4] == 'med':
                  return 'unacc'
               elif obj[4] == 'big':
                  return 'acc'
               elif obj[4] == 'small':
                  return 'unacc'
               else:
                  return 'unacc'
            elif obj[1] == 'high':
               # {"feature": "2", "instances": 4, "metric_value": 0.0, "depth": 5}
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
            # {"feature": "1", "instances": 24, "metric_value": 0.225, "depth": 4}
            if obj[1] == 'vhigh':
               return 'unacc'
            elif obj[1] == 'high':
               return 'unacc'
            elif obj[1] == 'med':
               # {"feature": "2", "instances": 6, "metric_value": 0.1667, "depth": 5}
               if obj[2] == '4':
                  # {"feature": "4", "instances": 2, "metric_value": 0.0, "depth": 6}
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
               # {"feature": "4", "instances": 5, "metric_value": 0.0, "depth": 5}
               if obj[4] == 'small':
                  return 'unacc'
               elif obj[4] == 'big':
                  return 'acc'
               else:
                  return 'acc'
            else:
               return 'unacc'
         elif obj[0] == 'high':
            # {"feature": "4", "instances": 23, "metric_value": 0.3067, "depth": 4}
            if obj[4] == 'med':
               # {"feature": "2", "instances": 11, "metric_value": 0.2576, "depth": 5}
               if obj[2] == '4':
                  # {"feature": "1", "instances": 4, "metric_value": 0.0, "depth": 6}
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
                  # {"feature": "1", "instances": 3, "metric_value": 0.0, "depth": 6}
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
               # {"feature": "1", "instances": 5, "metric_value": 0.0, "depth": 5}
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
            # {"feature": "2", "instances": 19, "metric_value": 0.3614, "depth": 4}
            if obj[2] == '5more':
               # {"feature": "1", "instances": 6, "metric_value": 0.3333, "depth": 5}
               if obj[1] == 'vhigh':
                  # {"feature": "4", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[4] == 'small':
                     return 'unacc'
                  elif obj[4] == 'med':
                     return 'acc'
                  else:
                     return 'acc'
               elif obj[1] == 'med':
                  # {"feature": "4", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[4] == 'small':
                     return 'acc'
                  elif obj[4] == 'big':
                     return 'good'
                  else:
                     return 'good'
               elif obj[1] == 'low':
                  return 'good'
               elif obj[1] == 'high':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[2] == '4':
               # {"feature": "1", "instances": 5, "metric_value": 0.2, "depth": 5}
               if obj[1] == 'med':
                  # {"feature": "4", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[4] == 'small':
                     return 'acc'
                  elif obj[4] == 'med':
                     return 'good'
                  else:
                     return 'good'
               elif obj[1] == 'vhigh':
                  return 'unacc'
               elif obj[1] == 'high':
                  return 'acc'
               elif obj[1] == 'low':
                  return 'good'
               else:
                  return 'good'
            elif obj[2] == '3':
               return 'acc'
            elif obj[2] == '2':
               return 'acc'
            else:
               return 'acc'
         else:
            return 'acc'
      elif obj[5] == 'high':
         # {"feature": "0", "instances": 79, "metric_value": 0.5075, "depth": 3}
         if obj[0] == 'low':
            # {"feature": "1", "instances": 23, "metric_value": 0.3043, "depth": 4}
            if obj[1] == 'vhigh':
               return 'acc'
            elif obj[1] == 'high':
               # {"feature": "4", "instances": 6, "metric_value": 0.0, "depth": 5}
               if obj[4] == 'big':
                  return 'vgood'
               elif obj[4] == 'med':
                  return 'acc'
               elif obj[4] == 'small':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[1] == 'med':
               # {"feature": "4", "instances": 6, "metric_value": 0.0, "depth": 5}
               if obj[4] == 'small':
                  return 'good'
               elif obj[4] == 'big':
                  return 'vgood'
               elif obj[4] == 'med':
                  return 'good'
               else:
                  return 'good'
            elif obj[1] == 'low':
               # {"feature": "2", "instances": 3, "metric_value": 0.0, "depth": 5}
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
            # {"feature": "1", "instances": 22, "metric_value": 0.0, "depth": 4}
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
            # {"feature": "1", "instances": 19, "metric_value": 0.2281, "depth": 4}
            if obj[1] == 'med':
               # {"feature": "4", "instances": 6, "metric_value": 0.1667, "depth": 5}
               if obj[4] == 'small':
                  return 'acc'
               elif obj[4] == 'med':
                  # {"feature": "2", "instances": 2, "metric_value": 0.0, "depth": 6}
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
               # {"feature": "2", "instances": 3, "metric_value": 0.0, "depth": 5}
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
            # {"feature": "1", "instances": 15, "metric_value": 0.0, "depth": 4}
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
      elif obj[5] == 'low':
         return 'unacc'
      else:
         return 'unacc'
   elif obj[3] == '2':
      return 'unacc'
   elif obj[3] == 'more':
      # {"feature": "5", "instances": 213, "metric_value": 0.4415, "depth": 2}
      if obj[5] == 'high':
         # {"feature": "0", "instances": 79, "metric_value": 0.5696, "depth": 3}
         if obj[0] == 'med':
            # {"feature": "1", "instances": 24, "metric_value": 0.4375, "depth": 4}
            if obj[1] == 'med':
               # {"feature": "4", "instances": 7, "metric_value": 0.381, "depth": 5}
               if obj[4] == 'small':
                  # {"feature": "2", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[2] == '2':
                     return 'unacc'
                  elif obj[2] == '4':
                     return 'acc'
                  elif obj[2] == '5more':
                     return 'acc'
                  else:
                     return 'acc'
               elif obj[4] == 'med':
                  # {"feature": "2", "instances": 3, "metric_value": 0.0, "depth": 6}
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
               # {"feature": "4", "instances": 7, "metric_value": 0.1429, "depth": 5}
               if obj[4] == 'big':
                  return 'acc'
               elif obj[4] == 'med':
                  return 'acc'
               elif obj[4] == 'small':
                  # {"feature": "2", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[2] == '2':
                     return 'unacc'
                  elif obj[2] == '5more':
                     return 'acc'
                  else:
                     return 'acc'
               else:
                  return 'unacc'
            elif obj[1] == 'low':
               # {"feature": "4", "instances": 6, "metric_value": 0.25, "depth": 5}
               if obj[4] == 'med':
                  # {"feature": "2", "instances": 4, "metric_value": 0.0, "depth": 6}
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
               # {"feature": "2", "instances": 4, "metric_value": 0.0, "depth": 5}
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
            # {"feature": "1", "instances": 22, "metric_value": 0.2996, "depth": 4}
            if obj[1] == 'med':
               # {"feature": "4", "instances": 7, "metric_value": 0.0, "depth": 5}
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
               # {"feature": "4", "instances": 5, "metric_value": 0.0, "depth": 5}
               if obj[4] == 'med':
                  return 'vgood'
               elif obj[4] == 'small':
                  return 'acc'
               else:
                  return 'acc'
            elif obj[1] == 'low':
               # {"feature": "2", "instances": 3, "metric_value": 0.0, "depth": 5}
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
            # {"feature": "1", "instances": 19, "metric_value": 0.0, "depth": 4}
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
            # {"feature": "1", "instances": 14, "metric_value": 0.0952, "depth": 4}
            if obj[1] == 'vhigh':
               return 'unacc'
            elif obj[1] == 'high':
               return 'acc'
            elif obj[1] == 'low':
               # {"feature": "2", "instances": 3, "metric_value": 0.3333, "depth": 5}
               if obj[2] == '2':
                  # {"feature": "4", "instances": 2, "metric_value": 0.0, "depth": 6}
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
      elif obj[5] == 'med':
         # {"feature": "0", "instances": 74, "metric_value": 0.4575, "depth": 3}
         if obj[0] == 'low':
            # {"feature": "1", "instances": 23, "metric_value": 0.3313, "depth": 4}
            if obj[1] == 'low':
               # {"feature": "4", "instances": 7, "metric_value": 0.1905, "depth": 5}
               if obj[4] == 'med':
                  # {"feature": "2", "instances": 3, "metric_value": 0.0, "depth": 6}
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
               # {"feature": "4", "instances": 7, "metric_value": 0.1905, "depth": 5}
               if obj[4] == 'big':
                  return 'acc'
               elif obj[4] == 'med':
                  # {"feature": "2", "instances": 3, "metric_value": 0.0, "depth": 6}
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
               # {"feature": "4", "instances": 3, "metric_value": 0.0, "depth": 5}
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
            # {"feature": "1", "instances": 20, "metric_value": 0.2533, "depth": 4}
            if obj[1] == 'low':
               # {"feature": "4", "instances": 6, "metric_value": 0.0, "depth": 5}
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
               # {"feature": "4", "instances": 5, "metric_value": 0.2, "depth": 5}
               if obj[4] == 'small':
                  return 'unacc'
               elif obj[4] == 'med':
                  # {"feature": "2", "instances": 2, "metric_value": 0.0, "depth": 6}
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
            # {"feature": "4", "instances": 17, "metric_value": 0.1569, "depth": 4}
            if obj[4] == 'small':
               return 'unacc'
            elif obj[4] == 'med':
               # {"feature": "2", "instances": 6, "metric_value": 0.1667, "depth": 5}
               if obj[2] == '4':
                  # {"feature": "1", "instances": 2, "metric_value": 0.0, "depth": 6}
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
            # {"feature": "2", "instances": 14, "metric_value": 0.2738, "depth": 4}
            if obj[2] == '2':
               return 'unacc'
            elif obj[2] == '4':
               # {"feature": "1", "instances": 4, "metric_value": 0.25, "depth": 5}
               if obj[1] == 'low':
                  # {"feature": "4", "instances": 2, "metric_value": 0.0, "depth": 6}
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
               # {"feature": "1", "instances": 3, "metric_value": 0.0, "depth": 5}
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
      elif obj[5] == 'low':
         return 'unacc'
      else:
         return 'unacc'
   else:
      return 'unacc'
