def findDecision(obj): #obj[0]: 0, obj[1]: 1, obj[2]: 2, obj[3]: 3
   # {"feature": "0", "instances": 250, "metric_value": 1.3116, "depth": 1}
   if obj[0]>1:
      # {"feature": "1", "instances": 200, "metric_value": 1.2501, "depth": 2}
      if obj[1]>1:
         # {"feature": "2", "instances": 163, "metric_value": 1.1885, "depth": 3}
         if obj[2]<=3:
            # {"feature": "3", "instances": 95, "metric_value": 0.7907, "depth": 4}
            if obj[3]>2:
               return 'L'
            elif obj[3]<=2:
               return 'L'
            else:
               return 'L'
         elif obj[2]>3:
            # {"feature": "3", "instances": 68, "metric_value": 1.3612, "depth": 4}
            if obj[3]<=3:
               return 'L'
            elif obj[3]>3:
               return 'R'
            else:
               return 'R'
         else:
            return 'R'
      elif obj[1]<=1:
         # {"feature": "2", "instances": 37, "metric_value": 0.6689, "depth": 3}
         if obj[2]>1:
            # {"feature": "3", "instances": 34, "metric_value": 0.3228, "depth": 4}
            if obj[3]>1:
               return 'R'
            elif obj[3]<=1:
               return 'R'
            else:
               return 'R'
         elif obj[2]<=1:
            # {"feature": "3", "instances": 3, "metric_value": 0.9183, "depth": 4}
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
   elif obj[0]<=1:
      # {"feature": "3", "instances": 50, "metric_value": 0.9682, "depth": 2}
      if obj[3]>2:
         # {"feature": "2", "instances": 28, "metric_value": 0.3712, "depth": 3}
         if obj[2]>1:
            return 'R'
         elif obj[2]<=1:
            # {"feature": "1", "instances": 6, "metric_value": 0.9183, "depth": 4}
            if obj[1]<=3:
               return 'R'
            elif obj[1]>3:
               return 'B'
            else:
               return 'B'
         else:
            return 'R'
      elif obj[3]<=2:
         # {"feature": "2", "instances": 22, "metric_value": 1.3815, "depth": 3}
         if obj[2]>2:
            # {"feature": "1", "instances": 13, "metric_value": 0.7732, "depth": 4}
            if obj[1]<=4:
               return 'R'
            elif obj[1]>4:
               return 'R'
            else:
               return 'R'
         elif obj[2]<=2:
            # {"feature": "1", "instances": 9, "metric_value": 1.5305, "depth": 4}
            if obj[1]<=2:
               return 'B'
            elif obj[1]>2:
               return 'L'
            else:
               return 'L'
         else:
            return 'B'
      else:
         return 'R'
   else:
      return 'R'
