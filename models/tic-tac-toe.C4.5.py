def findDecision(obj): #obj[0]: 0, obj[1]: 1, obj[2]: 2, obj[3]: 3, obj[4]: 4, obj[5]: 5, obj[6]: 6, obj[7]: 7, obj[8]: 8
   # {"feature": "4", "instances": 383, "metric_value": 0.9451, "depth": 1}
   if obj[4] == 'x':
      # {"feature": "0", "instances": 181, "metric_value": 0.7307, "depth": 2}
      if obj[0] == 'o':
         # {"feature": "6", "instances": 71, "metric_value": 0.9229, "depth": 3}
         if obj[6] == 'x':
            # {"feature": "2", "instances": 36, "metric_value": 0.7107, "depth": 4}
            if obj[2] == 'x':
               return 'positive'
            elif obj[2] == 'o':
               # {"feature": "1", "instances": 10, "metric_value": 0.8813, "depth": 5}
               if obj[1] == 'o':
                  return 'negative'
               elif obj[1] == 'x':
                  # {"feature": "5", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[5] == 'x':
                     return 'positive'
                  elif obj[5] == 'b':
                     return 'positive'
                  elif obj[5] == 'o':
                     return 'negative'
                  else:
                     return 'negative'
               elif obj[1] == 'b':
                  # {"feature": "5", "instances": 2, "metric_value": 1.0, "depth": 6}
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
            # {"feature": "3", "instances": 27, "metric_value": 0.951, "depth": 4}
            if obj[3] == 'x':
               # {"feature": "5", "instances": 12, "metric_value": 0.8113, "depth": 5}
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
               # {"feature": "5", "instances": 3, "metric_value": 0.9183, "depth": 5}
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
         # {"feature": "8", "instances": 60, "metric_value": 0.65, "depth": 3}
         if obj[8] == 'x':
            return 'positive'
         elif obj[8] == 'o':
            # {"feature": "3", "instances": 24, "metric_value": 0.9799, "depth": 4}
            if obj[3] == 'x':
               # {"feature": "6", "instances": 9, "metric_value": 0.9911, "depth": 5}
               if obj[6] == 'x':
                  return 'positive'
               elif obj[6] == 'o':
                  return 'negative'
               elif obj[6] == 'b':
                  # {"feature": "1", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[1] == 'o':
                     return 'positive'
                  elif obj[1] == 'x':
                     return 'negative'
                  else:
                     return 'negative'
               else:
                  return 'positive'
            elif obj[3] == 'o':
               # {"feature": "2", "instances": 9, "metric_value": 0.5033, "depth": 5}
               if obj[2] == 'x':
                  return 'positive'
               elif obj[2] == 'o':
                  # {"feature": "7", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[7] == 'x':
                     return 'positive'
                  elif obj[7] == 'b':
                     return 'negative'
                  else:
                     return 'negative'
               elif obj[2] == 'b':
                  return 'positive'
               else:
                  return 'positive'
            elif obj[3] == 'b':
               # {"feature": "7", "instances": 6, "metric_value": 0.65, "depth": 5}
               if obj[7] == 'o':
                  return 'negative'
               elif obj[7] == 'x':
                  # {"feature": "1", "instances": 2, "metric_value": 1.0, "depth": 6}
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
         # {"feature": "8", "instances": 50, "metric_value": 0.3274, "depth": 3}
         if obj[8] == 'o':
            # {"feature": "7", "instances": 25, "metric_value": 0.5294, "depth": 4}
            if obj[7] == 'x':
               # {"feature": "1", "instances": 14, "metric_value": 0.3712, "depth": 5}
               if obj[1] == 'x':
                  return 'positive'
               elif obj[1] == 'o':
                  return 'positive'
               elif obj[1] == 'b':
                  # {"feature": "3", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[3] == 'x':
                     return 'positive'
                  elif obj[3] == 'b':
                     return 'negative'
                  else:
                     return 'negative'
               else:
                  return 'positive'
            elif obj[7] == 'o':
               # {"feature": "6", "instances": 7, "metric_value": 0.8631, "depth": 5}
               if obj[6] == 'x':
                  return 'positive'
               elif obj[6] == 'o':
                  return 'negative'
               elif obj[6] == 'b':
                  return 'positive'
               else:
                  return 'positive'
            elif obj[7] == 'b':
               return 'positive'
            else:
               return 'positive'
         elif obj[8] == 'b':
            return 'positive'
         elif obj[8] == 'x':
            return 'positive'
         else:
            return 'positive'
      else:
         return 'positive'
   elif obj[4] == 'o':
      # {"feature": "8", "instances": 144, "metric_value": 0.9685, "depth": 2}
      if obj[8] == 'x':
         # {"feature": "2", "instances": 70, "metric_value": 1.0, "depth": 3}
         if obj[2] == 'o':
            # {"feature": "6", "instances": 30, "metric_value": 0.8813, "depth": 4}
            if obj[6] == 'o':
               return 'negative'
            elif obj[6] == 'x':
               # {"feature": "7", "instances": 13, "metric_value": 0.8905, "depth": 5}
               if obj[7] == 'x':
                  return 'positive'
               elif obj[7] == 'o':
                  # {"feature": "5", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[5] == 'x':
                     return 'negative'
                  elif obj[5] == 'o':
                     return 'positive'
                  else:
                     return 'positive'
               elif obj[7] == 'b':
                  # {"feature": "1", "instances": 2, "metric_value": 1.0, "depth": 6}
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
            # {"feature": "5", "instances": 27, "metric_value": 0.8256, "depth": 4}
            if obj[5] == 'x':
               return 'positive'
            elif obj[5] == 'o':
               # {"feature": "3", "instances": 7, "metric_value": 0.5917, "depth": 5}
               if obj[3] == 'o':
                  return 'negative'
               elif obj[3] == 'x':
                  return 'negative'
               elif obj[3] == 'b':
                  return 'positive'
               else:
                  return 'positive'
            elif obj[5] == 'b':
               # {"feature": "3", "instances": 5, "metric_value": 0.7219, "depth": 5}
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
            # {"feature": "7", "instances": 13, "metric_value": 0.9957, "depth": 4}
            if obj[7] == 'x':
               # {"feature": "6", "instances": 8, "metric_value": 0.8113, "depth": 5}
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
         # {"feature": "0", "instances": 46, "metric_value": 0.859, "depth": 3}
         if obj[0] == 'o':
            return 'negative'
         elif obj[0] == 'x':
            # {"feature": "7", "instances": 20, "metric_value": 0.9341, "depth": 4}
            if obj[7] == 'x':
               # {"feature": "2", "instances": 11, "metric_value": 0.994, "depth": 5}
               if obj[2] == 'o':
                  # {"feature": "1", "instances": 6, "metric_value": 0.65, "depth": 6}
                  if obj[1] == 'x':
                     return 'negative'
                  elif obj[1] == 'b':
                     # {"feature": "5", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[5] == 'x':
                        return 'negative'
                     elif obj[5] == 'b':
                        return 'positive'
                     else:
                        return 'positive'
                  else:
                     return 'negative'
               elif obj[2] == 'x':
                  # {"feature": "1", "instances": 4, "metric_value": 0.8113, "depth": 6}
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
               # {"feature": "6", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[6] == 'x':
                  return 'positive'
               elif obj[6] == 'b':
                  return 'negative'
               else:
                  return 'negative'
            else:
               return 'positive'
         elif obj[0] == 'b':
            return 'negative'
         else:
            return 'negative'
      elif obj[8] == 'b':
         # {"feature": "0", "instances": 28, "metric_value": 0.9059, "depth": 3}
         if obj[0] == 'x':
            # {"feature": "7", "instances": 21, "metric_value": 0.9852, "depth": 4}
            if obj[7] == 'x':
               # {"feature": "3", "instances": 8, "metric_value": 0.5436, "depth": 5}
               if obj[3] == 'o':
                  return 'negative'
               elif obj[3] == 'x':
                  # {"feature": "2", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[2] == 'b':
                     return 'positive'
                  elif obj[2] == 'o':
                     return 'negative'
                  else:
                     return 'negative'
               elif obj[3] == 'b':
                  return 'negative'
               else:
                  return 'negative'
            elif obj[7] == 'o':
               # {"feature": "1", "instances": 8, "metric_value": 0.9544, "depth": 5}
               if obj[1] == 'x':
                  return 'positive'
               elif obj[1] == 'o':
                  return 'negative'
               elif obj[1] == 'b':
                  return 'positive'
               else:
                  return 'positive'
            elif obj[7] == 'b':
               # {"feature": "2", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[2] == 'x':
                  return 'positive'
               elif obj[2] == 'b':
                  # {"feature": "1", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[1] == 'b':
                     return 'positive'
                  elif obj[1] == 'x':
                     return 'negative'
                  else:
                     return 'negative'
               elif obj[2] == 'o':
                  return 'negative'
               else:
                  return 'negative'
            else:
               return 'positive'
         elif obj[0] == 'o':
            return 'negative'
         elif obj[0] == 'b':
            return 'negative'
         else:
            return 'negative'
      else:
         return 'negative'
   elif obj[4] == 'b':
      # {"feature": "0", "instances": 58, "metric_value": 0.8247, "depth": 2}
      if obj[0] == 'x':
         # {"feature": "6", "instances": 33, "metric_value": 0.4395, "depth": 3}
         if obj[6] == 'x':
            return 'positive'
         elif obj[6] == 'o':
            # {"feature": "2", "instances": 8, "metric_value": 0.8113, "depth": 4}
            if obj[2] == 'x':
               # {"feature": "3", "instances": 7, "metric_value": 0.5917, "depth": 5}
               if obj[3] == 'o':
                  return 'positive'
               elif obj[3] == 'x':
                  # {"feature": "1", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[1] == 'o':
                     return 'negative'
                  elif obj[1] == 'x':
                     return 'positive'
                  else:
                     return 'positive'
               else:
                  return 'negative'
            elif obj[2] == 'o':
               return 'negative'
            else:
               return 'negative'
         elif obj[6] == 'b':
            # {"feature": "2", "instances": 7, "metric_value": 0.5917, "depth": 4}
            if obj[2] == 'x':
               return 'positive'
            elif obj[2] == 'o':
               return 'negative'
            else:
               return 'negative'
         else:
            return 'positive'
      elif obj[0] == 'o':
         # {"feature": "8", "instances": 14, "metric_value": 1.0, "depth": 3}
         if obj[8] == 'x':
            # {"feature": "2", "instances": 10, "metric_value": 0.8813, "depth": 4}
            if obj[2] == 'x':
               return 'positive'
            elif obj[2] == 'o':
               # {"feature": "1", "instances": 4, "metric_value": 0.8113, "depth": 5}
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
         # {"feature": "8", "instances": 11, "metric_value": 0.994, "depth": 3}
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
