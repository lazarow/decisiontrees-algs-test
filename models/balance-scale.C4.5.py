def findDecision(obj): #obj[0]: 0, obj[1]: 1, obj[2]: 2, obj[3]: 3
   # {"feature": "1", "instances": 250, "metric_value": 1.3116, "depth": 1}
   if obj[1]>1:
      # {"feature": "0", "instances": 204, "metric_value": 1.3122, "depth": 2}
      if obj[0]>1:
         # {"feature": "3", "instances": 163, "metric_value": 1.1885, "depth": 3}
         if obj[3]>1:
            # {"feature": "2", "instances": 133, "metric_value": 1.2938, "depth": 4}
            if obj[2]>1:
               return 'L'
            elif obj[2]<=1:
               return 'L'
            else:
               return 'L'
         elif obj[3]<=1:
            return 'L'
         else:
            return 'L'
      elif obj[0]<=1:
         # {"feature": "3", "instances": 41, "metric_value": 1.0383, "depth": 3}
         if obj[3]>2:
            # {"feature": "2", "instances": 24, "metric_value": 0.4138, "depth": 4}
            if obj[2]>1:
               return 'R'
            elif obj[2]<=1:
               return 'R'
            else:
               return 'R'
         elif obj[3]<=2:
            # {"feature": "2", "instances": 17, "metric_value": 1.4681, "depth": 4}
            if obj[2]>2:
               return 'R'
            elif obj[2]<=2:
               return 'L'
            else:
               return 'L'
         else:
            return 'R'
      else:
         return 'R'
   elif obj[1]<=1:
      # {"feature": "2", "instances": 46, "metric_value": 0.6784, "depth": 2}
      if obj[2]>1:
         # {"feature": "3", "instances": 41, "metric_value": 0.2812, "depth": 3}
         if obj[3]>1:
            return 'R'
         elif obj[3]<=1:
            # {"feature": "0", "instances": 8, "metric_value": 0.8113, "depth": 4}
            if obj[0]<=3:
               return 'R'
            elif obj[0]>3:
               return 'L'
            else:
               return 'L'
         else:
            return 'R'
      elif obj[2]<=1:
         # {"feature": "0", "instances": 5, "metric_value": 1.5219, "depth": 3}
         if obj[0]>1:
            # {"feature": "3", "instances": 3, "metric_value": 0.9183, "depth": 4}
            if obj[3]<=3:
               return 'L'
            elif obj[3]>3:
               return 'B'
            else:
               return 'B'
         elif obj[0]<=1:
            # {"feature": "3", "instances": 2, "metric_value": 1.0, "depth": 4}
            if obj[3]<=1:
               return 'B'
            elif obj[3]>1:
               return 'R'
            else:
               return 'R'
         else:
            return 'B'
      else:
         return 'B'
   else:
      return 'R'
