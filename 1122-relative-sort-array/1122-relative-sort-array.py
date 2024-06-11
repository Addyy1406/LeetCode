class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Create a dictionary to store the indices of elements in arr2
        index_map = {num: i for i, num in enumerate(arr2)}
        
        # Define a custom sorting function
        def custom_sort(num):
            if num in index_map:
                return (0, index_map[num])  # Sort by appearance order in arr2
            else:
                return (1, num)  # Sort other elements at the end in ascending order
        
        # Sort arr1 using the custom sorting function
        arr1.sort(key=custom_sort)
        
        return arr1