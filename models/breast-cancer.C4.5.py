def findDecision(obj): #obj[0]: 0, obj[1]: 1, obj[2]: 2, obj[3]: 3, obj[4]: 4, obj[5]: 5, obj[6]: 6, obj[7]: 7, obj[8]: 8
   # {"feature": "5", "instances": 114, "metric_value": 0.8043, "depth": 1}
   if obj[5] == 'no':
      # {"feature": "4", "instances": 88, "metric_value": 0.6041, "depth": 2}
      if obj[4] == '0-2':
         # {"feature": "3", "instances": 82, "metric_value": 0.5349, "depth": 3}
         if obj[3] == '30-34':
            # {"feature": "1", "instances": 16, "metric_value": 0.6962, "depth": 4}
            if obj[1] == '50-59':
               return 'no'
            elif obj[1] == '40-49':
               # {"feature": "6", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[6]<=2:
                  # {"feature": "8", "instances": 4, "metric_value": 0.8113, "depth": 6}
                  if obj[8] == 'right_up':
                     return 'yes'
                  elif obj[8] == 'left_low':
                     return 'yes'
                  elif obj[8] == 'right_low':
                     return 'no'
                  elif obj[8] == 'left_up':
                     return 'yes'
                  else:
                     return 'yes'
               elif obj[6]>2:
                  return 'no'
               else:
                  return 'no'
            elif obj[1] == '60-69':
               return 'no'
            elif obj[1] == '30-39':
               return 'no'
            else:
               return 'no'
         elif obj[3] == '25-29':
            # {"feature": "7", "instances": 14, "metric_value": 0.5917, "depth": 4}
            if obj[7] == 'left':
               return 'no'
            elif obj[7] == 'right':
               # {"feature": "0", "instances": 6, "metric_value": 0.9183, "depth": 5}
               if obj[0] == 'no-recurrence-events':
                  # {"feature": "1", "instances": 5, "metric_value": 0.7219, "depth": 6}
                  if obj[1] == '60-69':
                     return 'no'
                  elif obj[1] == '50-59':
                     return 'no'
                  elif obj[1] == '40-49':
                     return 'yes'
                  else:
                     return 'yes'
               elif obj[0] == 'recurrence-events':
                  return 'yes'
               else:
                  return 'yes'
            else:
               return 'no'
         elif obj[3] == '10-14':
            return 'no'
         elif obj[3] == '15-19':
            # {"feature": "6", "instances": 10, "metric_value": 0.469, "depth": 4}
            if obj[6]<=2:
               return 'no'
            elif obj[6]>2:
               # {"feature": "1", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[1] == '60-69':
                  return 'yes'
               elif obj[1] == '30-39':
                  return 'no'
               else:
                  return 'no'
            else:
               return 'yes'
         elif obj[3] == '20-24':
            # {"feature": "0", "instances": 10, "metric_value": 0.469, "depth": 4}
            if obj[0] == 'no-recurrence-events':
               return 'no'
            elif obj[0] == 'recurrence-events':
               # {"feature": "1", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[1] == '30-39':
                  return 'yes'
               elif obj[1] == '40-49':
                  return 'no'
               else:
                  return 'no'
            else:
               return 'yes'
         elif obj[3] == '40-44':
            return 'no'
         elif obj[3] == '35-39':
            return 'no'
         elif obj[3] == '50-54':
            # {"feature": "7", "instances": 5, "metric_value": 0.971, "depth": 4}
            if obj[7] == 'right':
               # {"feature": "6", "instances": 3, "metric_value": 0.9183, "depth": 5}
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
            # {"feature": "1", "instances": 2, "metric_value": 1.0, "depth": 4}
            if obj[1] == '40-49':
               return 'yes'
            elif obj[1] == '30-39':
               return 'no'
            else:
               return 'no'
         elif obj[3] == '0-4':
            return 'no'
         else:
            return 'no'
      elif obj[4] == '3-5':
         # {"feature": "1", "instances": 6, "metric_value": 1.0, "depth": 3}
         if obj[1] == '60-69':
            return 'yes'
         elif obj[1] == '50-59':
            # {"feature": "0", "instances": 2, "metric_value": 1.0, "depth": 4}
            if obj[0] == 'no-recurrence-events':
               return 'yes'
            elif obj[0] == 'recurrence-events':
               return 'no'
            else:
               return 'no'
         elif obj[1] == '40-49':
            return 'no'
         elif obj[1] == '30-39':
            return 'no'
         else:
            return 'no'
      else:
         return 'no'
   elif obj[5] == 'yes':
      # {"feature": "3", "instances": 22, "metric_value": 0.994, "depth": 2}
      if obj[3] == '30-34':
         # {"feature": "0", "instances": 7, "metric_value": 0.9852, "depth": 3}
         if obj[0] == 'recurrence-events':
            # {"feature": "2", "instances": 5, "metric_value": 0.971, "depth": 4}
            if obj[2] == 'ge40':
               # {"feature": "6", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[6]<=2:
                  return 'yes'
               elif obj[6]>2:
                  # {"feature": "4", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[4] == '6-8':
                     return 'no'
                  elif obj[4] == '9-11':
                     return 'yes'
                  else:
                     return 'yes'
               else:
                  return 'no'
            elif obj[2] == 'premeno':
               return 'no'
            else:
               return 'no'
         elif obj[0] == 'no-recurrence-events':
            return 'no'
         else:
            return 'no'
      elif obj[3] == '25-29':
         # {"feature": "8", "instances": 4, "metric_value": 0.8113, "depth": 3}
         if obj[8] == 'left_up':
            return 'no'
         elif obj[8] == 'right_low':
            return 'yes'
         else:
            return 'yes'
      elif obj[3] == '35-39':
         # {"feature": "0", "instances": 3, "metric_value": 0.9183, "depth": 3}
         if obj[0] == 'no-recurrence-events':
            return 'yes'
         elif obj[0] == 'recurrence-events':
            return 'no'
         else:
            return 'no'
      elif obj[3] == '20-24':
         # {"feature": "0", "instances": 2, "metric_value": 1.0, "depth": 3}
         if obj[0] == 'recurrence-events':
            return 'yes'
         elif obj[0] == 'no-recurrence-events':
            return 'no'
         else:
            return 'no'
      elif obj[3] == '40-44':
         return 'yes'
      elif obj[3] == '15-19':
         return 'yes'
      elif obj[3] == '45-49':
         return 'no'
      elif obj[3] == '50-54':
         return 'yes'
      else:
         return 'yes'
   elif obj[5] == '?':
      # {"feature": "0", "instances": 4, "metric_value": 0.8113, "depth": 2}
      if obj[0] == 'no-recurrence-events':
         return 'yes'
      elif obj[0] == 'recurrence-events':
         return 'no'
      else:
         return 'no'
   else:
      return 'yes'
