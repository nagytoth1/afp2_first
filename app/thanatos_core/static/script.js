function start() {
    startTime = performance.now();
    countElapsedTime(startTime, 0);
};

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
function checkAnswer(answer) {
    //gets every single radiobutton to a list (NodeListOf<HTMLElement>)
    var buttons = document.getElementsByName('gender');
    var result = "❌";
      
    for(i = 0; i < buttons.length; i++) {
        if(buttons[i].checked && buttons[i].value == answer)
            result = "✔";
    }
    console.log(result);
    document.getElementById('result').innerHTML = result;
}