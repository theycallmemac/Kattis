package main

import "fmt"

func main() {
    fmt.Println("Hello World!")
}
[● mac@valhalla ~/go_projects/src/kattis] cat hissingmicrophone.go
package main

import (
        "fmt"
        "os"
)

func main() {
        var s string
        fmt.Scan(&s)
        runes := []rune(s)
        for i := 0; i < len(runes) - 1; i++ {
                if runes[i] == 's' && runes[i+1] == 's' {
                        fmt.Println("hiss")
                        os.Exit(0)
                }
        }
        fmt.Println("no hiss")
}
