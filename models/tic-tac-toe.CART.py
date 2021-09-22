def findDecision(obj): #obj[0]: 0, obj[1]: 1, obj[2]: 2, obj[3]: 3, obj[4]: 4, obj[5]: 5, obj[6]: 6, obj[7]: 7, obj[8]: 8
   # {"feature": "4", "instances": 383, "metric_value": 0.3916, "depth": 1}
   if obj[4] == 'x':
      # {"feature": "0", "instances": 181, "metric_value": 0.2988, "depth": 2}
      if obj[0] == 'o':
         # {"feature": "6", "instances": 71, "metric_value": 0.3362, "depth": 3}
         if obj[6] == 'x':
            # {"feature": "2", "instances": 36, "metric_value": 0.1167, "depth": 4}
            if obj[2] == 'x':
               return 'positive'
            elif obj[2] == 'o':
               # {"feature": "1", "instances": 10, "metric_value": 0.2333, "depth": 5}
               if obj[1] == 'o':
                  return 'negative'
               elif obj[1] == 'x':
                  # {"feature": "5", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[5] == 'x':
                     return 'positive'
                  elif obj[5] == 'b':
                     return 'positive'
                  elif obj[5] == 'o':
                     return 'negative'
                  else:
                     return 'negative'
               elif obj[1] == 'b':
                  # {"feature": "5", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[5] == 'o':
                     return 'negative'
                  elif obj[5] == 'x':
                     return 'positive'
                  else:
                     return 'positive'
               else:
                  return 'negative'
            elif obj[2] == 'b':
               return 'positive'
            else:
               return 'positive'
         elif obj[6] == 'o':
            # {"feature": "3", "instances": 27, "metric_value": 0.216, "depth": 4}
            if obj[3] == 'x':
               # {"feature": "5", "instances": 12, "metric_value": 0.0, "depth": 5}
               if obj[5] == 'x':
                  return 'positive'
               elif obj[5] == 'b':
                  return 'negative'
               elif obj[5] == 'o':
                  return 'negative'
               else:
                  return 'negative'
            elif obj[3] == 'o':
               return 'negative'
            elif obj[3] == 'b':
               # {"feature": "5", "instances": 3, "metric_value": 0.0, "depth": 5}
               if obj[5] == 'x':
                  return 'negative'
               elif obj[5] == 'b':
                  return 'positive'
               else:
                  return 'positive'
            else:
               return 'negative'
         elif obj[6] == 'b':
            return 'positive'
         else:
            return 'positive'
      elif obj[0] == 'x':
         # {"feature": "8", "instances": 60, "metric_value": 0.1944, "depth": 3}
         if obj[8] == 'x':
            return 'positive'
         elif obj[8] == 'o':
            # {"feature": "3", "instances": 24, "metric_value": 0.3287, "depth": 4}
            if obj[3] == 'x':
               # {"feature": "6", "instances": 9, "metric_value": 0.1111, "depth": 5}
               if obj[6] == 'x':
                  return 'positive'
               elif obj[6] == 'o':
                  return 'negative'
               elif obj[6] == 'b':
                  # {"feature": "1", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1] == 'o':
                     return 'positive'
                  elif obj[1] == 'x':
                     return 'negative'
                  else:
                     return 'negative'
               else:
                  return 'positive'
            elif obj[3] == 'o':
               # {"feature": "2", "instances": 9, "metric_value": 0.1481, "depth": 5}
               if obj[2] == 'x':
                  return 'positive'
               elif obj[2] == 'o':
                  # {"feature": "5", "instances": 3, "metric_value": 0.0, "depth": 6}
                  if obj[5] == 'b':
                     return 'positive'
                  elif obj[5] == 'x':
                     return 'positive'
                  elif obj[5] == 'o':
                     return 'negative'
                  else:
                     return 'negative'
               elif obj[2] == 'b':
                  return 'positive'
               else:
                  return 'positive'
            elif obj[3] == 'b':
               # {"feature": "7", "instances": 6, "metric_value": 0.1667, "depth": 5}
               if obj[7] == 'o':
                  return 'negative'
               elif obj[7] == 'x':
                  # {"feature": "1", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1] == 'x':
                     return 'positive'
                  elif obj[1] == 'b':
                     return 'negative'
                  else:
                     return 'negative'
               else:
                  return 'positive'
            else:
               return 'negative'
         elif obj[8] == 'b':
            return 'positive'
         else:
            return 'positive'
      elif obj[0] == 'b':
         # {"feature": "3", "instances": 50, "metric_value": 0.1035, "depth": 3}
         if obj[3] == 'o':
            # {"feature": "7", "instances": 21, "metric_value": 0.0762, "depth": 4}
            if obj[7] == 'x':
               return 'positive'
            elif obj[7] == 'o':
               # {"feature": "1", "instances": 5, "metric_value": 0.2, "depth": 5}
               if obj[1] == 'b':
                  return 'positive'
               elif obj[1] == 'x':
                  # {"feature": "5", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[5] == 'b':
                     return 'positive'
                  elif obj[5] == 'x':
                     return 'negative'
                  else:
                     return 'negative'
               elif obj[1] == 'o':
                  return 'positive'
               else:
                  return 'positive'
            elif obj[7] == 'b':
               return 'positive'
            else:
               return 'positive'
         elif obj[3] == 'x':
            return 'positive'
         elif obj[3] == 'b':
            # {"feature": "1", "instances": 11, "metric_value": 0.1558, "depth": 4}
            if obj[1] == 'x':
               # {"feature": "5", "instances": 7, "metric_value": 0.1429, "depth": 5}
               if obj[5] == 'o':
                  return 'positive'
               elif obj[5] == 'b':
                  return 'positive'
               elif obj[5] == 'x':
                  # {"feature": "2", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[2] == 'b':
                     return 'negative'
                  elif obj[2] == 'o':
                     return 'positive'
                  else:
                     return 'positive'
               else:
                  return 'negative'
            elif obj[1] == 'o':
               return 'positive'
            elif obj[1] == 'b':
               return 'negative'
            else:
               return 'negative'
         else:
            return 'positive'
      else:
         return 'positive'
   elif obj[4] == 'o':
      # {"feature": "8", "instances": 144, "metric_value": 0.4574, "depth": 2}
      if obj[8] == 'x':
         # {"feature": "2", "instances": 70, "metric_value": 0.4205, "depth": 3}
         if obj[2] == 'o':
            # {"feature": "6", "instances": 30, "metric_value": 0.1846, "depth": 4}
            if obj[6] == 'o':
               return 'negative'
            elif obj[6] == 'x':
               # {"feature": "7", "instances": 13, "metric_value": 0.1923, "depth": 5}
               if obj[7] == 'x':
                  return 'positive'
               elif obj[7] == 'o':
                  # {"feature": "5", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[5] == 'x':
                     return 'negative'
                  elif obj[5] == 'o':
                     return 'positive'
                  else:
                     return 'positive'
               elif obj[7] == 'b':
                  # {"feature": "1", "instances": 2, "metric_value": 0.0, "depth": 6}
                  if obj[1] == 'o':
                     return 'positive'
                  elif obj[1] == 'x':
                     return 'negative'
                  else:
                     return 'negative'
               else:
                  return 'positive'
            elif obj[6] == 'b':
               return 'negative'
            else:
               return 'negative'
         elif obj[2] == 'x':
            # {"feature": "5", "instances": 27, "metric_value": 0.1228, "depth": 4}
            if obj[5] == 'x':
               return 'positive'
            elif obj[5] == 'o':
               # {"feature": "3", "instances": 7, "metric_value": 0.0, "depth": 5}
               if obj[3] == 'o':
                  return 'negative'
               elif obj[3] == 'x':
                  return 'negative'
               elif obj[3] == 'b':
                  return 'positive'
               else:
                  return 'positive'
            elif obj[5] == 'b':
               # {"feature": "3", "instances": 5, "metric_value": 0.0, "depth": 5}
               if obj[3] == 'o':
                  return 'positive'
               elif obj[3] == 'b':
                  return 'positive'
               elif obj[3] == 'x':
                  return 'negative'
               else:
                  return 'negative'
            else:
               return 'positive'
         elif obj[2] == 'b':
            # {"feature": "7", "instances": 13, "metric_value": 0.2308, "depth": 4}
            if obj[7] == 'x':
               # {"feature": "6", "instances": 8, "metric_value": 0.0, "depth": 5}
               if obj[6] == 'x':
                  return 'positive'
               elif obj[6] == 'o':
                  return 'negative'
               else:
                  return 'negative'
            elif obj[7] == 'o':
               return 'negative'
            elif obj[7] == 'b':
               return 'negative'
            else:
               return 'negative'
         else:
            return 'negative'
      elif obj[8] == 'o':
         # {"feature": "0", "instances": 46, "metric_value": 0.1978, "depth": 3}
         if obj[0] == 'o':
            return 'negative'
         elif obj[0] == 'x':
            # {"feature": "7", "instances": 20, "metric_value": 0.3394, "depth": 4}
            if obj[7] == 'x':
               # {"feature": "2", "instances": 11, "metric_value": 0.2879, "depth": 5}
               if obj[2] == 'o':
                  # {"feature": "1", "instances": 6, "metric_value": 0.1667, "depth": 6}
                  if obj[1] == 'x':
                     return 'negative'
                  elif obj[1] == 'b':
                     # {"feature": "5", "instances": 2, "metric_value": 0.0, "depth": 7}
                     if obj[5] == 'x':
                        return 'negative'
                     elif obj[5] == 'b':
                        return 'positive'
                     else:
                        return 'positive'
                  else:
                     return 'negative'
               elif obj[2] == 'x':
                  # {"feature": "1", "instances": 4, "metric_value": 0.0, "depth": 6}
                  if obj[1] == 'x':
                     return 'positive'
                  elif obj[1] == 'b':
                     return 'negative'
                  else:
                     return 'negative'
               elif obj[2] == 'b':
                  return 'positive'
               else:
                  return 'positive'
            elif obj[7] == 'b':
               return 'positive'
            elif obj[7] == 'o':
               # {"feature": "1", "instances": 3, "metric_value": 0.0, "depth": 5}
               if obj[1] == 'o':
                  return 'negative'
               elif obj[1] == 'x':
                  return 'positive'
               elif obj[1] == 'b':
                  return 'positive'
               else:
                  return 'positive'
            else:
               return 'positive'
         elif obj[0] == 'b':
            return 'negative'
         else:
            return 'negative'
      elif obj[8] == 'b':
         # {"feature": "7", "instances": 28, "metric_value": 0.3512, "depth": 3}
         if obj[7] == 'x':
            # {"feature": "1", "instances": 12, "metric_value": 0.1111, "depth": 4}
            if obj[1] == 'x':
               return 'negative'
            elif obj[1] == 'b':
               return 'negative'
            elif obj[1] == 'o':
               # {"feature": "2", "instances": 3, "metric_value": 0.0, "depth": 5}
               if obj[2] == 'o':
                  return 'negative'
               elif obj[2] == 'b':
                  return 'positive'
               else:
                  return 'positive'
            else:
               return 'negative'
         elif obj[7] == 'o':
            # {"feature": "1", "instances": 10, "metric_value": 0.0, "depth": 4}
            if obj[1] == 'o':
               return 'negative'
            elif obj[1] == 'x':
               return 'positive'
            elif obj[1] == 'b':
               return 'positive'
            else:
               return 'positive'
         elif obj[7] == 'b':
            # {"feature": "3", "instances": 6, "metric_value": 0.2222, "depth": 4}
            if obj[3] == 'x':
               # {"feature": "2", "instances": 3, "metric_value": 0.0, "depth": 5}
               if obj[2] == 'o':
                  return 'negative'
               elif obj[2] == 'x':
                  return 'positive'
               elif obj[2] == 'b':
                  return 'positive'
               else:
                  return 'positive'
            elif obj[3] == 'o':
               return 'negative'
            elif obj[3] == 'b':
               return 'positive'
            else:
               return 'positive'
         else:
            return 'negative'
      else:
         return 'negative'
   elif obj[4] == 'b':
      # {"feature": "0", "instances": 58, "metric_value": 0.3088, "depth": 2}
      if obj[0] == 'x':
         # {"feature": "6", "instances": 33, "metric_value": 0.1429, "depth": 3}
         if obj[6] == 'x':
            return 'positive'
         elif obj[6] == 'o':
            # {"feature": "3", "instances": 8, "metric_value": 0.1667, "depth": 4}
            if obj[3] == 'o':
               return 'positive'
            elif obj[3] == 'x':
               # {"feature": "5", "instances": 3, "metric_value": 0.0, "depth": 5}
               if obj[5] == 'x':
                  return 'negative'
               elif obj[5] == 'o':
                  return 'positive'
               else:
                  return 'positive'
            else:
               return 'negative'
         elif obj[6] == 'b':
            # {"feature": "2", "instances": 7, "metric_value": 0.0, "depth": 4}
            if obj[2] == 'x':
               return 'positive'
            elif obj[2] == 'o':
               return 'negative'
            else:
               return 'negative'
         else:
            return 'positive'
      elif obj[0] == 'o':
         # {"feature": "8", "instances": 14, "metric_value": 0.3, "depth": 3}
         if obj[8] == 'x':
            # {"feature": "2", "instances": 10, "metric_value": 0.15, "depth": 4}
            if obj[2] == 'x':
               return 'positive'
            elif obj[2] == 'o':
               # {"feature": "1", "instances": 4, "metric_value": 0.0, "depth": 5}
               if obj[1] == 'o':
                  return 'negative'
               elif obj[1] == 'x':
                  return 'positive'
               else:
                  return 'positive'
            elif obj[2] == 'b':
               return 'positive'
            else:
               return 'positive'
         elif obj[8] == 'b':
            return 'negative'
         else:
            return 'negative'
      elif obj[0] == 'b':
         # {"feature": "8", "instances": 11, "metric_value": 0.0, "depth": 3}
         if obj[8] == 'x':
            return 'positive'
         elif obj[8] == 'o':
            return 'negative'
         else:
            return 'negative'
      else:
         return 'positive'
   else:
      return 'positive'
