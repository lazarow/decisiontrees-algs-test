def findDecision(obj): #obj[0]: 0, obj[1]: 1, obj[2]: 2, obj[3]: 3, obj[4]: 4, obj[5]: 5, obj[6]: 6, obj[7]: 7, obj[8]: 8, obj[9]: 9, obj[10]: 10, obj[11]: 11, obj[12]: 12, obj[13]: 13, obj[14]: 14, obj[15]: 15, obj[16]: 16, obj[17]: 17
   # {"feature": "12", "instances": 59, "metric_value": 21.7725, "depth": 1}
   if obj[12]<=3:
      # {"feature": "17", "instances": 49, "metric_value": 20.7352, "depth": 2}
      if obj[17]>1:
         # {"feature": "7", "instances": 30, "metric_value": 14.0489, "depth": 3}
         if obj[7]>1:
            # {"feature": "14", "instances": 27, "metric_value": 14.1722, "depth": 4}
            if obj[14]>2:
               # {"feature": "13", "instances": 15, "metric_value": 5.9498, "depth": 5}
               if obj[13]>2:
                  # {"feature": "5", "instances": 14, "metric_value": 6.4641, "depth": 6}
                  if obj[5]<=1:
                     # {"feature": "9", "instances": 8, "metric_value": 4.3469, "depth": 7}
                     if obj[9]>2:
                        # {"feature": "15", "instances": 5, "metric_value": 4.2426, "depth": 8}
                        if obj[15]>1:
                           return '3'
                        elif obj[15]<=1:
                           return '2'
                        else:
                           return '2'
                     elif obj[9]<=2:
                        return '3'
                     else:
                        return '3'
                  elif obj[5]>1:
                     return '3'
                  else:
                     return '3'
               elif obj[13]<=2:
                  return '2'
               else:
                  return '2'
            elif obj[14]<=2:
               # {"feature": "9", "instances": 12, "metric_value": 8.5295, "depth": 5}
               if obj[9]<=2:
                  # {"feature": "0", "instances": 9, "metric_value": 7.2426, "depth": 6}
                  if obj[0]>1:
                     # {"feature": "13", "instances": 8, "metric_value": 5.7735, "depth": 7}
                     if obj[13]<=4:
                        # {"feature": "4", "instances": 4, "metric_value": 3.8637, "depth": 8}
                        if obj[4]<=1:
                           return '2'
                        elif obj[4]>1:
                           return '3'
                        else:
                           return '3'
                     elif obj[13]>4:
                        # {"feature": "2", "instances": 4, "metric_value": 3.8637, "depth": 8}
                        if obj[2]<=1:
                           return '3'
                        elif obj[2]>1:
                           return '4'
                        else:
                           return '4'
                     else:
                        return '3'
                  elif obj[0]<=1:
                     return '1'
                  else:
                     return '1'
               elif obj[9]>2:
                  return '2'
               else:
                  return '2'
            else:
               return '2'
         elif obj[7]<=1:
            return '2'
         else:
            return '2'
      elif obj[17]<=1:
         # {"feature": "15", "instances": 19, "metric_value": 12.1101, "depth": 3}
         if obj[15]<=1:
            # {"feature": "0", "instances": 12, "metric_value": 8.9244, "depth": 4}
            if obj[0]>1:
               # {"feature": "7", "instances": 11, "metric_value": 5.501, "depth": 5}
               if obj[7]>1:
                  # {"feature": "10", "instances": 7, "metric_value": 3.8974, "depth": 6}
                  if obj[10]<=2:
                     # {"feature": "1", "instances": 5, "metric_value": 4.2426, "depth": 7}
                     if obj[1]>1:
                        return '2'
                     elif obj[1]<=1:
                        return '3'
                     else:
                        return '3'
                  elif obj[10]>2:
                     return '2'
                  else:
                     return '2'
               elif obj[7]<=1:
                  return '2'
               else:
                  return '2'
            elif obj[0]<=1:
               return '1'
            else:
               return '1'
         elif obj[15]>1:
            return '2'
         else:
            return '2'
      else:
         return '2'
   elif obj[12]>3:
      return '3'
   else:
      return '3'
