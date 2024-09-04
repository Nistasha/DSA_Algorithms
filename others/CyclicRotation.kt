/**
 * 
CyclicRotation
Rotate an array to the right by a given number of steps.

 */
fun solution (A: IntArray, K: Int): IntArray{
    val N= A.size
    if (N== 0) return A //if array is empty
    val effectiveK = K % N
    
    if (effectiveK == 0) return A
    var rotatedArray = IntArray(N)
    for (i in A.indices){
        val newIndex= (i + effectiveK)% N
        rotatedArray[newIndex] = A[i] 
    }
    return rotatedArray
}
fun main() {
    val A= intArrayOf(3, 8, 9, 7, 6)
    val K = 2
    print("rotatedarray is : ${solution(A, K).contentToString()}")
    
}