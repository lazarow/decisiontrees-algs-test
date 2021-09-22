def findDecision(obj): #obj[0]: 0, obj[1]: 1, obj[2]: 2, obj[3]: 3
   # {"feature": "1", "instances": 250, "metric_value": 24.9679, "depth": 1}
   if obj[1]>1:
      # {"feature": "0", "instances": 204, "metric_value": 24.0935, "depth": 2}
      if obj[0]>2:
         # {"feature": "2", "instances": 113, "metric_value": 21.8993, "depth": 3}
         if obj[2]>1:
            # {"feature": "3", "instances": 92, "metric_value": 17.99, "depth": 4}
            if obj[3]<=3:
               return 'L'
            elif obj[3]>3:
               return 'R'
            else:
               return 'R'
         elif obj[2]<=1:
            return 'L'
         else:
            return 'L'
      elif obj[0]<=2:
         # {"feature": "3", "instances": 91, "metric_value": 17.3286, "depth": 3}
         if obj[3]>1:
            # {"feature": "2", "instances": 71, "metric_value": 17.2722, "depth": 4}
            if obj[2]<=4:
               return 'R'
            elif obj[2]>4:
               return 'R'
            else:
               return 'R'
         elif obj[3]<=1:
            # {"feature": "2", "instances": 20, "metric_value": 8.7417, "depth": 4}
            if obj[2]>1:
               return 'L'
            elif obj[2]<=1:
               return 'L'
            else:
               return 'L'
         else:
            return 'L'
      else:
         return 'R'
   elif obj[1]<=1:
      # {"feature": "2", "instances": 46, "metric_value": 18.0274, "depth": 2}
      if obj[2]<=3:
         # {"feature": "3", "instances": 26, "metric_value": 11.1367, "depth": 3}
         if obj[3]>1:
            # {"feature": "0", "instances": 21, "metric_value": 12.9282, "depth": 4}
            if obj[0]>2:
               return 'R'
            elif obj[0]<=2:
               return 'R'
            else:
               return 'R'
         elif obj[3]<=1:
            # {"feature": "0", "instances": 5, "metric_value": 5.633, "depth": 4}
            if obj[0]>2:
               return 'L'
            elif obj[0]<=2:
               return 'R'
            else:
               return 'R'
         else:
            return 'L'
      elif obj[2]>3:
         return 'R'
      else:
         return 'R'
   else:
      return 'R'
