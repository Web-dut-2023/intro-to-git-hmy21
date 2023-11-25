
document.getElementById('search-btn').addEventListener('click', function() {
    var searchValue = document.getElementById('search-box').value.toUpperCase();
    var trainRows = document.querySelectorAll('.train-row');
    for (var i = 0; i < trainRows.length; i++) {
        var trainNum = trainRows[i].getAttribute('data-train-num');
        if (trainNum.indexOf(searchValue) > -1) {
            trainRows[i].style.display = '';
        } else {
            trainRows[i].style.display = 'none';
        }
    }
});