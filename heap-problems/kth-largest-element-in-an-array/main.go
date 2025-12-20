package leetcode

import (
	"container/heap"
)

type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(j, k int) bool { return h[j] < h[k] }
func (h MinHeap) Swap(j, k int)      { h[j], h[k] = h[k], h[j] }
func (h *MinHeap) Push(val any) {
	*h = append(*h, val.(int))
}

func (h *MinHeap) Pop() any {
	prev := *h
	n := len(prev)
	popped_val := prev[n-1]
	*h = prev[:n-1]
	return popped_val
}

func findKthLargest(nums []int, k int) int {
	h := &MinHeap{}
	heap.Init(h)
	for _, val := range nums {
		heap.Push(h, val)
		if h.Len() > k {
			heap.Pop(h)
		}
	}
	return (*h)[0]
}
