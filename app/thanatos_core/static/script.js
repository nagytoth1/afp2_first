//This function initializes the countElapsedTime() method and is called/activated when user presses a button or reaches a page
function start() {
    startTime = performance.now();
    countElapsedTime(startTime, 0);
};

//Counts the elapsed time from the start (from when the student reaches the page)
function countElapsedTime(startTime, elapsedMinutes) {
    currentTime = performance.now();
    var elapsedSeconds = Math.round((currentTime - startTime) / 1000);

    if(elapsedSeconds > 4) //60 másodperc elteltével resetel
    {
        elapsedMinutes += 1;
        startTime = currentTime;
        elapsedSeconds = 0;
    }
    
    var elapsedTime = `${elapsedMinutes} perc ${elapsedSeconds} másodperc`;
    
    document.getElementById('time').innerHTML = elapsedTime;
    setTimeout(function() {
        countElapsedTime(startTime, elapsedMinutes);
    }, 1000);

    if(elapsedMinutes >= 45)
    {
        var time = document.getElementById('time');
        time.innerHTML = "Most már azért felkelnék a géptől... " + elapsedTime;
        time.style.color = 'red';
    }
}

//Checks whether the selected radiobutton contains the correct answer or not.
function checkAnswer(id, answer) {
    //gets every single radiobutton to a list (NodeListOf<HTMLElement>)
    result = id == answer ? "✔" : "❌";
    document.getElementById('isCorrect').innerHTML = result;
}

function getCurrentTime() {
    var today = new Date();
    var currHour = today.getHours().toString().padStart(2, "0");
    var currMinute = today.getMinutes().toString().padStart(2, "0");
    var currSec = today.getSeconds().toString().padStart(2, "0");
    var currentTime = `${currHour}:${currMinute}:${currSec}`;
    document.getElementById('currentTime').innerHTML = currentTime;
    setTimeout(function () { getCurrentTime() }, 1000);
}

