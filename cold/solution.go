package main

import (
        "fmt"
)

func main() {
        var n, t int
        var sum int = 0
        fmt.Scan(&n)
        var arr [100]int
        for i := 0; i < n; i++ {
                fmt.Scan(&t)
                arr[i] = t
        }
        for j := 0; j < n; j++ {
                if arr[j] < 0 {
                        sum++
                }
        }
        fmt.Println(sum)
}
