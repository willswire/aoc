package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reports := parseReports()
	fmt.Println(reports)

	numOfSafeReports := 0
	for _, report := range reports {
		if isSafe(report) {
			numOfSafeReports++
		}
	}
	fmt.Println(numOfSafeReports)
}

func isSafe(report []int) bool {
	if len(report) < 2 {
		return false
	}

	firstDiff := report[1] - report[0]
	if firstDiff == 0 || abs(firstDiff) > 3 {
		return false
	}

	isIncreasing := firstDiff > 0

	for i := 1; i < len(report); i++ {
		diff := report[i] - report[i-1]

		if abs(diff) < 1 || abs(diff) > 3 {
			return false
		}

		if isIncreasing && diff <= 0 {
			return false
		}
		if !isIncreasing && diff >= 0 {
			return false
		}
	}

	return true
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func parseReports() (reports [][]int) {
	filename := "input.txt"
	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return [][]int{{}}
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		report := scanner.Text()
		levels := strings.Split(report, " ")

		reportRow := []int{}
		for _, level := range levels {
			num, err := strconv.Atoi(level)
			if err != nil {
				fmt.Println("Error parsing report:", err)
				return [][]int{{}}
			}
			reportRow = append(reportRow, num)
		}
		reports = append(reports, reportRow)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
	}

	return reports
}
