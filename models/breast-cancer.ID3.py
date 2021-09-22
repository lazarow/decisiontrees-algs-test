def findDecision(obj): #obj[0]: 0, obj[1]: 1, obj[2]: 2, obj[3]: 3, obj[4]: 4, obj[5]: 5, obj[6]: 6, obj[7]: 7, obj[8]: 8
   # {"feature": "4", "instances": 114, "metric_value": 0.8043, "depth": 1}
   if obj[4] == '0-2':
      # {"feature": "3", "instances": 87, "metric_value": 0.6084, "depth": 2}
      if obj[3] == '30-34':
         # {"feature": "1", "instances": 16, "metric_value": 0.6962, "depth": 3}
         if obj[1] == '50-59':
            return 'no'
         elif obj[1] == '40-49':
            # {"feature": "8", "instances": 5, "metric_value": 0.971, "depth": 4}
            if obj[8] == 'right_up':
               # {"feature": "6", "instances": 2, "metric_value": 1.0, "depth": 5}
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
      elif obj[3] == '25-29':
         # {"feature": "7", "instances": 15, "metric_value": 0.5665, "depth": 3}
         if obj[7] == 'left':
            return 'no'
         elif obj[7] == 'right':
            # {"feature": "1", "instances": 6, "metric_value": 0.9183, "depth": 4}
            if obj[1] == '50-59':
               # {"feature": "0", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[0] == 'no-recurrence-events':
                  return 'no'
               elif obj[0] == 'recurrence-events':
                  return 'yes'
               else:
                  return 'yes'
            elif obj[1] == '60-69':
               return 'no'
            elif obj[1] == '40-49':
               return 'yes'
            else:
               return 'yes'
         else:
            return 'no'
      elif obj[3] == '15-19':
         # {"feature": "5", "instances": 11, "metric_value": 0.684, "depth": 3}
         if obj[5] == 'no':
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
         elif obj[5] == 'yes':
            return 'yes'
         else:
            return 'yes'
      elif obj[3] == '20-24':
         # {"feature": "1", "instances": 11, "metric_value": 0.4395, "depth": 3}
         if obj[1] == '50-59':
            return 'no'
         elif obj[1] == '40-49':
            return 'no'
         elif obj[1] == '30-39':
            # {"feature": "0", "instances": 2, "metric_value": 1.0, "depth": 4}
            if obj[0] == 'no-recurrence-events':
               return 'no'
            elif obj[0] == 'recurrence-events':
               return 'yes'
            else:
               return 'yes'
         elif obj[1] == '60-69':
            return 'no'
         else:
            return 'no'
      elif obj[3] == '10-14':
         return 'no'
      elif obj[3] == '40-44':
         return 'no'
      elif obj[3] == '35-39':
         # {"feature": "5", "instances": 7, "metric_value": 0.5917, "depth": 3}
         if obj[5] == 'no':
            return 'no'
         elif obj[5] == 'yes':
            return 'yes'
         else:
            return 'yes'
      elif obj[3] == '50-54':
         # {"feature": "7", "instances": 6, "metric_value": 1.0, "depth": 3}
         if obj[7] == 'right':
            # {"feature": "6", "instances": 4, "metric_value": 0.8113, "depth": 4}
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
         # {"feature": "1", "instances": 2, "metric_value": 1.0, "depth": 3}
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
      # {"feature": "1", "instances": 11, "metric_value": 0.9457, "depth": 2}
      if obj[1] == '60-69':
         return 'yes'
      elif obj[1] == '40-49':
         # {"feature": "5", "instances": 3, "metric_value": 0.9183, "depth": 3}
         if obj[5] == 'yes':
            return 'yes'
         elif obj[5] == 'no':
            return 'no'
         else:
            return 'no'
      elif obj[1] == '50-59':
         # {"feature": "3", "instances": 3, "metric_value": 0.9183, "depth": 3}
         if obj[3] == '25-29':
            return 'yes'
         elif obj[3] == '30-34':
            return 'no'
         elif obj[3] == '20-24':
            return 'no'
         else:
            return 'no'
      elif obj[1] == '30-39':
         return 'no'
      else:
         return 'no'
   elif obj[4] == '6-8':
      # {"feature": "1", "instances": 8, "metric_value": 0.9544, "depth": 2}
      if obj[1] == '60-69':
         return 'no'
      elif obj[1] == '50-59':
         # {"feature": "0", "instances": 3, "metric_value": 0.9183, "depth": 3}
         if obj[0] == 'recurrence-events':
            # {"feature": "6", "instances": 2, "metric_value": 1.0, "depth": 4}
            if obj[6]<=2:
               return 'yes'
            elif obj[6]>2:
               return 'no'
            else:
               return 'no'
         elif obj[0] == 'no-recurrence-events':
            return 'no'
         else:
            return 'no'
      elif obj[1] == '30-39':
         return 'yes'
      else:
         return 'yes'
   elif obj[4] == '9-11':
      # {"feature": "3", "instances": 5, "metric_value": 0.7219, "depth": 2}
      if obj[3] == '30-34':
         return 'yes'
      elif obj[3] == '35-39':
         return 'yes'
      elif obj[3] == '25-29':
         return 'no'
      else:
         return 'no'
   elif obj[4] == '15-17':
      # {"feature": "3", "instances": 3, "metric_value": 0.9183, "depth": 2}
      if obj[3] == '30-34':
         return 'no'
      elif obj[3] == '25-29':
         return 'no'
      elif obj[3] == '40-44':
         return 'yes'
      else:
         return 'yes'
   else:
      return 'no'
