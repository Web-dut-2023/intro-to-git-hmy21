document.addEventListener('DOMContentLoaded', function() {
    var searchBtn = document.getElementById('search-btn');
    if (searchBtn) {
        searchBtn.addEventListener('click', function() {
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
    }
    document.getElementById('sort-price').addEventListener('click', function() {
        console.log('sort-price button clicked');
        sortTrains('cost');
    });

    document.getElementById('sort-origin').addEventListener('click', function() {
        console.log('sort-origin button clicked');
        sortTrains('origin');
    });

    document.getElementById('sort-destination').addEventListener('click', function() {
        console.log('sort-destination button clicked');
        sortTrains('destination');
    });
});

function sortTrains(key) {
    console.log('sortTrains function called with key:', key);
    var trainRows = Array.from(document.querySelectorAll('.train-row'));
    trainRows.sort(function(a, b) {
        var aValue = a.getAttribute('data-train-' + key);
        var bValue = b.getAttribute('data-train-' + key);
        console.log('Comparing', aValue, 'and', bValue);
        if (aValue < bValue) {
            return -1;
        } else if (aValue > bValue) {
            return 1;
        } else {
            return 0;
        }
    });

    var trainList = document.querySelector('.train-list');
    trainRows.forEach(function(row) {
        console.log('Appending row', row);
        trainList.appendChild(row);
    });
}