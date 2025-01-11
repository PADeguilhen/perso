package main

import (
	_ "embed"
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

//go:embed jour2.txt
var input string

type rgb struct {
	r, g, b int
}

func retMax(lst [][]string) int {
	digit := regexp.MustCompile("[0-9]+")
	var max int
	for _, value := range lst {
		i, err := strconv.Atoi(digit.FindStringSubmatch(value[0])[0])
		if err != nil {
			panic(err)
		}
		if i > max {
			max = i
		}
	}
	return max
}

func powRGB(maxi rgb) int {
	return maxi.b * maxi.g * maxi.r
}

func conp(temp, cons rgb) bool {
	return temp.r <= cons.r && temp.b <= cons.b && temp.g <= cons.g
}

func jour2_p1() {
	lines := strings.Split(input, "\n")

	digit := regexp.MustCompile("[0-9]+")
	red := regexp.MustCompile("[[0-9]+ red]*")
	green := regexp.MustCompile("[[0-9]+ green]*")
	blue := regexp.MustCompile("[[0-9]+ blue]*")

	target := rgb{12, 13, 14}
	var sum int
	for _, line := range lines {
		var partiel rgb
		partiel.r = retMax(red.FindAllStringSubmatch(line, -1))
		partiel.g = retMax(green.FindAllStringSubmatch(line, -1))
		partiel.b = retMax(blue.FindAllStringSubmatch(line, -1))

		if conp(partiel, target) {
			var incr, _ = strconv.Atoi(digit.FindStringSubmatch(line)[0])
			sum += incr
		}
	}
	fmt.Println(sum)
}

func jour2_p2() {
	lines := strings.Split(input, "\n")

	red := regexp.MustCompile("[[0-9]+ red]*")
	green := regexp.MustCompile("[[0-9]+ green]*")
	blue := regexp.MustCompile("[[0-9]+ blue]*")

	var sum int
	for _, line := range lines {
		var partiel rgb
		partiel.r = retMax(red.FindAllStringSubmatch(line, -1))
		partiel.g = retMax(green.FindAllStringSubmatch(line, -1))
		partiel.b = retMax(blue.FindAllStringSubmatch(line, -1))

		sum += powRGB(partiel)
	}
	fmt.Println(sum)
}

func main() {
	// jour2_p1()
	jour2_p2()
}
