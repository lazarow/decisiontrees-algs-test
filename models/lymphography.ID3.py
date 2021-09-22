def findDecision(obj): #obj[0]: 0, obj[1]: 1, obj[2]: 2, obj[3]: 3, obj[4]: 4, obj[5]: 5, obj[6]: 6, obj[7]: 7, obj[8]: 8, obj[9]: 9, obj[10]: 10, obj[11]: 11, obj[12]: 12, obj[13]: 13, obj[14]: 14, obj[15]: 15, obj[16]: 16, obj[17]: 17
   # {"feature": "14", "instances": 59, "metric_value": 1.2858, "depth": 1}
   if obj[14]>2:
      # {"feature": "7", "instances": 32, "metric_value": 0.8571, "depth": 2}
      if obj[7]>1:
         # {"feature": "15", "instances": 28, "metric_value": 0.6769, "depth": 3}
         if obj[15]>1:
            # {"feature": "9", "instances": 20, "metric_value": 0.2864, "depth": 4}
            if obj[9]>2:
               return '3'
            elif obj[9]<=2:
               # {"feature": "1", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[1]<=1:
                  return '3'
               elif obj[1]>1:
                  return '2'
               else:
                  return '2'
            else:
               return '3'
         elif obj[15]<=1:
            # {"feature": "1", "instances": 8, "metric_value": 1.0, "depth": 4}
            if obj[1]<=1:
               # {"feature": "10", "instances": 6, "metric_value": 0.9183, "depth": 5}
               if obj[10]<=2:
                  return '3'
               elif obj[10]>2:
                  # {"feature": "5", "instances": 3, "metric_value": 0.9183, "depth": 6}
                  if obj[5]<=1:
                     return '2'
                  elif obj[5]>1:
                     return '3'
                  else:
                     return '3'
               else:
                  return '2'
            elif obj[1]>1:
               return '2'
            else:
               return '2'
         else:
            return '2'
      elif obj[7]<=1:
         return '2'
      else:
         return '2'
   elif obj[14]<=2:
      # {"feature": "12", "instances": 27, "metric_value": 1.2615, "depth": 2}
      if obj[12]>1:
         # {"feature": "17", "instances": 23, "metric_value": 0.8077, "depth": 3}
         if obj[17]<=3:
            # {"feature": "1", "instances": 21, "metric_value": 0.4537, "depth": 4}
            if obj[1]>1:
               return '2'
            elif obj[1]<=1:
               # {"feature": "5", "instances": 9, "metric_value": 0.7642, "depth": 5}
               if obj[5]<=1:
                  # {"feature": "0", "instances": 8, "metric_value": 0.5436, "depth": 6}
                  if obj[0]<=3:
                     return '2'
                  elif obj[0]>3:
                     # {"feature": "10", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[10]>2:
                        return '2'
                     elif obj[10]<=2:
                        return '3'
                     else:
                        return '3'
                  else:
                     return '2'
               elif obj[5]>1:
                  return '3'
               else:
                  return '3'
            else:
               return '2'
         elif obj[17]>3:
            # {"feature": "2", "instances": 2, "metric_value": 1.0, "depth": 4}
            if obj[2]<=1:
               return '3'
            elif obj[2]>1:
               return '4'
            else:
               return '4'
         else:
            return '3'
      elif obj[12]<=1:
         # {"feature": "0", "instances": 4, "metric_value": 1.0, "depth": 3}
         if obj[0]<=1:
            return '1'
         elif obj[0]>1:
            return '3'
         else:
            return '3'
      else:
         return '1'
   else:
      return '2'
