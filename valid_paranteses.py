class Solution:
   def isValid( self, sequence ):
       '''
       Function to check if sequence contains valid parenthesis
       :param sequence: Sequence of brackets
       :return: True is sequence is valid else False
       '''
       # Replace the proper pairs until sequence becomes empty or no pairs are present
       while True:
           if '()' in sequence :
               sequence = sequence.replace ( '()' , '' )
           elif '{}' in sequence :
               sequence = sequence.replace ( '{}' , '' )
           elif '[]' in sequence :
               sequence = sequence.replace ( '[]' , '' )
           else :
               return not sequence

if __name__ == '__main__':
   sequence = '{[()]}'
   print(f'Is {sequence} valid ? : {Solution().isValid(sequence)}')
   sequence1 = '{[()]}{]{}}'
   print(f'Is {sequence1} valid ? : {Solution().isValid (sequence1)}')