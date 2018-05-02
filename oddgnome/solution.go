package main

import (
        "fmt"
)

func outOfPlace(a []int) int {
        for k := 1; k < len(a)-1; k++ {
                if a[k-1]+1 != a[k] {
                        return (k + 1)
                }
        }
        return 0
}

func readArray(arr []int, g int) []int {
        m := 0
        for j := 0; j < g; j++ {
                fmt.Scan(&m)
                arr = append(arr, m)
        }
        return arr
}

func main() {
        n, g := 0, 0
        fmt.Scan(&n)
        for i := 0; i < n; i++ {
                fmt.Scan(&g)
                var arr = make([]int, 0)
                arr = readArray(arr, g)
                pos := outOfPlace(arr)
                fmt.Println(pos)
        }
}
