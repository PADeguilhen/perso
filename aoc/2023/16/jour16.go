package main

import (
	_ "embed"
	"fmt"
	"strings"
)

//go:embed jour16.txt
var input string

type Point struct{ x, y int }

type Grid map[Point]byte
type Mask map[Point]bool
type Vect struct {
	p   Point
	dir int
}

var lines []string = strings.Split(input, "\n")
var format Point = Point{len(lines[0]), len(lines)}

func (p Point) incr(direction int) Point {
	switch direction {
	case 0: // up
		return Point{p.x, p.y - 1}
	case 1: // left
		return Point{p.x - 1, p.y}
	case 2: // down
		return Point{p.x, p.y + 1}
	case 3: // right
		return Point{p.x + 1, p.y}
	default:
		return p
	}
}

func (p Point) cmp() bool {
	return p.x < format.x && p.y < format.y && p.x >= 0 && p.y >= 0
}

func parse() (Grid, Mask) {
	ret := make(Grid)
	mask := make(Mask)

	for indexy, line := range lines {
		for indexx, element := range []byte(line) {
			ret[Point{indexx, indexy}] = element
		}
	}
	return ret, mask
}

func contains(sls []Vect, elmt Vect) bool {
	for _, e := range sls {
		if elmt == e {
			return true
		}
	}
	return false
}

/*
char => byte

	. => 46
	- => 45
	/ => 47
	\ => 92
	| => 124
*/
func loopb(room Grid, mask Mask, pos Point, direction int, visite []Vect) {
	if !pos.cmp() || contains(visite, Vect{pos, direction}) {
		return
	}

	mask[pos] = true
	visite = append(visite, Vect{pos, direction})

	switch direction {
	case 0: // up
		if room[pos] == 47 {
			loopb(room, mask, pos.incr(3), 3, visite)
		} else if room[pos] == 92 {
			loopb(room, mask, pos.incr(1), 1, visite)
		} else if room[pos] == 124 || room[pos] == 46 {
			loopb(room, mask, pos.incr(0), 0, visite)
		} else if room[pos] == 45 {
			loopb(room, mask, pos.incr(1), 1, visite)
			loopb(room, mask, pos.incr(3), 3, visite)
		}
	case 1: // left
		if room[pos] == 47 {
			loopb(room, mask, pos.incr(2), 2, visite)
		} else if room[pos] == 92 {
			loopb(room, mask, pos.incr(0), 0, visite)
		} else if room[pos] == 124 {
			loopb(room, mask, pos.incr(2), 2, visite)
			loopb(room, mask, pos.incr(0), 0, visite)
		} else if room[pos] == 45 || room[pos] == 46 {
			loopb(room, mask, pos.incr(1), 1, visite)
		}
	case 2: // down
		if room[pos] == 47 {
			loopb(room, mask, pos.incr(1), 1, visite)
		} else if room[pos] == 92 {
			loopb(room, mask, pos.incr(3), 3, visite)
		} else if room[pos] == 124 || room[pos] == 46 {
			loopb(room, mask, pos.incr(2), 2, visite)
		} else if room[pos] == 45 {
			loopb(room, mask, pos.incr(1), 1, visite)
			loopb(room, mask, pos.incr(3), 3, visite)
		}
	case 3: // right
		if room[pos] == 47 {
			loopb(room, mask, pos.incr(0), 0, visite)
		} else if room[pos] == 92 {
			loopb(room, mask, pos.incr(2), 2, visite)
		} else if room[pos] == 124 {
			loopb(room, mask, pos.incr(2), 2, visite)
			loopb(room, mask, pos.incr(0), 0, visite)
		} else if room[pos] == 45 || room[pos] == 46 {
			loopb(room, mask, pos.incr(3), 3, visite)
		}
	}
}

func main() {
	room, mask := parse()

	loopb(room, mask, Point{0, 0}, 3, make([]Vect, 0))
	/* for k, v := range mask {
		fmt.Println("test: ", k, v)
	} */
	// fmt.Println(finalCount(mask))
	//pos, mask = fillLine(room, mask, pos.incr(2), 2)
	fmt.Println(len(mask))
}
