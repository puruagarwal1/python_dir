/**
 * You can edit, run, and share this code.
 * play.kotlinlang.org
 */
fun mergeSort(arr: IntArray) {
    if (arr.size <= 1) {
        return
    }
    
    val middle = arr.size / 2
    val left = arr.copyOfRange(0, middle)
    val right = arr.copyOfRange(middle, arr.size)
    
    mergeSort(left)
    mergeSort(right)
    
    merge(arr, left, right)
}

fun merge(arr: IntArray, left: IntArray, right: IntArray) {
    var i = 0
    var j = 0
    var k = 0
    
    while (i < left.size && j < right.size) {
        if (left[i] < right[j]) {
            arr[k++] = left[i++]
        } else {
            arr[k++] = right[j++]
        }
    }
    
    while (i < left.size) {
        arr[k++] = left[i++]
    }
    
    while (j < right.size) {
        arr[k++] = right[j++]
    }
}

fun main() {
    val arr = intArrayOf(12, 11, 13, 5, 6, 7)
    println("Original Array: ${arr.joinToString()}")
    
    mergeSort(arr)
    
    println("Sorted Array: ${arr.joinToString()}")
}
