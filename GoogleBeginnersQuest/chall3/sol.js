function controlCar(scanArray){
//console.log(scanArray);
let i = scanArray.lastIndexOf(Math.max(...scanArray));

if (i <= 8){
 //console.log("Moving to the left. the furthest car is " + scanArray[i].toString() + " meters away. Using index: " + i.toString());
 return -1;
} else if ((i === 7 || i === 9) && scanArray[7] == scanArray[8] && scanArray[8] == scanArray[9] ){
 //console.log("staying course. The furthest car is " + scanArray[i].toString() + " meters away. Using index: " + i.toString())
 return 0; 
} else{
 //console.log("Moving to the right. The furthest car is " + scanArray[i].toString() + " meters away. Using index: " + i.toString());
return 1;
}