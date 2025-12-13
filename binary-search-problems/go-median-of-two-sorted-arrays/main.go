package leetcode

import "math"

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	// ensure starting with smaller array
	if len(nums1) > len(nums2) {
		return findMedianSortedArrays(nums2, nums1)
	}

	len_n1, len_n2 := len(nums1), len(nums2)

	left, right := 0, len_n1

	for left <= right {
		// create partitions
		partition_n1 := left + (right-left)/2
		partition_n2 := (len_n1+len_n2+1)/2 - partition_n1

		// set max left, if its the beginning of the array, set to -infinity
		maxLeft_n1 := math.Inf(-1)
		if partition_n1 > 0 {
			maxLeft_n1 = float64(nums1[partition_n1-1])
		}
		// set min right, if it is the last element, set to +infinity
		minRight_n1 := math.Inf(1)
		if partition_n1 < len_n1 {
			minRight_n1 = float64(nums1[partition_n1])
		}

		// logic above applied to the second array
		maxLeft_n2 := math.Inf(-1)
		if partition_n2 > 0 {
			maxLeft_n2 = float64(nums2[partition_n2-1])
		}
		minRight_n2 := math.Inf(1)
		if partition_n2 < len_n2 {
			minRight_n2 = float64(nums2[partition_n2])
		}

		// verify it is a valid partition
		if maxLeft_n1 <= minRight_n2 && maxLeft_n2 <= minRight_n1 {
			// partition meets requirements
			if (len_n1+len_n2)%2 == 0 {
				// if even amount of elements return the average of the 2 middle values
				return (max(maxLeft_n1, maxLeft_n2) + min(minRight_n1, minRight_n2)) / 2
			} else {
				// if odd amount of elements return the middle value
				return max(maxLeft_n1, maxLeft_n2)
			}
		} else if maxLeft_n1 > minRight_n2 {
			// partition is too long
			right = partition_n1 - 1
		} else {
			// partition is not long enough
			left = partition_n1 + 1
		}
	}

	panic("Invalid Input")
}
