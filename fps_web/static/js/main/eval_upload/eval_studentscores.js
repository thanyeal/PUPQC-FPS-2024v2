
const valueToSetThree = percentaging.count_ra3;
const valueToSetFour  = percentaging.count_rb3;

if (valueToSetThree && valueToSetFour == null) {
    document.querySelector("#caption-query-changer").innerHTML = '<p class="text-center" style="margin-top: 5% !important;">No data available.</p>';
}
else {
    console.log("received")
    const ra3 = document.getElementById('ra3');
    ra3.textContent = valueToSetThree;
    
    const rb3 = document.getElementById('rb3');
    rb3.textContent = valueToSetFour;
}