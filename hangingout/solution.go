package main

import "fmt"

func main() {
        l, n, p, a, t, r := 0, 0, 0, "", 0, 0
        fmt.Scan(&l, &n)
        for i := 0; i < n; i++ {
                fmt.Scan(&a, &p)
                switch a {
                case "enter":
                        switch {
                        case t+p <= l:
                                t += p
                        case t+p > l:
                                r += 1
                        }
                case "leave":
                        t -= p
                }
        }
        fmt.Println(r)
}
