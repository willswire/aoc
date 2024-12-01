package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func main() {
	left, right := parseLists()
	slices.Sort(left)
	slices.Sort(right)
	distance := computeDistance(left, right)
	fmt.Println("Distance:", distance)

	frequencyMap := computeFrequency(right)
	similarityScore := computeSimilarityScore(left, frequencyMap)
	fmt.Println("Similarity Score:", similarityScore)
}

func parseLists() ([]int, []int) {
	filename := "input.txt"
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return []int{}, []int{}
	}

	defer file.Close()

	var left, right []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		ids := strings.Split(line, "   ")
		leftE, err := strconv.Atoi(ids[0])
		if err != nil {
			fmt.Println("Error parsing left ID:", err)
			return []int{}, []int{}
		}
		left = append(left, leftE)

		rightE, err := strconv.Atoi(ids[1])
		if err != nil {
			fmt.Println("Error parsing right ID:", err)
			return []int{}, []int{}
		}
		right = append(right, rightE)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
	}

	return left, right
}

func computeDistance(left []int, right []int) int {
	distance := 0
	for i := 0; i < len(left) && i < len(right); i++ {
		distance += abs(right[i] - left[i])
	}
	return distance
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func computeFrequency(right []int) map[int]int {
	frequencyMap := make(map[int]int)
	for _, num := range right {
		frequencyMap[num]++
	}
	return frequencyMap
}

func computeSimilarityScore(left []int, frequencyMap map[int]int) int {
	similarityScore := 0
	for _, num := range left {
		similarityScore += num * frequencyMap[num]
	}
	return similarityScore
}
