"""Merge Sort Implementation - Stable sorting algorithm."""

from typing import List, Any, Callable, Optional


class MergeSort:
    """Merge Sort algorithm with performance tracking."""
    
    def __init__(self):
        self.comparisons = 0
        self.operations = 0
    
    def sort(self, arr: List[Any], key: Optional[Callable] = None, reverse: bool = False) -> List[Any]:
        """Sort array using Merge Sort algorithm.
        
        Args:
            arr: List to sort
            key: Optional function to extract comparison key
            reverse: Sort in descending order if True
        
        Returns:
            Sorted list
        """
        self.comparisons = 0
        self.operations = 0
        
        if not arr or len(arr) <= 1:
            return arr
        
        arr_copy = arr.copy()
        self._mergesort(arr_copy, 0, len(arr_copy) - 1, key, reverse)
        return arr_copy
    
    def _mergesort(self, arr: List[Any], left: int, right: int,
                   key: Optional[Callable], reverse: bool) -> None:
        """Internal merge sort implementation."""
        if left < right:
            mid = (left + right) // 2
            self._mergesort(arr, left, mid, key, reverse)
            self._mergesort(arr, mid + 1, right, key, reverse)
            self._merge(arr, left, mid, right, key, reverse)
    
    def _merge(self, arr: List[Any], left: int, mid: int, right: int,
               key: Optional[Callable], reverse: bool) -> None:
        """Merge two sorted subarrays."""
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(left_arr) and j < len(right_arr):
            left_val = key(left_arr[i]) if key else left_arr[i]
            right_val = key(right_arr[j]) if key else right_arr[j]
            self.comparisons += 1
            
            cond = left_val > right_val if reverse else left_val <= right_val
            if cond:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
            self.operations += 1
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            self.operations += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
            self.operations += 1
