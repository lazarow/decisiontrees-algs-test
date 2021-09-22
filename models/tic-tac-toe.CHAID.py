def findDecision(obj): #obj[0]: 0, obj[1]: 1, obj[2]: 2, obj[3]: 3, obj[4]: 4, obj[5]: 5, obj[6]: 6, obj[7]: 7, obj[8]: 8
   # {"feature": "4", "instances": 383, "metric_value": 19.9826, "depth": 1}
   if obj[4] == 'x':
      # {"feature": "6", "instances": 181, "metric_value": 19.9944, "depth": 2}
      if obj[6] == 'o':
         # {"feature": "0", "instances": 75, "metric_value": 11.241, "depth": 3}
         if obj[0] == 'x':
            # {"feature": "8", "instances": 28, "metric_value": 8.1674, "depth": 4}
            if obj[8] == 'x':
               return 'positive'
            elif obj[8] == 'o':
               # {"feature": "3", "instances": 11, "metric_value": 6.6921, "depth": 5}
               if obj[3] == 'b':
                  # {"feature": "2", "instances": 4, "metric_value": 4.8284, "depth": 6}
                  if obj[2] == 'x':
                     return 'negative'
                  elif obj[2] == 'o':
                     return 'positive'
                  elif obj[2] == 'b':
                     return 'negative'
                  else:
                     return 'negative'
               elif obj[3] == 'o':
                  return 'positive'
               elif obj[3] == 'x':
                  return 'negative'
               else:
                  return 'negative'
            elif obj[8] == 'b':
               return 'positive'
            else:
               return 'positive'
         elif obj[0] == 'o':
            # {"feature": "3", "instances": 27, "metric_value": 8.165, "depth": 4}
            if obj[3] == 'x':
               # {"feature": "5", "instances": 12, "metric_value": 7.6569, "depth": 5}
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
               # {"feature": "5", "instances": 3, "metric_value": 3.4142, "depth": 5}
               if obj[5] == 'x':
                  return 'negative'
               elif obj[5] == 'b':
                  return 'positive'
               else:
                  return 'positive'
            else:
               return 'negative'
         elif obj[0] == 'b':
            # {"feature": "8", "instances": 20, "metric_value": 8.9834, "depth": 4}
            if obj[8] == 'o':
               # {"feature": "7", "instances": 9, "metric_value": 6.8783, "depth": 5}
               if obj[7] == 'x':
                  return 'positive'
               elif obj[7] == 'o':
                  return 'negative'
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
      elif obj[6] == 'x':
         # {"feature": "0", "instances": 73, "metric_value": 15.3676, "depth": 3}
         if obj[0] == 'o':
            # {"feature": "2", "instances": 36, "metric_value": 11.0207, "depth": 4}
            if obj[2] == 'x':
               return 'positive'
            elif obj[2] == 'o':
               # {"feature": "8", "instances": 10, "metric_value": 4.0, "depth": 5}
               if obj[8] == 'o':
                  # {"feature": "5", "instances": 6, "metric_value": 4.2307, "depth": 6}
                  if obj[5] == 'x':
                     # {"feature": "1", "instances": 3, "metric_value": 4.2426, "depth": 7}
                     if obj[1] == 'o':
                        return 'negative'
                     elif obj[1] == 'x':
                        return 'positive'
                     elif obj[1] == 'b':
                        return 'positive'
                     else:
                        return 'positive'
                  elif obj[5] == 'o':
                     return 'negative'
                  elif obj[5] == 'b':
                     return 'positive'
                  else:
                     return 'positive'
               elif obj[8] == 'x':
                  return 'negative'
               elif obj[8] == 'b':
                  return 'negative'
               else:
                  return 'negative'
            elif obj[2] == 'b':
               return 'positive'
            else:
               return 'positive'
         elif obj[0] == 'b':
            # {"feature": "8", "instances": 19, "metric_value": 9.5924, "depth": 4}
            if obj[8] == 'o':
               # {"feature": "1", "instances": 9, "metric_value": 5.8637, "depth": 5}
               if obj[1] == 'b':
                  # {"feature": "3", "instances": 4, "metric_value": 4.8284, "depth": 6}
                  if obj[3] == 'x':
                     return 'positive'
                  elif obj[3] == 'b':
                     return 'negative'
                  elif obj[3] == 'o':
                     return 'positive'
                  else:
                     return 'positive'
               elif obj[1] == 'o':
                  return 'positive'
               elif obj[1] == 'x':
                  return 'positive'
               else:
                  return 'positive'
            elif obj[8] == 'b':
               return 'positive'
            elif obj[8] == 'x':
               return 'positive'
            else:
               return 'positive'
         elif obj[0] == 'x':
            # {"feature": "2", "instances": 18, "metric_value": 8.2706, "depth": 4}
            if obj[2] == 'o':
               # {"feature": "1", "instances": 9, "metric_value": 5.7155, "depth": 5}
               if obj[1] == 'b':
                  return 'positive'
               elif obj[1] == 'o':
                  return 'positive'
               elif obj[1] == 'x':
                  # {"feature": "8", "instances": 3, "metric_value": 3.4142, "depth": 6}
                  if obj[8] == 'o':
                     return 'negative'
                  elif obj[8] == 'x':
                     return 'positive'
                  else:
                     return 'positive'
               else:
                  return 'negative'
            elif obj[2] == 'x':
               return 'positive'
            elif obj[2] == 'b':
               return 'positive'
            else:
               return 'positive'
         else:
            return 'positive'
      elif obj[6] == 'b':
         # {"feature": "0", "instances": 33, "metric_value": 12.4701, "depth": 3}
         if obj[0] == 'x':
            # {"feature": "2", "instances": 14, "metric_value": 6.899, "depth": 4}
            if obj[2] == 'o':
               # {"feature": "5", "instances": 8, "metric_value": 4.0, "depth": 5}
               if obj[5] == 'o':
                  # {"feature": "7", "instances": 4, "metric_value": 4.8284, "depth": 6}
                  if obj[7] == 'b':
                     return 'positive'
                  elif obj[7] == 'o':
                     return 'negative'
                  elif obj[7] == 'x':
                     return 'negative'
                  else:
                     return 'negative'
               elif obj[5] == 'x':
                  return 'positive'
               elif obj[5] == 'b':
                  return 'positive'
               else:
                  return 'positive'
            elif obj[2] == 'x':
               return 'positive'
            elif obj[2] == 'b':
               return 'positive'
            else:
               return 'positive'
         elif obj[0] == 'b':
            return 'positive'
         elif obj[0] == 'o':
            return 'positive'
         else:
            return 'positive'
      else:
         return 'positive'
   elif obj[4] == 'o':
      # {"feature": "5", "instances": 144, "metric_value": 6.8535, "depth": 2}
      if obj[5] == 'x':
         # {"feature": "8", "instances": 65, "metric_value": 9.7648, "depth": 3}
         if obj[8] == 'x':
            # {"feature": "2", "instances": 32, "metric_value": 11.206, "depth": 4}
            if obj[2] == 'x':
               return 'positive'
            elif obj[2] == 'o':
               # {"feature": "3", "instances": 13, "metric_value": 7.4049, "depth": 5}
               if obj[3] == 'b':
                  return 'negative'
               elif obj[3] == 'o':
                  # {"feature": "1", "instances": 4, "metric_value": 3.8637, "depth": 6}
                  if obj[1] == 'x':
                     return 'negative'
                  elif obj[1] == 'b':
                     return 'positive'
                  else:
                     return 'positive'
               elif obj[3] == 'x':
                  return 'negative'
               else:
                  return 'negative'
            elif obj[2] == 'b':
               # {"feature": "0", "instances": 4, "metric_value": 2.8284, "depth": 5}
               if obj[0] == 'b':
                  # {"feature": "3", "instances": 2, "metric_value": 2.8284, "depth": 6}
                  if obj[3] == 'o':
                     return 'positive'
                  elif obj[3] == 'x':
                     return 'negative'
                  else:
                     return 'negative'
               elif obj[0] == 'o':
                  return 'negative'
               elif obj[0] == 'x':
                  return 'negative'
               else:
                  return 'negative'
            else:
               return 'negative'
         elif obj[8] == 'o':
            # {"feature": "3", "instances": 22, "metric_value": 9.5549, "depth": 4}
            if obj[3] == 'x':
               # {"feature": "2", "instances": 11, "metric_value": 6.2806, "depth": 5}
               if obj[2] == 'x':
                  return 'negative'
               elif obj[2] == 'o':
                  # {"feature": "7", "instances": 3, "metric_value": 4.2426, "depth": 6}
                  if obj[7] == 'o':
                     return 'positive'
                  elif obj[7] == 'b':
                     return 'positive'
                  elif obj[7] == 'x':
                     return 'negative'
                  else:
                     return 'negative'
               elif obj[2] == 'b':
                  return 'negative'
               else:
                  return 'negative'
            elif obj[3] == 'b':
               return 'negative'
            elif obj[3] == 'o':
               return 'negative'
            else:
               return 'negative'
         elif obj[8] == 'b':
            # {"feature": "0", "instances": 11, "metric_value": 6.552, "depth": 4}
            if obj[0] == 'x':
               # {"feature": "3", "instances": 6, "metric_value": 4.0, "depth": 5}
               if obj[3] == 'o':
                  # {"feature": "2", "instances": 2, "metric_value": 2.8284, "depth": 6}
                  if obj[2] == 'o':
                     return 'negative'
                  elif obj[2] == 'x':
                     return 'positive'
                  else:
                     return 'positive'
               elif obj[3] == 'b':
                  return 'negative'
               elif obj[3] == 'x':
                  return 'negative'
               else:
                  return 'negative'
            elif obj[0] == 'o':
               return 'negative'
            elif obj[0] == 'b':
               return 'negative'
            else:
               return 'negative'
         else:
            return 'negative'
      elif obj[5] == 'o':
         # {"feature": "3", "instances": 40, "metric_value": 8.8116, "depth": 3}
         if obj[3] == 'x':
            # {"feature": "6", "instances": 18, "metric_value": 5.3127, "depth": 4}
            if obj[6] == 'x':
               # {"feature": "7", "instances": 12, "metric_value": 5.6569, "depth": 5}
               if obj[7] == 'x':
                  return 'positive'
               elif obj[7] == 'o':
                  # {"feature": "1", "instances": 4, "metric_value": 4.8284, "depth": 6}
                  if obj[1] == 'x':
                     return 'positive'
                  elif obj[1] == 'o':
                     return 'negative'
                  elif obj[1] == 'b':
                     return 'positive'
                  else:
                     return 'positive'
               elif obj[7] == 'b':
                  # {"feature": "0", "instances": 4, "metric_value": 3.8637, "depth": 6}
                  if obj[0] == 'x':
                     return 'positive'
                  elif obj[0] == 'o':
                     return 'negative'
                  else:
                     return 'negative'
               else:
                  return 'positive'
            elif obj[6] == 'o':
               # {"feature": "8", "instances": 5, "metric_value": 5.2779, "depth": 5}
               if obj[8] == 'x':
                  return 'negative'
               elif obj[8] == 'o':
                  return 'positive'
               elif obj[8] == 'b':
                  return 'positive'
               else:
                  return 'positive'
            elif obj[6] == 'b':
               return 'negative'
            else:
               return 'negative'
         elif obj[3] == 'o':
            return 'negative'
         elif obj[3] == 'b':
            # {"feature": "8", "instances": 6, "metric_value": 3.266, "depth": 4}
            if obj[8] == 'x':
               return 'positive'
            elif obj[8] == 'o':
               # {"feature": "6", "instances": 3, "metric_value": 3.4142, "depth": 5}
               if obj[6] == 'x':
                  return 'negative'
               elif obj[6] == 'b':
                  return 'positive'
               else:
                  return 'positive'
            else:
               return 'negative'
         else:
            return 'positive'
      elif obj[5] == 'b':
         # {"feature": "0", "instances": 39, "metric_value": 5.7644, "depth": 3}
         if obj[0] == 'x':
            # {"feature": "6", "instances": 21, "metric_value": 7.1635, "depth": 4}
            if obj[6] == 'o':
               # {"feature": "2", "instances": 9, "metric_value": 5.9136, "depth": 5}
               if obj[2] == 'o':
                  return 'negative'
               elif obj[2] == 'x':
                  return 'positive'
               else:
                  return 'positive'
            elif obj[6] == 'x':
               # {"feature": "3", "instances": 9, "metric_value": 6.8783, "depth": 5}
               if obj[3] == 'x':
                  return 'positive'
               elif obj[3] == 'o':
                  return 'positive'
               elif obj[3] == 'b':
                  return 'negative'
               else:
                  return 'negative'
            elif obj[6] == 'b':
               return 'positive'
            else:
               return 'positive'
         elif obj[0] == 'o':
            # {"feature": "6", "instances": 12, "metric_value": 4.8637, "depth": 4}
            if obj[6] == 'x':
               # {"feature": "8", "instances": 8, "metric_value": 4.2426, "depth": 5}
               if obj[8] == 'o':
                  return 'negative'
               elif obj[8] == 'x':
                  # {"feature": "7", "instances": 4, "metric_value": 3.8637, "depth": 6}
                  if obj[7] == 'x':
                     return 'positive'
                  elif obj[7] == 'o':
                     return 'negative'
                  else:
                     return 'negative'
               else:
                  return 'positive'
            elif obj[6] == 'b':
               return 'negative'
            elif obj[6] == 'o':
               return 'negative'
            else:
               return 'negative'
         elif obj[0] == 'b':
            # {"feature": "3", "instances": 6, "metric_value": 4.2307, "depth": 4}
            if obj[3] == 'x':
               # {"feature": "1", "instances": 3, "metric_value": 1.4142, "depth": 5}
               if obj[1] == 'o':
                  # {"feature": "2", "instances": 2, "metric_value": 2.8284, "depth": 6}
                  if obj[2] == 'b':
                     return 'negative'
                  elif obj[2] == 'o':
                     return 'positive'
                  else:
                     return 'positive'
               elif obj[1] == 'b':
                  return 'negative'
               else:
                  return 'negative'
            elif obj[3] == 'o':
               return 'positive'
            elif obj[3] == 'b':
               return 'positive'
            else:
               return 'positive'
         else:
            return 'positive'
      else:
         return 'positive'
   elif obj[4] == 'b':
      # {"feature": "2", "instances": 58, "metric_value": 9.2001, "depth": 2}
      if obj[2] == 'x':
         # {"feature": "6", "instances": 31, "metric_value": 9.121, "depth": 3}
         if obj[6] == 'o':
            # {"feature": "8", "instances": 16, "metric_value": 4.6188, "depth": 4}
            if obj[8] == 'o':
               # {"feature": "3", "instances": 6, "metric_value": 5.8637, "depth": 5}
               if obj[3] == 'x':
                  return 'negative'
               elif obj[3] == 'o':
                  return 'positive'
               elif obj[3] == 'b':
                  return 'negative'
               else:
                  return 'negative'
            elif obj[8] == 'x':
               return 'positive'
            elif obj[8] == 'b':
               # {"feature": "7", "instances": 4, "metric_value": 4.8284, "depth": 5}
               if obj[7] == 'x':
                  return 'negative'
               elif obj[7] == 'o':
                  return 'positive'
               elif obj[7] == 'b':
                  return 'positive'
               else:
                  return 'positive'
            else:
               return 'positive'
         elif obj[6] == 'b':
            return 'positive'
         elif obj[6] == 'x':
            return 'positive'
         else:
            return 'positive'
      elif obj[2] == 'o':
         # {"feature": "6", "instances": 20, "metric_value": 7.0055, "depth": 3}
         if obj[6] == 'x':
            # {"feature": "0", "instances": 15, "metric_value": 5.6569, "depth": 4}
            if obj[0] == 'x':
               return 'positive'
            elif obj[0] == 'o':
               # {"feature": "1", "instances": 4, "metric_value": 3.8637, "depth": 5}
               if obj[1] == 'o':
                  return 'negative'
               elif obj[1] == 'x':
                  return 'positive'
               else:
                  return 'positive'
            elif obj[0] == 'b':
               # {"feature": "1", "instances": 2, "metric_value": 2.8284, "depth": 5}
               if obj[1] == 'x':
                  return 'negative'
               elif obj[1] == 'b':
                  return 'positive'
               else:
                  return 'positive'
            else:
               return 'negative'
         elif obj[6] == 'b':
            return 'negative'
         elif obj[6] == 'o':
            return 'negative'
         else:
            return 'negative'
      elif obj[2] == 'b':
         return 'positive'
      else:
         return 'positive'
   else:
      return 'positive'
