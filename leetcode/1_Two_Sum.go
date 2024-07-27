func twoSum(nums []int, target int) []int {
	var result []int

	myMap := map[int]int{}

	/*
	       1 2 3 4 5 6    target 9
	               ^
	       myMap = {
	           8: 0,
	           7: 1,
	           6: 2,
	           5: 3,
	       }

	   return []int{current_index, myMap[current_value]}
	*/

	for i := 0; i < len(nums); i++ {
		currentNumber := nums[i]
		secondNumberIndex, ok := myMap[currentNumber]
		if ok {
			result = append(result, i, secondNumberIndex)
			break
		}
		secondNumber := target - currentNumber
		myMap[secondNumber] = i
	}
	return result
}
