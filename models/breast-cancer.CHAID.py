def findDecision(obj): #obj[0]: 0, obj[1]: 1, obj[2]: 2, obj[3]: 3, obj[4]: 4, obj[5]: 5, obj[6]: 6, obj[7]: 7, obj[8]: 8
   # {"feature": "3", "instances": 114, "metric_value": 23.7104, "depth": 1}
   if obj[3] == '30-34':
      # {"feature": "4", "instances": 26, "metric_value": 8.8135, "depth": 2}
      if obj[4] == '0-2':
         # {"feature": "1", "instances": 16, "metric_value": 8.6232, "depth": 3}
         if obj[1] == '50-59':
            return 'no'
         elif obj[1] == '40-49':
            # {"feature": "8", "instances": 5, "metric_value": 4.2426, "depth": 4}
            if obj[8] == 'right_up':
               # {"feature": "6", "instances": 2, "metric_value": 2.8284, "depth": 5}
               if obj[6]>2:
                  return 'no'
               elif obj[6]<=2:
                  return 'yes'
               else:
                  return 'yes'
            elif obj[8] == 'left_low':
               return 'yes'
            elif obj[8] == 'right_low':
               return 'no'
            elif obj[8] == 'left_up':
               return 'yes'
            else:
               return 'yes'
         elif obj[1] == '60-69':
            return 'no'
         elif obj[1] == '30-39':
            return 'no'
         else:
            return 'no'
      elif obj[4] == '6-8':
         # {"feature": "8", "instances": 4, "metric_value": 2.8284, "depth": 3}
         if obj[8] == 'right_low':
            # {"feature": "6", "instances": 2, "metric_value": 2.8284, "depth": 4}
            if obj[6]<=2:
               return 'yes'
            elif obj[6]>2:
               return 'no'
            else:
               return 'no'
         elif obj[8] == 'right_up':
            return 'no'
         elif obj[8] == 'left_low':
            return 'no'
         else:
            return 'no'
      elif obj[4] == '9-11':
         return 'yes'
      elif obj[4] == '3-5':
         # {"feature": "1", "instances": 2, "metric_value": 2.8284, "depth": 3}
         if obj[1] == '50-59':
            return 'no'
         elif obj[1] == '60-69':
            return 'yes'
         else:
            return 'yes'
      elif obj[4] == '15-17':
         return 'no'
      else:
         return 'no'
   elif obj[3] == '25-29':
      # {"feature": "4", "instances": 20, "metric_value": 10.2593, "depth": 2}
      if obj[4] == '0-2':
         # {"feature": "8", "instances": 15, "metric_value": 8.1801, "depth": 3}
         if obj[8] == 'left_low':
            # {"feature": "0", "instances": 7, "metric_value": 3.7236, "depth": 4}
            if obj[0] == 'no-recurrence-events':
               # {"feature": "1", "instances": 6, "metric_value": 4.0, "depth": 5}
               if obj[1] == '40-49':
                  # {"feature": "2", "instances": 2, "metric_value": 2.8284, "depth": 6}
                  if obj[2] == 'premeno':
                     return 'yes'
                  elif obj[2] == 'ge40':
                     return 'no'
                  else:
                     return 'no'
               elif obj[1] == '50-59':
                  return 'no'
               elif obj[1] == '60-69':
                  return 'no'
               else:
                  return 'no'
            elif obj[0] == 'recurrence-events':
               return 'yes'
            else:
               return 'yes'
         elif obj[8] == 'left_up':
            return 'no'
         elif obj[8] == 'right_up':
            return 'no'
         elif obj[8] == 'right_low':
            return 'no'
         else:
            return 'no'
      elif obj[4] == '3-5':
         return 'yes'
      elif obj[4] == '6-8':
         return 'yes'
      elif obj[4] == '15-17':
         return 'no'
      elif obj[4] == '9-11':
         return 'no'
      else:
         return 'no'
   elif obj[3] == '20-24':
      # {"feature": "8", "instances": 16, "metric_value": 6.6563, "depth": 2}
      if obj[8] == 'left_up':
         # {"feature": "1", "instances": 6, "metric_value": 6.6921, "depth": 3}
         if obj[1] == '50-59':
            return 'no'
         elif obj[1] == '40-49':
            return 'no'
         elif obj[1] == '30-39':
            return 'yes'
         elif obj[1] == '60-69':
            return 'no'
         else:
            return 'no'
      elif obj[8] == 'left_low':
         # {"feature": "1", "instances": 5, "metric_value": 5.4142, "depth": 3}
         if obj[1] == '50-59':
            return 'no'
         elif obj[1] == '40-49':
            return 'no'
         elif obj[1] == '60-69':
            return 'yes'
         else:
            return 'yes'
      elif obj[8] == 'central':
         return 'no'
      elif obj[8] == 'right_up':
         # {"feature": "0", "instances": 2, "metric_value": 2.8284, "depth": 3}
         if obj[0] == 'recurrence-events':
            return 'yes'
         elif obj[0] == 'no-recurrence-events':
            return 'no'
         else:
            return 'no'
      else:
         return 'yes'
   elif obj[3] == '15-19':
      # {"feature": "5", "instances": 12, "metric_value": 5.5777, "depth": 2}
      if obj[5] == 'no':
         # {"feature": "1", "instances": 10, "metric_value": 7.2779, "depth": 3}
         if obj[1] == '60-69':
            # {"feature": "6", "instances": 4, "metric_value": 3.8637, "depth": 4}
            if obj[6]<=2:
               return 'no'
            elif obj[6]>2:
               return 'yes'
            else:
               return 'yes'
         elif obj[1] == '50-59':
            return 'no'
         elif obj[1] == '40-49':
            return 'no'
         elif obj[1] == '30-39':
            return 'no'
         else:
            return 'no'
      elif obj[5] == 'yes':
         return 'yes'
      else:
         return 'yes'
   elif obj[3] == '40-44':
      # {"feature": "1", "instances": 11, "metric_value": 8.4734, "depth": 2}
      if obj[1] == '50-59':
         return 'no'
      elif obj[1] == '40-49':
         # {"feature": "4", "instances": 3, "metric_value": 4.2426, "depth": 3}
         if obj[4] == '3-5':
            return 'yes'
         elif obj[4] == '15-17':
            return 'yes'
         elif obj[4] == '0-2':
            return 'no'
         else:
            return 'no'
      elif obj[1] == '30-39':
         return 'no'
      elif obj[1] == '60-69':
         return 'yes'
      elif obj[1] == '70-79':
         return 'no'
      else:
         return 'no'
   elif obj[3] == '10-14':
      return 'no'
   elif obj[3] == '35-39':
      # {"feature": "4", "instances": 9, "metric_value": 5.501, "depth": 2}
      if obj[4] == '0-2':
         # {"feature": "5", "instances": 7, "metric_value": 4.8783, "depth": 3}
         if obj[5] == 'no':
            return 'no'
         elif obj[5] == 'yes':
            return 'yes'
         else:
            return 'yes'
      elif obj[4] == '9-11':
         return 'yes'
      elif obj[4] == '6-8':
         return 'no'
      else:
         return 'no'
   elif obj[3] == '50-54':
      # {"feature": "7", "instances": 6, "metric_value": 3.4142, "depth": 2}
      if obj[7] == 'right':
         # {"feature": "6", "instances": 4, "metric_value": 3.8637, "depth": 3}
         if obj[6]<=2:
            return 'yes'
         elif obj[6]>2:
            return 'no'
         else:
            return 'no'
      elif obj[7] == 'left':
         return 'no'
      else:
         return 'no'
   elif obj[3] == '5-9':
      # {"feature": "1", "instances": 2, "metric_value": 2.8284, "depth": 2}
      if obj[1] == '40-49':
         return 'yes'
      elif obj[1] == '30-39':
         return 'no'
      else:
         return 'no'
   elif obj[3] == '45-49':
      return 'no'
   elif obj[3] == '0-4':
      return 'no'
   else:
      return 'no'
