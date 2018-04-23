package main

import (
        "fmt"
)

func main() {
        var n, bat, count float64
        var total, i float64 = 0, 0
        fmt.Scan(&n)
        for i < n {
                fmt.Scan(&bat)
                if bat >= 0 {
                        total += bat
                        count++
                } else {
                    total = total
                }
                i++
        }
        fmt.Println(total / count)
}
