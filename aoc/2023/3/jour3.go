package main

import (
	_ "embed"
	"fmt"
	"strings"
)

//go:embed jour3.txt
var input string

type context struct {
	start, end, value int
}

func getInt(line string) []context {
	var ret []context
	var start int
	var temp int
	for index, chr := range []byte(line) {
		if chr < 48 || chr > 57 {
			if temp != 0 {
				ret = append(ret, context{start, index - 1, temp})
			}
			start = index + 1
			temp = 0
		} else {
			temp = 10*temp + (int(chr) - 48)
		}
	}
	if temp != 0 {
		ret = append(ret, context{start, len(line) - 1, temp})
	}
	return ret
}

func find(lst []context, index int) ([]context, int) {
	var sum int
	var tmp []context
	for _, cont := range lst {
		if (cont.end <= index+1 && cont.end >= index-1) || (cont.start <= index+1 && cont.start >= index-1) || (index >= cont.start && index <= cont.end) {
			sum += cont.value
		} else {
			tmp = append(tmp, cont)
		}
	}
	return lst, sum
}

func findR(lst []context, index int) (int, int) {
	var sum = 1
	var cpt int
	for _, cont := range lst {
		if (cont.end <= index+1 && cont.end >= index-1) || (cont.start <= index+1 && cont.start >= index-1) || (index >= cont.start && index <= cont.end) {
			sum *= cont.value
			cpt++
		}
	}
	return sum, cpt
}

func findAll(top, middle, bottom []context, index int) ([]context, []context, []context, int) {
	var sum int
	top, tmp1 := find(top, index)
	bottom, tmp3 := find(bottom, index)

	var tmp2 int
	var contmp []context
	for _, cont := range middle {
		if cont.start-1 == index || cont.end+1 == index {
			tmp2 += cont.value
		} else {
			contmp = append(contmp, cont)
		}
	}

	sum = tmp1 + tmp2 + tmp3
	return top, contmp, bottom, sum
}

func findRatio(top, middle, bottom []context, index int) int {
	gear1, cpt1 := findR(top, index)
	gear3, cpt3 := findR(bottom, index)
	var cpt2 int

	var gear2 = 1
	for _, cont := range middle {
		if cpt1+cpt2+cpt3 > 2 {
			break
		}
		if cont.start-1 == index || cont.end+1 == index {
			gear2 *= cont.value
			cpt3++
		}
	}
	//fmt.Println(gear1 * gear2 * gear3)
	if cpt1+cpt2+cpt3 == 2 {

		return gear1 * gear2 * gear3
	}
	return 0
}

func jour3_p1() {
	lines := strings.Split(input, "\n")

	var top []context
	var middle = getInt(lines[0])
	var bottom = getInt(lines[1])
	var sum int
	for index, line := range lines {
		for i, chr := range []byte(line) {
			if (chr < 48 || chr > 57) && chr != 46 { //not an int and not a point
				var tmp int
				top, middle, bottom, tmp = findAll(top, middle, bottom, i)
				sum += tmp

			}
		}

		top = middle
		middle = bottom
		if index >= len(lines)-2 {
			bottom = []context{}
		} else {
			bottom = getInt(lines[index+2])
		}
	}
	fmt.Println(sum)
}

func jour3_p2() {
	lines := strings.Split(input, "\n")

	var top []context
	var middle = getInt(lines[0])
	var bottom = getInt(lines[1])
	var sum int
	for index, line := range lines {
		for i, chr := range []byte(line) {
			if chr == 42 { // exactly a *
				sum += findRatio(top, middle, bottom, i)
			}
		}

		top = middle
		middle = bottom
		if index >= len(lines)-2 {
			bottom = []context{}
		} else {
			bottom = getInt(lines[index+2])
		}
	}
	fmt.Println(sum)
}
func main() {
	jour3_p1()
	jour3_p2()
}
