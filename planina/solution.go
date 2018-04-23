package main

import (
        "fmt"
)

var s float64 = 2

func planina(n float64) float64 {
        var i float64 = 0
        for i < n {
                s = s + s - 1
                i++
        }
        return s * s
}

func main() {
        var n float64
        fmt.Scan(&n)
        result := planina(n)
        fmt.Printf("%.0f", result)
}
