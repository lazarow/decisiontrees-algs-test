def findDecision(obj): #obj[0]: 0, obj[1]: 1, obj[2]: 2, obj[3]: 3, obj[4]: 4, obj[5]: 5, obj[6]: 6, obj[7]: 7, obj[8]: 8, obj[9]: 9, obj[10]: 10, obj[11]: 11, obj[12]: 12, obj[13]: 13, obj[14]: 14, obj[15]: 15, obj[16]: 16, obj[17]: 17
   # {"feature": "0", "instances": 59, "metric_value": 1.2858, "depth": 1}
   if obj[0]>1:
      # {"feature": "8", "instances": 57, "metric_value": 1.1099, "depth": 2}
      if obj[8]<=2:
         # {"feature": "12", "instances": 56, "metric_value": 1.0, "depth": 3}
         if obj[12]<=3:
            # {"feature": "17", "instances": 46, "metric_value": 0.9656, "depth": 4}
            if obj[17]<=4:
               # {"feature": "9", "instances": 41, "metric_value": 0.9012, "depth": 5}
               if obj[9]<=3:
                  # {"feature": "7", "instances": 40, "metric_value": 0.8813, "depth": 6}
                  if obj[7]>1:
                     # {"feature": "13", "instances": 31, "metric_value": 0.9629, "depth": 7}
                     if obj[13]>2:
                        # {"feature": "1", "instances": 25, "metric_value": 0.9988, "depth": 8}
                        if obj[1]<=1:
                           # {"feature": "4", "instances": 13, "metric_value": 0.8905, "depth": 9}
                           if obj[4]<=1:
                              # {"feature": "5", "instances": 12, "metric_value": 0.8113, "depth": 10}
                              if obj[5]<=1:
                                 # {"feature": "11", "instances": 8, "metric_value": 0.9544, "depth": 11}
                                 if obj[11]<=3:
                                    # {"feature": "10", "instances": 6, "metric_value": 1.0, "depth": 12}
                                    if obj[10]>2:
                                       # {"feature": "14", "instances": 3, "metric_value": 0.9183, "depth": 13}
                                       if obj[14]>2:
                                          # {"feature": "15", "instances": 2, "metric_value": 1.0, "depth": 14}
                                          if obj[15]<=1:
                                             return '2'
                                          elif obj[15]>1:
                                             return '3'
                                          else:
                                             return '3'
                                       elif obj[14]<=2:
                                          return '2'
                                       else:
                                          return '2'
                                    elif obj[10]<=2:
                                       # {"feature": "14", "instances": 3, "metric_value": 0.9183, "depth": 13}
                                       if obj[14]<=1:
                                          # {"feature": "16", "instances": 2, "metric_value": 1.0, "depth": 14}
                                          if obj[16]<=1:
                                             return '2'
                                          elif obj[16]>1:
                                             return '3'
                                          else:
                                             return '3'
                                       elif obj[14]>1:
                                          return '3'
                                       else:
                                          return '3'
                                    else:
                                       return '3'
                                 elif obj[11]>3:
                                    return '3'
                                 else:
                                    return '3'
                              elif obj[5]>1:
                                 return '3'
                              else:
                                 return '3'
                           elif obj[4]>1:
                              return '2'
                           else:
                              return '2'
                        elif obj[1]>1:
                           # {"feature": "4", "instances": 12, "metric_value": 0.8113, "depth": 9}
                           if obj[4]<=1:
                              return '2'
                           elif obj[4]>1:
                              # {"feature": "2", "instances": 5, "metric_value": 0.971, "depth": 10}
                              if obj[2]>1:
                                 # {"feature": "11", "instances": 3, "metric_value": 0.9183, "depth": 11}
                                 if obj[11]>2:
                                    return '2'
                                 elif obj[11]<=2:
                                    return '3'
                                 else:
                                    return '3'
                              elif obj[2]<=1:
                                 return '3'
                              else:
                                 return '3'
                           else:
                              return '3'
                        else:
                           return '2'
                     elif obj[13]<=2:
                        return '2'
                     else:
                        return '2'
                  elif obj[7]<=1:
                     return '2'
                  else:
                     return '2'
               elif obj[9]>3:
                  return '3'
               else:
                  return '3'
            elif obj[17]>4:
               return '3'
            else:
               return '3'
         elif obj[12]>3:
            return '3'
         else:
            return '3'
      elif obj[8]>2:
         return '4'
      else:
         return '4'
   elif obj[0]<=1:
      return '1'
   else:
      return '1'
