"""Quick Sort Implementation - Efficient general-purpose sorting."""

from typing import List, Any, Callable, Optional


class QuickSort:
    """Quick Sort algorithm with performance tracking."""
    
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
    
    def sort(self, arr: List[Any], key: Optional[Callable] = None, reverse: bool = False) -> List[Any]:
        """Sort array using Quick Sort algorithm.
        
        Args:
            arr: List to sort
            key: Optional function to extract comparison key
            reverse: Sort in descending order if True
        
        Returns:
            Sorted list
        """
        self.comparisons = 0
        self.swaps = 0
        
        if not arr or len(arr) <= 1:
            return arr
        
        arr_copy = arr.copy()
        self._quicksort(arr_copy, 0, len(arr_copy) - 1, key, reverse)
        return arr_copy
    
    def _quicksort(self, arr: List[Any], low: int, high: int, 
                   key: Optional[Callable], reverse: bool) -> None:
        """Internal quick sort implementation."""
        if low < high:
            pi = self._partition(arr, low, high, key, reverse)
            self._quicksort(arr, low, pi - 1, key, reverse)
            self._quicksort(arr, pi + 1, high, key, reverse)
    
    def _partition(self, arr: List[Any], low: int, high: int,
                   key: Optional[Callable], reverse: bool) -> int:
        """Partition array for quick sort."""
        pivot = arr[high]
        pivot_val = key(pivot) if key else pivot
        
        i = low - 1
        for j in range(low, high):
            val = key(arr[j]) if key else arr[j]
            self.comparisons += 1
            
            cond = val > pivot_val if reverse else val < pivot_val
            if cond:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.swaps += 1
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.swaps += 1
        return i + 1
