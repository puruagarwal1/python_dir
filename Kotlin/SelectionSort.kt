fun selectionSort(arr: IntArray) {
    val n = arr.size
    
    for (i in 0 until n - 1) {
        var minIndex = i
        
        
        for (j in i + 1 until n) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j
            }
        }
        
        val temp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = temp
    }
}

fun main() {
    val arr = intArrayOf(64, 25, 12, 22, 11)
    selectionSort(arr)
    println("Sorted array: ${arr.joinToString()}")
}
