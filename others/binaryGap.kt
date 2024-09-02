fun solution(N:Int): Int{
    val binaryRepresentation = N.toString(2)
    
    var maxGap = 0
    var currentGap = 0
    var inGap = false

    for (char in binaryRepresentation){
        if (char == '1'){
            if(inGap){
                maxGap= maxOf(maxGap, currentGap)
                currentGap = 0
            }
            inGap = true
        } else if(inGap){
            currentGap++
        }
    }
    return maxGap

}


fun main(){
    println("Binary gap in 32 :  ${solution(32)}")
    println("Binary Gap in 1041 : ${solution(1041)}")
}