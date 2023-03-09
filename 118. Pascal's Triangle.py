class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
      items = []
      def pascal(row , index, numsRows):
        if index+1 == numsRows:
          return 0
        else:
          arr = [1]*(index+1)     
          for i in range(1,len(arr)-1):
            arr[i]= items[index-1][i-1] +  items[index-1][i]
          items.append(arr)
          pascal(arr, index+1, numsRows)

      pascal([1], 0, numRows+1)
      return items

        
