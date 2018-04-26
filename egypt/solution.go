package main

import (
        "fmt"
        "math"
        "sort"
)

func main() {
        var a, b, c float64
        for i := 0; i < 1000; i++ {
                fmt.Scan(&a, &b, &c)
                sides := []float64{a, b, c}
                sort.Float64s(sides)
                switch {
                case sides[0] == 0 && sides[1] == 0 && sides[2] == 0:
                        goto End
                case math.Pow(sides[0], 2)+math.Pow(sides[1], 2) == math.Pow(sides[2], 2):
                        fmt.Println("right")
                default:
                        fmt.Println("wrong")
                }
        }
End:
}
