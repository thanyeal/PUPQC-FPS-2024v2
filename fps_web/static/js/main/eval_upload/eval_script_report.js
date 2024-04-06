
function printDiv(divName) {
    var printWindow = window.open('', '', 'width=1080,height=720');
    printWindow.document.write('<html><head><title>Faculty Performance System</title></head><body>');
    printWindow.document.write(document.getElementById(divName).innerHTML);
    printWindow.document.write('</body>');
    printWindow.document.close(); // Necessary for IE
    printWindow.focus();
    printWindow.print();
    printWindow.close();
}