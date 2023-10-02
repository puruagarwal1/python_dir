fun main() {
    val n = 10
    var firstNumber = 0
    var secondNumber = 1

    println("First $n Fibonacci numbers:")

    for (i in 1..n) {
        print("$firstNumber ")

        val nextNumber = firstNumber + secondNumber
        firstNumber = secondNumber
        secondNumber = nextNumber
    }
}
