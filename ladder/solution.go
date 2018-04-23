package main

import (
        "fmt"
        "math"
)

func main() {
        var h, v float64
        fmt.Scan(&h, &v)
        r := math.Pi / 180.00 * v
        fmt.Println(math.Ceil(h/math.Sin(r)))
}
