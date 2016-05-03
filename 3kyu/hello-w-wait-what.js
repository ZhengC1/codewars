/*
 * This is hello world, without
 * strings
 * regex
 * numbers
 * functions with the names
 * any object keys with the names. 
 */
var helloWorld = function () {
    var one = Number(true);
    var dog = one + one;
    var four = dog * dog;
    var eight = dog * dog * dog;
    var sixteen = dog * dog * dog * dog;
    var thirtyTwo = dog * dog * dog * dog * dog;
    var sixtyFour = dog * dog * dog * dog * dog * dog;
    var oneTwentyEight = dog * dog * dog * dog * dog * dog * dog;

    var H = sixtyFour + eight; var h = oneTwentyEight - sixteen - eight;
    var e = h - dog - one;
    var l = h + four; 
    var o =  l + dog + one;
    var space = thirtyTwo;
    var W = sixtyFour + sixteen + four + dog + one;
    var w = oneTwentyEight - eight - one;
    var r = h + eight + dog;
    var d = h - four;
    var excl = thirtyTwo + one;
    return String.fromCharCode(H,e,l,l,o, space, W,o,r,l,d,excl);
}
