package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		var b, p float64
		fmt.Scan(&b, &p)
		var bpm float64 = 60.0 * b / p
		var x float64 = bpm / b
		fmt.Printf("%.4f %.4f %.4f\n", bpm-x, bpm, bpm+x)
	}
}
