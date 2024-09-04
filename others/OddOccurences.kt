/**
 * Find value that occurs in odd number of elements
 
 */
fun solution (A: IntArray): Int{
    var unpaired = 0
    for (element in A){
        unpaired = unpaired xor element
        print (unpaired)
    }
    return unpaired
}
fun main() {
    val A= intArrayOf(3, 8, 6, 3, 8)
    print("Unpaired element is : ${solution(A)}")
    
}