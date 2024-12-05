let RunSentimentAnalysis = () => {
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            // Display the server response (either the result or the error message)
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        } else if (this.readyState == 4 && this.status == 400) {
            // Handle error response
            document.getElementById("system_response").innerHTML = "Invalid text! Please try again.";
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + textToAnalyze, true);
    xhttp.send();
}
