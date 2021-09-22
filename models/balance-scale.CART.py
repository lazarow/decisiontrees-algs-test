def findDecision(obj): #obj[0]: 0, obj[1]: 1, obj[2]: 2, obj[3]: 3
   # {"feature": "0", "instances": 250, "metric_value": 0.496, "depth": 1}
   if obj[0]>2:
      # {"feature": "1", "instances": 139, "metric_value": 0.3998, "depth": 2}
      if obj[1]>1:
         # {"feature": "2", "instances": 113, "metric_value": 0.3616, "depth": 3}
         if obj[2]<=3:
            # {"feature": "3", "instances": 69, "metric_value": 0.1814, "depth": 4}
            if obj[3]<=4:
               return 'L'
            elif obj[3]>4:
               return 'L'
            else:
               return 'L'
         elif obj[2]>3:
            # {"feature": "3", "instances": 44, "metric_value": 0.4036, "depth": 4}
            if obj[3]<=3:
               return 'L'
            elif obj[3]>3:
               return 'R'
            else:
               return 'R'
         else:
            return 'L'
      elif obj[1]<=1:
         # {"feature": "2", "instances": 26, "metric_value": 0.1918, "depth": 3}
         if obj[2]>1:
            # {"feature": "3", "instances": 23, "metric_value": 0.087, "depth": 4}
            if obj[3]>1:
               return 'R'
            elif obj[3]<=1:
               return 'L'
            else:
               return 'L'
         elif obj[2]<=1:
            # {"feature": "3", "instances": 3, "metric_value": 0.0, "depth": 4}
            if obj[3]<=3:
               return 'L'
            elif obj[3]>3:
               return 'B'
            else:
               return 'B'
         else:
            return 'L'
      else:
         return 'R'
   elif obj[0]<=2:
      # {"feature": "3", "instances": 111, "metric_value": 0.3955, "depth": 2}
      if obj[3]>2:
         # {"feature": "2", "instances": 63, "metric_value": 0.1817, "depth": 3}
         if obj[2]>1:
            # {"feature": "1", "instances": 54, "metric_value": 0.0955, "depth": 4}
            if obj[1]<=4:
               return 'R'
            elif obj[1]>4:
               return 'R'
            else:
               return 'R'
         elif obj[2]<=1:
            # {"feature": "1", "instances": 9, "metric_value": 0.5556, "depth": 4}
            if obj[1]<=4:
               return 'R'
            elif obj[1]>4:
               return 'B'
            else:
               return 'B'
         else:
            return 'R'
      elif obj[3]<=2:
         # {"feature": "1", "instances": 48, "metric_value": 0.4468, "depth": 3}
         if obj[1]>2:
            # {"feature": "2", "instances": 29, "metric_value": 0.3454, "depth": 4}
            if obj[2]<=4:
               return 'L'
            elif obj[2]>4:
               return 'R'
            else:
               return 'R'
         elif obj[1]<=2:
            # {"feature": "2", "instances": 19, "metric_value": 0.25, "depth": 4}
            if obj[2]>2:
               return 'R'
            elif obj[2]<=2:
               return 'B'
            else:
               return 'B'
         else:
            return 'R'
      else:
         return 'L'
   else:
      return 'R'
