fun insertionSort(arr: IntArray) {
    val n = arr.size
    
    for (i in 1 until n) {
        val key = arr[i]
        var j = i - 1
        
    
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j]
            j--
        }
        
        arr[j + 1] = key
    }
}

fun main() {
    val arr = intArrayOf(64, 25, 12, 22, 11)
    insertionSort(arr)
    println("Sorted array: ${arr.joinToString()}")
}
