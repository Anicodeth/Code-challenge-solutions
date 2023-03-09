class Solution:

    def getRow(self, rowIndex: int) -> List[int]:
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

      pascal([1], 0,rowIndex+2)
      return items[-1] if rowIndex!=0 else [1]
